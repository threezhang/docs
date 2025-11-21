#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini Image Generation - 完整演示脚本
包含三个场景：文生图、单图生图、多图混合

使用方法：
1. 替换下方的 API_KEY
2. 根据需要修改配置参数
3. 运行: python3 complete_demo.py
"""

import requests
import base64
import os
from datetime import datetime

# ============================================================
# 配置区
# ============================================================

API_KEY = "sk-"  # 替换为你的 API Key

# 选择模型
USE_NANO_BANANA_2 = True  # True=Nano Banana 2 (4K), False=Nano Banana (1K)

if USE_NANO_BANANA_2:
    API_URL = "https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent"
    MODEL_NAME = "Nano Banana 2"
else:
    API_URL = "https://api.laozhang.ai/v1beta/models/gemini-2.5-flash-image:generateContent"
    MODEL_NAME = "Nano Banana"

# ============================================================
# 核心函数
# ============================================================

def generate_text_to_image(prompt, aspect_ratio="16:9", image_size="2K"):
    """
    场景1: 文生图 (Text-to-Image)
    """
    print(f"\n📝 提示词: {prompt}")
    print(f"📐 {aspect_ratio} | {image_size if USE_NANO_BANANA_2 else '1K'}")
    
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect_ratio}
        }
    }
    
    if USE_NANO_BANANA_2 and image_size:
        payload["generationConfig"]["imageConfig"]["imageSize"] = image_size
    
    return _call_api(payload, f"result_1_text_to_image")


def generate_image_to_image(input_image, prompt, aspect_ratio="1:1", image_size="2K"):
    """
    场景2: 单图生图 (Image-to-Image)
    """
    print(f"\n📁 输入: {input_image}")
    print(f"📝 提示词: {prompt}")
    print(f"📐 {aspect_ratio} | {image_size if USE_NANO_BANANA_2 else '1K'}")
    
    if not os.path.exists(input_image):
        print(f"❌ 找不到图片")
        return False
    
    with open(input_image, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    ext = os.path.splitext(input_image)[1].lower()
    mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
    
    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {"inline_data": {"mime_type": mime_type, "data": image_b64}}
            ]
        }],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect_ratio}
        }
    }
    
    if USE_NANO_BANANA_2 and image_size:
        payload["generationConfig"]["imageConfig"]["imageSize"] = image_size
    
    return _call_api(payload, f"result_2_image_style_transfer")


def generate_multi_image_mix(image_list, prompt, aspect_ratio="16:9", image_size="2K"):
    """
    场景3: 多图混合 (Multi-Image Mix)
    """
    print(f"\n📁 输入: {len(image_list)} 张图片")
    print(f"📝 提示词: {prompt}")
    print(f"📐 {aspect_ratio} | {image_size if USE_NANO_BANANA_2 else '1K'}")
    
    parts = [{"text": prompt}]
    
    for img_path in image_list:
        if not os.path.exists(img_path):
            print(f"❌ 找不到: {img_path}")
            return False
        
        with open(img_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode("utf-8")
        
        ext = os.path.splitext(img_path)[1].lower()
        mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
        parts.append({"inline_data": {"mime_type": mime_type, "data": img_b64}})
    
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect_ratio}
        }
    }
    
    if USE_NANO_BANANA_2 and image_size:
        payload["generationConfig"]["imageConfig"]["imageSize"] = image_size
    
    return _call_api(payload, f"result_3_multi_image_mix")


def _call_api(payload, prefix):
    """
    调用 API 并保存图片
    """
    print("🚀 生成中...", end=" ")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=180)
        
        if response.status_code != 200:
            print(f"\n❌ 失败: {response.status_code}")
            return False
        
        result = response.json()
        
        if "candidates" not in result or len(result["candidates"]) == 0:
            print("\n❌ 失败: 无图片数据")
            return False
        
        image_data = result["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
        filename = f"{prefix}.png"
        
        with open(filename, "wb") as f:
            f.write(base64.b64decode(image_data))
        
        file_size = len(base64.b64decode(image_data)) / 1024 / 1024
        print(f"✅ 已保存: {filename} ({file_size:.1f} MB)")
        
        return True
        
    except requests.exceptions.Timeout:
        print("\n❌ 超时")
        return False
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        return False


# ============================================================
# 主程序
# ============================================================

def main():
    print("\n" + "="*60)
    print("🎨 Gemini 图像生成 - 三个场景演示")
    print("="*60)
    print(f"🤖 模型: {MODEL_NAME}")
    if USE_NANO_BANANA_2:
        print(f"💰 价格: $0.05/张 | 分辨率: 1K/2K/4K")
    else:
        print(f"💰 价格: $0.025/张 | 分辨率: 1K")
    print("="*60)
    
    # ============================================================
    # 场景 1: 文生图 → 生成第一张图
    # ============================================================
    
    print("\n▶️  场景 1: 文生图 → 生成第一张图")
    success1 = generate_text_to_image(
        prompt="一只可爱的橘猫",
        aspect_ratio="1:1",
        image_size="2K" if USE_NANO_BANANA_2 else None
    )
    
    # ============================================================
    # 场景 2: 单图生图 → 用第一张图生成第二张图
    # ============================================================
    
    print("\n▶️  场景 2: 单图生图 → 用第一张图生成第二张图")
    
    if os.path.exists("result_1_text_to_image.png"):
        success2 = generate_image_to_image(
            input_image="result_1_text_to_image.png",
            prompt="把这只猫变成梵高星空风格的油画",
            aspect_ratio="1:1",
            image_size="2K" if USE_NANO_BANANA_2 else None
        )
    else:
        print("⚠️  跳过: 需要先运行场景 1")
        success2 = None
    
    # ============================================================
    # 场景 3: 多图混合 → 用第一张和第二张生成第三张图
    # ============================================================
    
    print("\n▶️  场景 3: 多图混合 → 用第一张和第二张生成第三张图")
    
    if os.path.exists("result_1_text_to_image.png") and os.path.exists("result_2_image_style_transfer.png"):
        success3 = generate_multi_image_mix(
            image_list=["result_1_text_to_image.png", "result_2_image_style_transfer.png"],
            prompt="将这两只猫融合成一个艺术作品",
            aspect_ratio="16:9",
            image_size="2K" if USE_NANO_BANANA_2 else None
        )
    else:
        print("⚠️  跳过: 需要先运行场景 1 和 2")
        success3 = None
    
    # ============================================================
    # 总结
    # ============================================================
    
    print("\n" + "="*60)
    print("✅ 演示完成")
    print("="*60)
    print(f"场景 1: {'✅ 成功' if success1 else '❌ 失败'}")
    print(f"场景 2: {'✅ 成功' if success2 else '⏭️ 跳过' if success2 is None else '❌ 失败'}")
    print(f"场景 3: {'✅ 成功' if success3 else '⏭️ 跳过' if success3 is None else '❌ 失败'}")
    print("="*60)


if __name__ == "__main__":
    main()

