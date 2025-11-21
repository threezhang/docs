#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 2.5 Flash Image (Nano Banana) - 稳定版演示
模型：gemini-2.5-flash-image

特点：
- 稳定可靠，适合生产环境
- 固定 1K 分辨率 (1024×1024)
- 价格：$0.025/张（比官网便宜 37.5%）
- 速度快，约 10 秒生成

使用前准备：
1. 安装依赖：pip install requests
2. 配置 API Key：在同目录下的 config.py 中设置
3. 运行：python3 nano_banana_demo.py

支持的纵横比：
- 横向: 21:9, 16:9, 4:3, 3:2
- 正方形: 1:1
- 纵向: 9:16, 3:4, 2:3
- 其他: 5:4, 4:5
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

# API 端点（Nano Banana 稳定版）
API_URL = "https://api.laozhang.ai/v1beta/models/gemini-2.5-flash-image:generateContent"

# 图片描述（提示词）
PROMPT = "A cute British Shorthair cat sitting on a wooden table, natural lighting, high quality photography"

# 纵横比（可选）
ASPECT_RATIO = "16:9"  # 宽屏
# 其他选项: "1:1" (正方形), "9:16" (竖屏), "4:3", "21:9" 等

# 输出目录
OUTPUT_DIR = "."
# ============================


def generate_image(prompt: str, aspect_ratio: str = "1:1") -> tuple:
    """
    生成图片并保存到本地
    
    返回: (成功标志, 消息, 文件路径)
    """
    print("="*60)
    print("🎨 Gemini 2.5 Flash Image - 图片生成")
    print("="*60)
    print(f"🚀 开始生成图片...")
    print(f"📝 提示词: {prompt}")
    print(f"📐 纵横比: {aspect_ratio}")
    print(f"🖼️  分辨率: 1K (固定)")
    
    # 构建请求数据
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {
                "aspectRatio": aspect_ratio
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
            timeout=120
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
        filename = f"nano_banana_{timestamp}.png"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        with open(filepath, 'wb') as f:
            f.write(decoded_data)
        
        file_size = len(decoded_data) / 1024  # KB
        
        print(f"✅ 图片已保存: {filepath}")
        print(f"📊 文件大小: {file_size:.2f} KB")
        
        return True, "生成成功", filepath
        
    except requests.exceptions.Timeout:
        return False, "请求超时（120秒）", None
    except requests.exceptions.ConnectionError:
        return False, "网络连接错误", None
    except Exception as e:
        return False, f"错误: {str(e)}", None


def main():
    """主函数"""
    print("\n" + "="*60)
    print("Gemini 2.5 Flash Image (Nano Banana) 演示")
    print("稳定版 | 1K 分辨率 | $0.025/张")
    print("="*60)
    print(f"⏰ 开始时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")
    
    # 生成图片
    success, message, filepath = generate_image(PROMPT, ASPECT_RATIO)
    
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

