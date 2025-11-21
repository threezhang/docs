#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 3 Pro Image Preview (Nano Banana 2) - 预览版演示
模型：gemini-3-pro-image-preview

特点：
- 基于 Gemini 3，更强推理能力
- 支持 1K/2K/4K 三种分辨率
- 支持多图参考（最多 14 张）
- 内置思考模式，自动优化构图
- 支持 Google 搜索接地
- 价格：$0.05/张

使用前准备：
1. 安装依赖：pip install requests
2. 配置 API Key：在同目录下的 config.py 中设置
3. 运行：python3 nano_banana2_demo.py

支持的纵横比和分辨率：
- 1K: 标准分辨率（如 1024×1024）
- 2K: 高分辨率（如 2048×2048）
- 4K: 超高分辨率（如 4096×4096）
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

# API 端点（Nano Banana 2 预览版）
API_URL = "https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent"

# 演示场景配置
DEMO_SCENES = {
    "1": {
        "name": "4K 超高清文生图",
        "prompt": "A futuristic cyberpunk city at night, neon lights reflecting on wet streets, flying cars, towering skyscrapers, highly detailed, cinematic lighting, 4k quality",
        "aspect_ratio": "16:9",
        "image_size": "4K",
        "images": []
    },
    "2": {
        "name": "2K 高清文生图",
        "prompt": "A serene Japanese zen garden with cherry blossoms, koi pond, stone lanterns, peaceful atmosphere, spring season, professional photography",
        "aspect_ratio": "4:3",
        "image_size": "2K",
        "images": []
    },
    "3": {
        "name": "图生图 - 风格迁移",
        "prompt": "Transform this image into Van Gogh's Starry Night style, with swirling brushstrokes and vibrant colors",
        "aspect_ratio": "1:1",
        "image_size": "2K",
        "images": ["test_cat.jpg"]  # 需要准备测试图片
    },
    "4": {
        "name": "多图混合 - 创意合成",
        "prompt": "Create a whimsical scene combining these images: a cat playfully interacting with an apple on a wooden table, natural lighting, photorealistic",
        "aspect_ratio": "16:9",
        "image_size": "2K",
        "images": ["test_cat.jpg", "test_apple.jpg"]  # 需要准备测试图片
    }
}

OUTPUT_DIR = "."
# ============================


def download_test_image(url: str, filename: str) -> bool:
    """下载测试图片"""
    if os.path.exists(filename):
        print(f"✅ 测试图片已存在: {filename}")
        return True
    
    try:
        print(f"📥 正在下载测试图片: {filename}...")
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"✅ 下载成功: {filename}")
            return True
        else:
            print(f"❌ 下载失败: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 下载失败: {str(e)}")
        return False


def prepare_test_images():
    """准备测试图片"""
    # 使用 Unsplash 的测试图片
    test_images = {
        "test_cat.jpg": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80",
        "test_apple.jpg": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=800&q=80"
    }
    
    all_exist = True
    for filename, url in test_images.items():
        if not download_test_image(url, filename):
            all_exist = False
    
    return all_exist


def encode_image(image_path: str) -> tuple:
    """将图片编码为 base64"""
    try:
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
        
        # 根据扩展名判断 mime_type
        ext = os.path.splitext(image_path)[1].lower()
        mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
        
        return mime_type, image_data
    except Exception as e:
        print(f"❌ 读取图片失败 {image_path}: {str(e)}")
        return None, None


def generate_image(prompt: str, aspect_ratio: str = "1:1", 
                  image_size: str = "1K", image_paths: list = None) -> tuple:
    """
    生成图片并保存到本地
    
    参数:
        prompt: 提示词
        aspect_ratio: 纵横比
        image_size: 分辨率（1K/2K/4K）
        image_paths: 参考图片路径列表
    
    返回: (成功标志, 消息, 文件路径)
    """
    print("="*60)
    print("🎨 Gemini 3 Pro Image Preview - 图片生成")
    print("="*60)
    print(f"🚀 开始生成图片...")
    print(f"📝 提示词: {prompt}")
    print(f"📐 纵横比: {aspect_ratio}")
    print(f"🖼️  分辨率: {image_size}")
    if image_paths:
        print(f"🖼️  参考图片: {len(image_paths)} 张")
    
    # 构建请求数据
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    # 构建 parts（包含文本和可选的图片）
    parts = [{"text": prompt}]
    
    # 添加参考图片
    if image_paths:
        for image_path in image_paths:
            mime_type, image_data = encode_image(image_path)
            if mime_type and image_data:
                parts.append({
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": image_data
                    }
                })
    
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {
                "aspectRatio": aspect_ratio,
                "imageSize": image_size
            }
        }
    }
    
    try:
        print("📡 发送请求到 Gemini API...")
        
        # 发送请求
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=180  # 4K 生成可能需要更长时间
        )
        
        if response.status_code != 200:
            return False, f"API 请求失败，状态码: {response.status_code}", None
        
        # 解析响应
        result = response.json()
        
        # 提取图片数据
        if "candidates" not in result or len(result["candidates"]) == 0:
            return False, "未找到图片数据", None
        
        candidate = result["candidates"][0]
        if "content" not in candidate or "parts" not in candidate["content"]:
            return False, "响应格式错误", None
        
        parts = candidate["content"]["parts"]
        image_data = None
        
        for part in parts:
            if "inlineData" in part and "data" in part["inlineData"]:
                image_data = part["inlineData"]["data"]
                break
        
        if not image_data:
            return False, "未找到图片数据", None
        
        # 解码并保存图片
        print("💾 正在保存图片...")
        decoded_data = base64.b64decode(image_data)
        
        # 生成文件名
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"nano_banana2_{image_size}_{timestamp}.png"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        with open(filepath, 'wb') as f:
            f.write(decoded_data)
        
        file_size = len(decoded_data) / 1024  # KB
        
        print(f"✅ 图片已保存: {filepath}")
        print(f"📊 文件大小: {file_size:.2f} KB")
        
        return True, "生成成功", filepath
        
    except requests.exceptions.Timeout:
        return False, "请求超时（180秒）", None
    except requests.exceptions.ConnectionError:
        return False, "网络连接错误", None
    except Exception as e:
        return False, f"错误: {str(e)}", None


def main():
    """主函数 - 交互式演示"""
    print("\n" + "="*60)
    print("Gemini 3 Pro Image Preview (Nano Banana 2) 演示")
    print("预览版 | 1K/2K/4K 分辨率 | $0.05/张")
    print("="*60)
    print(f"⏰ 开始时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")
    
    # 显示演示场景
    print("请选择演示场景：\n")
    for key, scene in DEMO_SCENES.items():
        print(f"{key}. {scene['name']}")
        print(f"   分辨率: {scene['image_size']}, 纵横比: {scene['aspect_ratio']}")
        if scene['images']:
            print(f"   需要图片: {', '.join(scene['images'])}")
        print()
    
    choice = input("请输入选择 (1-4): ").strip()
    
    if choice not in DEMO_SCENES:
        print("❌ 无效选择")
        return
    
    scene = DEMO_SCENES[choice]
    
    # 如果需要图片，先准备
    if scene['images']:
        print("\n准备测试图片...")
        if not prepare_test_images():
            print("❌ 测试图片准备失败，无法继续")
            return
    
    # 生成图片
    print(f"\n开始执行场景: {scene['name']}\n")
    success, message, filepath = generate_image(
        prompt=scene['prompt'],
        aspect_ratio=scene['aspect_ratio'],
        image_size=scene['image_size'],
        image_paths=scene['images'] if scene['images'] else None
    )
    
    # 显示结果
    print("\n" + "="*60)
    if success:
        print("🎉 生成成功！")
        print(f"✅ {message}")
        print(f"📁 文件路径: {filepath}")
    else:
        print("❌ 生成失败")
        print(f"💥 {message}")
        print("\n建议检查:")
        print("  1. API 密钥是否正确（config.py）")
        print("  2. 网络连接是否正常")
        print("  3. 提示词是否合理")
    
    print(f"⏰ 结束时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)


if __name__ == "__main__":
    main()

