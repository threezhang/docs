#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 图像编辑 - Google 原生格式（测试版）
模型：gemini-3-pro-image-preview（最新版）/ gemini-2.5-flash-image（稳定版）

特点：
- 支持自定义纵横比（10 种比例）
- 支持高分辨率（1K/2K/4K，仅 Nano Banana 2）
- 更灵活的参数控制

使用方法：
1. 安装依赖：pip install requests
2. 直接运行：python3 gemini_native_demo.py

注意：此文件包含测试用 API Key，仅供内部测试使用。
"""

import requests
import base64
import os
import datetime

# ========== 配置区（测试用 Key）==========
API_KEY = "sk-9SOAt1Bkvcv97WDXE0464d8b0712406f86594f4968524fBd"

# 模型选择
USE_NANO_BANANA_2 = True  # True = 最新版（支持 4K），False = 稳定版（固定 1K）

if USE_NANO_BANANA_2:
    API_URL = "https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent"
    DEFAULT_IMAGE_SIZE = "2K"  # 1K, 2K, 4K
else:
    API_URL = "https://api.laozhang.ai/v1beta/models/gemini-2.5-flash-image:generateContent"
    DEFAULT_IMAGE_SIZE = None  # 稳定版不支持
# =========================================


def encode_image(image_path: str) -> tuple:
    """将图片编码为 base64"""
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    ext = os.path.splitext(image_path)[1].lower()
    mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
    
    return mime_type, image_data


def generate_image(prompt: str, aspect_ratio: str = "1:1", 
                  image_size: str = None, input_images: list = None) -> str:
    """
    生成或编辑图片
    
    参数:
        prompt: 提示词
        aspect_ratio: 纵横比 (21:9, 16:9, 4:3, 3:2, 1:1, 9:16, 3:4, 2:3, 5:4, 4:5)
        image_size: 分辨率 (1K, 2K, 4K)，仅 Nano Banana 2 支持
        input_images: 输入图片路径列表
    
    返回: 输出文件路径
    """
    print("="*60)
    print("🎨 Gemini 图像处理 - Google 原生格式")
    print("="*60)
    print(f"📝 提示词: {prompt}")
    print(f"📐 纵横比: {aspect_ratio}")
    if image_size:
        print(f"🖼️  分辨率: {image_size}")
    if input_images:
        print(f"📁 输入图片: {len(input_images)} 张")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    # 构建 parts
    parts = [{"text": prompt}]
    
    if input_images:
        for img_path in input_images:
            if os.path.exists(img_path):
                mime_type, img_data = encode_image(img_path)
                parts.append({
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": img_data
                    }
                })
    
    # 构建请求体
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
    if image_size and USE_NANO_BANANA_2:
        payload["generationConfig"]["imageConfig"]["imageSize"] = image_size
    
    print("📡 发送请求...")
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=180)
        
        if response.status_code != 200:
            print(f"❌ API 请求失败: {response.status_code}")
            print(response.text)
            return None
        
        result = response.json()
        
        # 提取图片数据
        image_data = result["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
        
        # 保存图片
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        size_suffix = f"_{image_size}" if image_size else ""
        filename = f"native_result{size_suffix}_{timestamp}.png"
        
        with open(filename, "wb") as f:
            f.write(base64.b64decode(image_data))
        
        file_size = os.path.getsize(filename) / 1024
        print(f"✅ 图片已保存: {filename}")
        print(f"📊 文件大小: {file_size:.2f} KB")
        
        return filename
        
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        return None


def test_text_to_image():
    """测试1：文生图"""
    print("\n" + "="*60)
    print("测试1：文生图 (16:9 宽屏)")
    print("="*60)
    
    generate_image(
        prompt="A futuristic cyberpunk city at night, neon lights, flying cars, 4k quality",
        aspect_ratio="16:9",
        image_size=DEFAULT_IMAGE_SIZE
    )


def test_text_to_image_4k():
    """测试2：4K 超高清文生图"""
    print("\n" + "="*60)
    print("测试2：4K 超高清文生图")
    print("="*60)
    
    if not USE_NANO_BANANA_2:
        print("⚠️ 4K 仅 Nano Banana 2 支持，跳过此测试")
        return
    
    generate_image(
        prompt="A serene Japanese zen garden with cherry blossoms, koi pond, professional photography",
        aspect_ratio="4:3",
        image_size="4K"
    )


def test_image_style_transfer():
    """测试3：图片风格转换"""
    print("\n" + "="*60)
    print("测试3：图片风格转换")
    print("="*60)
    
    test_image = "test_cat.jpg"
    if not os.path.exists(test_image):
        print(f"⚠️ 测试图片不存在: {test_image}，跳过此测试")
        return
    
    generate_image(
        prompt="Transform this image into Van Gogh's Starry Night style oil painting",
        aspect_ratio="1:1",
        image_size=DEFAULT_IMAGE_SIZE,
        input_images=[test_image]
    )


def test_multi_image_mix():
    """测试4：多图混合"""
    print("\n" + "="*60)
    print("测试4：多图混合")
    print("="*60)
    
    images = ["test_cat.jpg", "test_apple.jpg"]
    missing = [img for img in images if not os.path.exists(img)]
    
    if missing:
        print(f"⚠️ 测试图片不存在: {missing}，跳过此测试")
        return
    
    generate_image(
        prompt="Create a whimsical scene: a cat playfully interacting with an apple",
        aspect_ratio="16:9",
        image_size=DEFAULT_IMAGE_SIZE,
        input_images=images
    )


def main():
    """主函数"""
    model_name = "Nano Banana 2" if USE_NANO_BANANA_2 else "Nano Banana"
    print("="*60)
    print(f"Gemini 图像处理 - Google 原生格式（测试版）")
    print(f"模型: {model_name}")
    print("="*60)
    
    # 运行所有测试
    test_text_to_image()
    test_text_to_image_4k()
    test_image_style_transfer()
    test_multi_image_mix()
    
    print("\n" + "="*60)
    print("🎉 所有测试完成！")
    print("="*60)


if __name__ == "__main__":
    main()

