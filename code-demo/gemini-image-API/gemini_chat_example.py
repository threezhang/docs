#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 图像编辑 - OpenAI Chat 兼容格式（用户示例版）
模型：gemini-3-pro-image-preview（最新版）/ gemini-2.5-flash-image（稳定版）

特点：
- 完美兼容 OpenAI SDK
- 支持图片 URL 和 Base64 两种输入方式
- 使用简单，无需了解 Google 原生 API

使用方法：
1. 安装依赖：pip install openai requests
2. 在下方配置区填入您的 API Key
3. 运行：python3 gemini_chat_example.py

获取 API Key：https://api.laozhang.ai/token
"""

import base64
import re
import os
from openai import OpenAI

# ========== 配置区（请填入您的 API Key）==========
API_KEY = "sk-YOUR_API_KEY"  # 替换为您的 API Key
BASE_URL = "https://api.laozhang.ai/v1"

# 模型选择
MODEL = "gemini-3-pro-image-preview"  # 最新版，支持更高质量
# MODEL = "gemini-2.5-flash-image"    # 稳定版，价格更低（$0.025 vs $0.05）
# ================================================


def extract_and_save_image(content: str, filename: str) -> bool:
    """从响应内容中提取 base64 图片并保存"""
    # 匹配 markdown 格式的 base64 图片
    match = re.search(r'!\[.*?\]\((data:image/\w+;base64,([^)]+))\)', content)
    if match:
        base64_data = match.group(2)
        # 确保 base64 填充正确
        padding = 4 - len(base64_data) % 4
        if padding != 4:
            base64_data += '=' * padding
        image_data = base64.b64decode(base64_data)
        with open(filename, 'wb') as f:
            f.write(image_data)
        return True
    return False


def single_image_edit_url():
    """
    场景1：单图编辑 - 使用 URL 输入
    
    适用于：网络图片编辑、在线图片处理
    """
    print("\n" + "="*60)
    print("场景1：单图编辑（URL 输入）")
    print("="*60)
    
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    
    # 使用网络图片 URL（替换为您的图片 URL）
    image_url = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80"
    prompt = "给这只猫戴上一顶红色的圣诞帽"
    
    print(f"📝 提示词: {prompt}")
    print(f"🖼️  图片: {image_url[:50]}...")
    print("📡 发送请求...")
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": image_url}}
                    ]
                }
            ]
        )
        
        content = response.choices[0].message.content
        output_file = "result_single_edit_url.png"
        
        if extract_and_save_image(content, output_file):
            print(f"✅ 成功！图片已保存: {output_file}")
            return True
        else:
            print(f"⚠️ 未找到图片数据")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        return False


def single_image_edit_base64():
    """
    场景2：单图编辑 - 使用本地文件（Base64）
    
    适用于：本地图片处理、风格转换
    """
    print("\n" + "="*60)
    print("场景2：单图编辑（Base64 输入）")
    print("="*60)
    
    # 替换为您的本地图片路径
    test_image = "your_image.jpg"
    
    if not os.path.exists(test_image):
        print(f"⚠️ 图片不存在: {test_image}")
        print("   请将您的图片放在当前目录，并修改 test_image 变量")
        return False
    
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    
    # 读取本地图片并转换为 base64
    with open(test_image, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    prompt = "将这张图片转换为梵高星空风格的油画"
    
    print(f"📝 提示词: {prompt}")
    print(f"🖼️  图片: {test_image}")
    print("📡 发送请求...")
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_b64}"
                            }
                        }
                    ]
                }
            ]
        )
        
        content = response.choices[0].message.content
        output_file = "result_style_transfer.png"
        
        if extract_and_save_image(content, output_file):
            print(f"✅ 成功！图片已保存: {output_file}")
            return True
        else:
            print(f"⚠️ 未找到图片数据")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        return False


def multi_image_merge():
    """
    场景3：多图合成
    
    适用于：创意合成、场景融合
    """
    print("\n" + "="*60)
    print("场景3：多图合成")
    print("="*60)
    
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    
    # 使用两张网络图片（可替换为您的图片）
    image1_url = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80"  # 猫
    image2_url = "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=800&q=80"  # 苹果
    prompt = "将这两张图片创意合成：一只猫在玩苹果"
    
    print(f"📝 提示词: {prompt}")
    print(f"🖼️  图片1: 猫")
    print(f"🖼️  图片2: 苹果")
    print("📡 发送请求...")
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": image1_url}},
                        {"type": "image_url", "image_url": {"url": image2_url}}
                    ]
                }
            ]
        )
        
        content = response.choices[0].message.content
        output_file = "result_multi_merge.png"
        
        if extract_and_save_image(content, output_file):
            print(f"✅ 成功！图片已保存: {output_file}")
            return True
        else:
            print(f"⚠️ 未找到图片数据")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        return False


def main():
    """主函数"""
    print("="*60)
    print("Gemini 图像编辑 - OpenAI Chat 兼容格式")
    print(f"模型: {MODEL}")
    print("="*60)
    
    if API_KEY == "sk-YOUR_API_KEY":
        print("\n❌ 请先配置您的 API Key！")
        print("   获取地址: https://api.laozhang.ai/token")
        print("   然后修改脚本顶部的 API_KEY 变量")
        return
    
    print("\n选择要运行的场景：")
    print("1. 单图编辑（URL 输入）")
    print("2. 单图编辑（本地文件）")
    print("3. 多图合成")
    print("4. 运行全部")
    
    choice = input("\n请输入选择 (1-4): ").strip()
    
    if choice == "1":
        single_image_edit_url()
    elif choice == "2":
        single_image_edit_base64()
    elif choice == "3":
        multi_image_merge()
    elif choice == "4":
        single_image_edit_url()
        single_image_edit_base64()
        multi_image_merge()
    else:
        print("无效选择")
    
    print("\n" + "="*60)
    print("🎉 完成！")
    print("="*60)


if __name__ == "__main__":
    main()

