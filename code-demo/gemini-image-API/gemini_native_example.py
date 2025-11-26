#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 图像编辑 - Google 原生格式（用户示例版）
模型：gemini-3-pro-image-preview（最新版）/ gemini-2.5-flash-image（稳定版）

特点：
- 支持自定义纵横比（10 种比例）
- 支持高分辨率（1K/2K/4K，仅 Nano Banana 2）
- 更灵活的参数控制

使用方法：
1. 安装依赖：pip install requests
2. 在下方配置区填入您的 API Key
3. 运行：python3 gemini_native_example.py

获取 API Key：https://api.laozhang.ai/token

支持的纵横比：
- 横向: 21:9 (超宽屏), 16:9 (宽屏), 4:3, 3:2
- 正方形: 1:1
- 纵向: 9:16 (竖屏), 3:4, 2:3
- 其他: 5:4, 4:5

支持的分辨率（仅 Nano Banana 2）：
- 1K: 标准分辨率
- 2K: 高分辨率
- 4K: 超高分辨率
"""

import requests
import base64
import os
import datetime

# ========== 配置区（请填入您的 API Key）==========
API_KEY = "sk-YOUR_API_KEY"  # 替换为您的 API Key

# 模型选择
USE_NANO_BANANA_2 = True  # True = 最新版（支持 4K），False = 稳定版（固定 1K）

if USE_NANO_BANANA_2:
    API_URL = "https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent"
    DEFAULT_IMAGE_SIZE = "2K"  # 1K, 2K, 4K
else:
    API_URL = "https://api.laozhang.ai/v1beta/models/gemini-2.5-flash-image:generateContent"
    DEFAULT_IMAGE_SIZE = None  # 稳定版不支持
# ================================================


def encode_image(image_path: str) -> tuple:
    """将图片编码为 base64"""
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    ext = os.path.splitext(image_path)[1].lower()
    mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
    
    return mime_type, image_data


def generate_image(prompt: str, aspect_ratio: str = "1:1", 
                  image_size: str = None, input_images: list = None,
                  output_filename: str = None) -> str:
    """
    生成或编辑图片
    
    参数:
        prompt: 提示词
        aspect_ratio: 纵横比 (21:9, 16:9, 4:3, 3:2, 1:1, 9:16, 3:4, 2:3, 5:4, 4:5)
        image_size: 分辨率 (1K, 2K, 4K)，仅 Nano Banana 2 支持
        input_images: 输入图片路径列表
        output_filename: 自定义输出文件名
    
    返回: 输出文件路径
    """
    print("="*60)
    print("🎨 Gemini 图像处理")
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
            else:
                print(f"⚠️ 图片不存在: {img_path}")
    
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
        if output_filename:
            filename = output_filename
        else:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            size_suffix = f"_{image_size}" if image_size else ""
            filename = f"result{size_suffix}_{timestamp}.png"
        
        with open(filename, "wb") as f:
            f.write(base64.b64decode(image_data))
        
        file_size = os.path.getsize(filename) / 1024
        print(f"✅ 图片已保存: {filename}")
        print(f"📊 文件大小: {file_size:.2f} KB")
        
        return filename
        
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        return None


def text_to_image_example():
    """
    场景1：文生图
    
    生成一张全新的图片
    """
    print("\n" + "="*60)
    print("场景1：文生图")
    print("="*60)
    
    # 可自定义参数
    prompt = "A serene Japanese zen garden with cherry blossoms, koi pond, professional photography"
    aspect_ratio = "16:9"  # 宽屏
    image_size = DEFAULT_IMAGE_SIZE
    
    return generate_image(
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        image_size=image_size,
        output_filename="result_text_to_image.png"
    )


def image_style_transfer_example():
    """
    场景2：图片风格转换
    
    将现有图片转换为特定艺术风格
    """
    print("\n" + "="*60)
    print("场景2：图片风格转换")
    print("="*60)
    
    # 替换为您的图片路径
    input_image = "your_image.jpg"
    
    if not os.path.exists(input_image):
        print(f"⚠️ 图片不存在: {input_image}")
        print("   请将您的图片放在当前目录，并修改 input_image 变量")
        return None
    
    prompt = "Transform this image into Van Gogh's Starry Night style oil painting"
    aspect_ratio = "1:1"
    image_size = DEFAULT_IMAGE_SIZE
    
    return generate_image(
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        image_size=image_size,
        input_images=[input_image],
        output_filename="result_style_transfer.png"
    )


def multi_image_mix_example():
    """
    场景3：多图混合
    
    将多张图片创意合成
    """
    print("\n" + "="*60)
    print("场景3：多图混合")
    print("="*60)
    
    # 替换为您的图片路径
    images = ["image1.jpg", "image2.jpg"]
    
    missing = [img for img in images if not os.path.exists(img)]
    if missing:
        print(f"⚠️ 图片不存在: {missing}")
        print("   请将您的图片放在当前目录，并修改 images 列表")
        return None
    
    prompt = "Combine these images into a creative artistic composition"
    aspect_ratio = "16:9"
    image_size = DEFAULT_IMAGE_SIZE
    
    return generate_image(
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        image_size=image_size,
        input_images=images,
        output_filename="result_multi_mix.png"
    )


def image_4k_example():
    """
    场景4：4K 超高清生成（仅 Nano Banana 2）
    
    生成 4K 超高清图片
    """
    print("\n" + "="*60)
    print("场景4：4K 超高清生成")
    print("="*60)
    
    if not USE_NANO_BANANA_2:
        print("⚠️ 4K 仅 Nano Banana 2 支持")
        print("   请将 USE_NANO_BANANA_2 设置为 True")
        return None
    
    prompt = "A futuristic cyberpunk city at night, neon lights, flying cars, highly detailed, 4k"
    aspect_ratio = "16:9"
    
    return generate_image(
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        image_size="4K",
        output_filename="result_4k.png"
    )


def main():
    """主函数"""
    model_name = "Nano Banana 2 (最新版)" if USE_NANO_BANANA_2 else "Nano Banana (稳定版)"
    
    print("="*60)
    print("Gemini 图像处理 - Google 原生格式")
    print(f"模型: {model_name}")
    print("="*60)
    
    if API_KEY == "sk-YOUR_API_KEY":
        print("\n❌ 请先配置您的 API Key！")
        print("   获取地址: https://api.laozhang.ai/token")
        print("   然后修改脚本顶部的 API_KEY 变量")
        return
    
    print("\n选择要运行的场景：")
    print("1. 文生图（16:9 宽屏）")
    print("2. 图片风格转换")
    print("3. 多图混合")
    print("4. 4K 超高清生成（仅 Nano Banana 2）")
    print("5. 运行全部")
    
    choice = input("\n请输入选择 (1-5): ").strip()
    
    if choice == "1":
        text_to_image_example()
    elif choice == "2":
        image_style_transfer_example()
    elif choice == "3":
        multi_image_mix_example()
    elif choice == "4":
        image_4k_example()
    elif choice == "5":
        text_to_image_example()
        image_style_transfer_example()
        multi_image_mix_example()
        image_4k_example()
    else:
        print("无效选择")
    
    print("\n" + "="*60)
    print("🎉 完成！")
    print("="*60)


if __name__ == "__main__":
    main()

