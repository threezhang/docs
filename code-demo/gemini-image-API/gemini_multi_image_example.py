#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 多图创作 API 示例

功能：
1. 单图编辑 - 添加元素、修改内容
2. 多图合成 - 将多张图片融合为一张
3. 风格迁移 - 转换图片风格

支持模型：
- gemini-3-pro-image-preview (Nano Banana 2) - $0.05/次，支持2K/4K
- gemini-2.5-flash-image (Nano Banana) - $0.025/次，稳定版

使用方法：
    1. 替换 API_KEY 为您的密钥
    2. 准备测试图片（或使用提供的下载命令）
    3. 运行: python gemini_multi_image_example.py

获取密钥：https://api.laozhang.ai/token
文档：https://docs.laozhang.ai/api-capabilities/gemini-flash-image-edit
"""

import requests
import base64
import re
import os
from datetime import datetime

# ==================== 配置区域 ====================

# ⚠️ 请替换为您的 API Key
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

BASE_URL = "https://api.laozhang.ai/v1"

# 测试图片（请先下载或替换为您的图片）
# 下载命令：
# curl -o test_sunset.jpg "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800"
# curl -o test_mountain.jpg "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800"
TEST_IMAGE_1 = "test_sunset.jpg"
TEST_IMAGE_2 = "test_mountain.jpg"

# ==================== 核心函数 ====================

def image_to_base64_url(image_path: str) -> str:
    """将本地图片转换为 base64 data URL"""
    with open(image_path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    
    ext = os.path.splitext(image_path)[1].lower()
    mime_types = {'.jpg': 'jpeg', '.jpeg': 'jpeg', '.png': 'png', '.webp': 'webp'}
    mime = mime_types.get(ext, 'jpeg')
    
    return f"data:image/{mime};base64,{data}"


def edit_images(prompt: str, image_paths: list, model: str = "gemini-3-pro-image-preview") -> dict:
    """
    编辑/合成图片
    
    Args:
        prompt: 编辑描述
        image_paths: 本地图片路径列表
        model: 模型名称
        
    Returns:
        dict: 包含结果的字典
    """
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 构建消息内容
    content = [{"type": "text", "text": prompt}]
    
    for img_path in image_paths:
        if not os.path.exists(img_path):
            return {"error": f"图片不存在: {img_path}"}
        content.append({
            "type": "image_url",
            "image_url": {"url": image_to_base64_url(img_path)}
        })
    
    data = {
        "model": model,
        "stream": False,
        "messages": [{"role": "user", "content": content}]
    }
    
    print(f"\n📤 发送请求:")
    print(f"   Model: {model}")
    print(f"   Images: {len(image_paths)} 张")
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=120)
        
        if response.status_code != 200:
            return {"error": f"API错误: {response.status_code}"}
        
        result = response.json()
        content_text = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        
        return {"success": True, "content": content_text}
        
    except Exception as e:
        return {"error": str(e)}


def save_result_image(content: str, filename: str) -> bool:
    """从响应中提取并保存图片"""
    patterns = [
        r'!\[.*?\]\(data:image/[^;]+;base64,([^)]+)\)',
        r'data:image/[^;]+;base64,([^\s"\')\]]+)',
    ]
    
    base64_data = None
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            base64_data = match.group(1)
            break
    
    if base64_data:
        try:
            base64_data = base64_data.strip()
            padding = 4 - len(base64_data) % 4
            if padding != 4:
                base64_data += '=' * padding
            
            image_data = base64.b64decode(base64_data)
            with open(filename, 'wb') as f:
                f.write(image_data)
            print(f"✅ 已保存: {filename} ({os.path.getsize(filename)/1024:.1f} KB)")
            return True
        except Exception as e:
            print(f"❌ 保存失败: {e}")
    else:
        print("⚠️ 未找到图片数据")
    return False


# ==================== 使用示例 ====================

def example_single_edit():
    """示例1: 单图编辑"""
    print("\n" + "="*60)
    print("🎨 示例1: 单图编辑 - 添加元素")
    print("="*60)
    
    result = edit_images(
        prompt="Add a beautiful rainbow in the sky",
        image_paths=[TEST_IMAGE_1],
        model="gemini-3-pro-image-preview"
    )
    
    if result.get("success"):
        save_result_image(result["content"], f"output_edit_{datetime.now().strftime('%H%M%S')}.png")
    else:
        print(f"❌ 失败: {result.get('error')}")


def example_multi_merge():
    """示例2: 多图融合"""
    print("\n" + "="*60)
    print("🖼️ 示例2: 多图融合")
    print("="*60)
    
    result = edit_images(
        prompt="Merge these two images: create a scene where the ocean meets the mountains",
        image_paths=[TEST_IMAGE_1, TEST_IMAGE_2],
        model="gemini-3-pro-image-preview"
    )
    
    if result.get("success"):
        save_result_image(result["content"], f"output_merge_{datetime.now().strftime('%H%M%S')}.png")
    else:
        print(f"❌ 失败: {result.get('error')}")


def example_style_transfer():
    """示例3: 风格迁移"""
    print("\n" + "="*60)
    print("🎭 示例3: 风格迁移")
    print("="*60)
    
    result = edit_images(
        prompt="Transform this into a watercolor painting style",
        image_paths=[TEST_IMAGE_1],
        model="gemini-3-pro-image-preview"
    )
    
    if result.get("success"):
        save_result_image(result["content"], f"output_style_{datetime.now().strftime('%H%M%S')}.png")
    else:
        print(f"❌ 失败: {result.get('error')}")


# ==================== 主程序 ====================

def main():
    print("\n" + "="*60)
    print("🚀 Gemini 多图创作示例")
    print("="*60)
    print("\n📖 文档: https://docs.laozhang.ai/api-capabilities/gemini-flash-image-edit")
    print("💰 价格: Nano Banana 2 $0.05/次 | Nano Banana $0.025/次")
    
    if API_KEY.startswith("sk-xxxx"):
        print("\n⚠️ 请先设置您的 API Key!")
        print("   编辑本文件，替换 API_KEY 变量的值")
        print("   获取密钥: https://api.laozhang.ai/token")
        print("\n📷 准备测试图片:")
        print('   curl -o test_sunset.jpg "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800"')
        print('   curl -o test_mountain.jpg "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800"')
        return
    
    # 检查测试图片
    if not os.path.exists(TEST_IMAGE_1):
        print(f"\n⚠️ 请先下载测试图片:")
        print(f'   curl -o {TEST_IMAGE_1} "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800"')
        print(f'   curl -o {TEST_IMAGE_2} "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800"')
        return
    
    # 运行示例
    example_single_edit()
    example_multi_merge()
    example_style_transfer()
    
    print("\n" + "="*60)
    print("🎉 示例完成!")
    print("="*60)


if __name__ == "__main__":
    main()

