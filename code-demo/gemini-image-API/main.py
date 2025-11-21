#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini Image Generation - 完整交互式演示
包含 Nano Banana (稳定版) 和 Nano Banana 2 (预览版) 两个模型

功能特点：
- 交互式菜单选择场景
- 支持两个模型切换
- 支持 1K/2K/4K 分辨率
- 自动下载测试图片
- 完善的错误处理

使用前准备：
1. 安装依赖：pip install requests
2. 配置 API Key：在同目录下的 config.py 中设置 API_KEY
3. 运行：python3 main.py

模型对比：
┌────────────────────┬───────────────────┬────────────────────┐
│ 特性               │ Nano Banana       │ Nano Banana 2      │
├────────────────────┼───────────────────┼────────────────────┤
│ 模型ID             │ gemini-2.5-flash  │ gemini-3-pro-image │
│ 状态               │ 稳定版            │ 预览版             │
│ 分辨率             │ 固定 1K           │ 1K/2K/4K          │
│ 价格               │ $0.025/张         │ $0.05/张          │
│ 思考模式           │ ❌                │ ✅                │
│ 搜索接地           │ ❌                │ ✅                │
│ 多图参考           │ 基础              │ 最多14张          │
│ 推荐场景           │ 生产环境          │ 追求最佳效果      │
└────────────────────┴───────────────────┴────────────────────┘
"""

import requests
import base64
import os
import datetime

# ========== 配置区 ==========
# 从 config.py 读取 API Key
try:
    from config import API_KEY
except ImportError:
    print("❌ 错误：找不到 config.py 文件")
    print("请在同目录下创建 config.py 文件，内容为：")
    print('API_KEY = "sk-YOUR_API_KEY"')
    exit(1)

# API 端点配置
API_ENDPOINTS = {
    "nano_banana": "https://api.laozhang.ai/v1beta/models/gemini-2.5-flash-image:generateContent",
    "nano_banana2": "https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent"
}

OUTPUT_DIR = "."
# ============================


class GeminiImageGenerator:
    """Gemini 图片生成器"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    
    def download_test_image(self, url: str, filename: str) -> bool:
        """下载测试图片"""
        if os.path.exists(filename):
            print(f"  ✅ 图片已存在: {filename}")
            return True
        
        try:
            print(f"  📥 下载中: {filename}...")
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"  ✅ 下载成功: {filename}")
                return True
            else:
                print(f"  ❌ 下载失败: HTTP {response.status_code}")
                return False
        except Exception as e:
            print(f"  ❌ 下载失败: {str(e)}")
            return False
    
    def prepare_test_images(self):
        """准备测试图片"""
        test_images = {
            "test_cat.jpg": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80",
            "test_apple.jpg": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=800&q=80"
        }
        
        print("\n📦 准备测试图片...")
        all_exist = True
        for filename, url in test_images.items():
            if not self.download_test_image(url, filename):
                all_exist = False
        
        return all_exist
    
    def encode_image(self, image_path: str) -> tuple:
        """将图片编码为 base64"""
        try:
            with open(image_path, "rb") as f:
                image_data = base64.b64encode(f.read()).decode("utf-8")
            
            ext = os.path.splitext(image_path)[1].lower()
            mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
            
            return mime_type, image_data
        except Exception as e:
            print(f"❌ 读取图片失败 {image_path}: {str(e)}")
            return None, None
    
    def generate(self, model_type: str, prompt: str, aspect_ratio: str = "1:1",
                image_size: str = None, image_paths: list = None) -> tuple:
        """
        生成图片
        
        参数:
            model_type: 模型类型 ("nano_banana" 或 "nano_banana2")
            prompt: 提示词
            aspect_ratio: 纵横比
            image_size: 分辨率 (仅 Nano Banana 2 支持 "1K"/"2K"/"4K")
            image_paths: 参考图片路径列表
        
        返回: (成功标志, 消息, 文件路径)
        """
        api_url = API_ENDPOINTS[model_type]
        model_name = "Nano Banana" if model_type == "nano_banana" else "Nano Banana 2"
        
        print("\n" + "="*60)
        print(f"🎨 {model_name} - 图片生成")
        print("="*60)
        print(f"🚀 开始生成...")
        print(f"📝 提示词: {prompt[:60]}{'...' if len(prompt) > 60 else ''}")
        print(f"📐 纵横比: {aspect_ratio}")
        
        if image_size and model_type == "nano_banana2":
            print(f"🖼️  分辨率: {image_size}")
        else:
            print(f"🖼️  分辨率: 1K (固定)")
        
        if image_paths:
            print(f"🖼️  参考图片: {len(image_paths)} 张")
        
        # 构建 parts
        parts = [{"text": prompt}]
        
        if image_paths:
            for image_path in image_paths:
                mime_type, image_data = self.encode_image(image_path)
                if mime_type and image_data:
                    parts.append({
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": image_data
                        }
                    })
        
        # 构建 payload
        payload = {
            "contents": [{"parts": parts}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {
                    "aspectRatio": aspect_ratio
                }
            }
        }
        
        # 添加分辨率参数（仅 Nano Banana 2）
        if image_size and model_type == "nano_banana2":
            payload["generationConfig"]["imageConfig"]["imageSize"] = image_size
        
        try:
            print("📡 发送请求...")
            
            timeout = 180 if (image_size == "4K") else 120
            response = requests.post(
                api_url,
                headers=self.headers,
                json=payload,
                timeout=timeout
            )
            
            if response.status_code != 200:
                return False, f"API 请求失败，状态码: {response.status_code}", None
            
            result = response.json()
            
            # 提取图片数据
            if "candidates" not in result or len(result["candidates"]) == 0:
                return False, "未找到图片数据", None
            
            candidate = result["candidates"][0]
            if "content" not in candidate or "parts" not in candidate["content"]:
                return False, "响应格式错误", None
            
            parts_response = candidate["content"]["parts"]
            image_data = None
            
            for part in parts_response:
                if "inlineData" in part and "data" in part["inlineData"]:
                    image_data = part["inlineData"]["data"]
                    break
            
            if not image_data:
                return False, "未找到图片数据", None
            
            # 保存图片
            print("💾 正在保存...")
            decoded_data = base64.b64decode(image_data)
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            size_tag = f"_{image_size}" if image_size else ""
            filename = f"gemini_{model_type}{size_tag}_{timestamp}.png"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            
            with open(filepath, 'wb') as f:
                f.write(decoded_data)
            
            file_size = len(decoded_data) / 1024
            
            print(f"✅ 保存成功: {filepath}")
            print(f"📊 文件大小: {file_size:.2f} KB")
            
            return True, "生成成功", filepath
            
        except requests.exceptions.Timeout:
            return False, f"请求超时（{timeout}秒）", None
        except requests.exceptions.ConnectionError:
            return False, "网络连接错误", None
        except Exception as e:
            return False, f"错误: {str(e)}", None


def show_menu():
    """显示主菜单"""
    print("\n" + "="*60)
    print("Gemini Image Generation - 交互式演示")
    print("="*60)
    print("\n请选择演示场景：\n")
    print("【Nano Banana - 稳定版 ($0.025/张)】")
    print("1. 文生图 - 1K 分辨率（快速稳定）")
    print()
    print("【Nano Banana 2 - 预览版 ($0.05/张)】")
    print("2. 文生图 - 4K 超高清（极致质量）")
    print("3. 文生图 - 2K 高清（平衡选择）")
    print("4. 图生图 - 风格迁移（需要测试图片）")
    print("5. 多图混合 - 创意合成（需要测试图片）")
    print()
    print("0. 退出")
    print("="*60)


def main():
    """主函数"""
    print("\n" + "="*60)
    print("🎨 Gemini Image Generation")
    print("完整交互式演示")
    print("="*60)
    print(f"⏰ 启动时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    generator = GeminiImageGenerator(API_KEY)
    
    # 定义演示场景
    scenes = {
        "1": {
            "name": "Nano Banana 文生图 (1K)",
            "model": "nano_banana",
            "prompt": "A cute British Shorthair cat sitting on a wooden table, soft natural lighting, high quality photography, 4k",
            "aspect_ratio": "16:9",
            "image_size": None,
            "images": None
        },
        "2": {
            "name": "Nano Banana 2 文生图 (4K)",
            "model": "nano_banana2",
            "prompt": "A futuristic cyberpunk city at night, neon lights reflecting on wet streets, flying cars, towering skyscrapers, highly detailed, cinematic lighting, ultra high resolution",
            "aspect_ratio": "16:9",
            "image_size": "4K",
            "images": None
        },
        "3": {
            "name": "Nano Banana 2 文生图 (2K)",
            "model": "nano_banana2",
            "prompt": "A serene Japanese zen garden with cherry blossoms, koi pond, stone lanterns, peaceful atmosphere, spring season, professional photography",
            "aspect_ratio": "4:3",
            "image_size": "2K",
            "images": None
        },
        "4": {
            "name": "Nano Banana 2 图生图 - 风格迁移",
            "model": "nano_banana2",
            "prompt": "Transform this image into Van Gogh's Starry Night style painting, with characteristic swirling brushstrokes, vibrant blues and yellows, impressionist technique",
            "aspect_ratio": "1:1",
            "image_size": "2K",
            "images": ["test_cat.jpg"]
        },
        "5": {
            "name": "Nano Banana 2 多图混合",
            "model": "nano_banana2",
            "prompt": "Create a whimsical photorealistic scene: this cute cat is curiously sniffing this red apple on a rustic wooden table, soft window light, cozy atmosphere",
            "aspect_ratio": "16:9",
            "image_size": "2K",
            "images": ["test_cat.jpg", "test_apple.jpg"]
        }
    }
    
    while True:
        show_menu()
        choice = input("\n请输入选择 (0-5): ").strip()
        
        if choice == "0":
            print("\n👋 感谢使用，再见！")
            break
        
        if choice not in scenes:
            print("\n❌ 无效选择，请重新输入")
            continue
        
        scene = scenes[choice]
        
        # 如果需要图片，先准备
        if scene["images"]:
            if not generator.prepare_test_images():
                print("\n❌ 测试图片准备失败")
                input("\n按 Enter 继续...")
                continue
        
        # 执行生成
        print(f"\n▶️  执行场景: {scene['name']}")
        
        success, message, filepath = generator.generate(
            model_type=scene["model"],
            prompt=scene["prompt"],
            aspect_ratio=scene["aspect_ratio"],
            image_size=scene["image_size"],
            image_paths=scene["images"]
        )
        
        # 显示结果
        print("\n" + "="*60)
        if success:
            print("🎉 生成成功！")
            print(f"📁 文件: {filepath}")
        else:
            print("❌ 生成失败")
            print(f"💥 原因: {message}")
        print("="*60)
        
        input("\n按 Enter 继续...")


if __name__ == "__main__":
    main()

