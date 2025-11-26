#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 多图创作 API 测试脚本

功能：
1. 单图编辑
2. 多图合成/融合
3. 支持 Nano Banana 和 Nano Banana 2

使用方法：
    python gemini_multi_image_demo.py

作者：老张API
文档：https://docs.laozhang.ai/api-capabilities/gemini-flash-image-edit
"""

import requests
import base64
import re
import os
from datetime import datetime

# ==================== 配置区域 ====================

API_KEY = "sk-9SOAt1Bkvcv97WDXE0464d8b0712406f86594f4968524fBd"
BASE_URL = "https://api.laozhang.ai/v1"

# 测试图片
TEST_IMAGE_1 = "test_sunset.jpg"   # 海滩日落
TEST_IMAGE_2 = "test_mountain.jpg" # 山脉

# ==================== 核心函数 ====================

def edit_image_openai_format(prompt: str, image_urls: list, model: str = "gemini-3-pro-image-preview") -> dict:
    """
    使用 OpenAI 兼容格式编辑/合成图片
    
    Args:
        prompt: 编辑描述
        image_urls: 图片URL列表（支持本地base64或远程URL）
        model: 模型名称
        
    Returns:
        dict: 结果
    """
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 构建消息内容
    content = [{"type": "text", "text": prompt}]
    
    for img_url in image_urls:
        content.append({
            "type": "image_url",
            "image_url": {"url": img_url}
        })
    
    data = {
        "model": model,
        "stream": False,
        "messages": [{
            "role": "user",
            "content": content
        }]
    }
    
    print(f"\n📤 发送请求:")
    print(f"   Model: {model}")
    print(f"   Prompt: {prompt[:60]}...")
    print(f"   Images: {len(image_urls)} 张")
    
    response = requests.post(url, headers=headers, json=data, timeout=120)
    
    if response.status_code != 200:
        print(f"\n❌ 错误: {response.status_code}")
        print(f"   {response.text[:200]}")
        return {"error": response.text}
    
    result = response.json()
    content_text = result.get("choices", [{}])[0].get("message", {}).get("content", "")
    
    return {
        "success": True,
        "content": content_text,
        "usage": result.get("usage", {})
    }


def extract_and_save_image(content: str, filename: str) -> bool:
    """从响应内容中提取并保存图片"""
    # 尝试多种匹配模式
    patterns = [
        r'!\[.*?\]\(data:image/[^;]+;base64,([^)]+)\)',  # markdown格式
        r'data:image/[^;]+;base64,([^\s"\')\]]+)',       # 通用base64
    ]
    
    base64_data = None
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            base64_data = match.group(1)
            break
    
    if base64_data:
        try:
            # 清理 base64 数据
            base64_data = base64_data.strip()
            # 修复 padding
            padding = 4 - len(base64_data) % 4
            if padding != 4:
                base64_data += '=' * padding
            
            image_data = base64.b64decode(base64_data)
            
            with open(filename, 'wb') as f:
                f.write(image_data)
            
            file_size = os.path.getsize(filename)
            print(f"✅ 已保存: {filename} ({file_size/1024:.1f} KB)")
            return True
        except Exception as e:
            print(f"❌ 保存失败: {e}")
            return False
    else:
        print("⚠️ 未找到图片数据")
        return False


def image_to_base64_url(image_path: str) -> str:
    """将本地图片转换为 base64 data URL"""
    with open(image_path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    
    # 检测图片类型
    ext = os.path.splitext(image_path)[1].lower()
    mime_types = {'.jpg': 'jpeg', '.jpeg': 'jpeg', '.png': 'png', '.webp': 'webp'}
    mime = mime_types.get(ext, 'jpeg')
    
    return f"data:image/{mime};base64,{data}"


# ==================== 测试函数 ====================

def test_single_image_edit():
    """测试1: 单图编辑"""
    print("\n" + "="*60)
    print("🎨 测试1: 单图编辑")
    print("="*60)
    
    if not os.path.exists(TEST_IMAGE_1):
        print(f"❌ 图片不存在: {TEST_IMAGE_1}")
        return None
    
    prompt = "Add a colorful hot air balloon floating in the sky above the ocean, make it look magical and dreamy"
    image_url = image_to_base64_url(TEST_IMAGE_1)
    
    print(f"📷 输入图片: {TEST_IMAGE_1}")
    print(f"📝 编辑指令: {prompt}")
    
    result = edit_image_openai_format(prompt, [image_url], model="gemini-3-pro-image-preview")
    
    if result.get("error"):
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"result_single_edit_{timestamp}.png"
    extract_and_save_image(result["content"], filename)
    
    return result


def test_multi_image_merge():
    """测试2: 多图融合"""
    print("\n" + "="*60)
    print("🖼️ 测试2: 多图融合")
    print("="*60)
    
    if not os.path.exists(TEST_IMAGE_1) or not os.path.exists(TEST_IMAGE_2):
        print(f"❌ 图片不存在")
        return None
    
    prompt = "Merge these two images into one beautiful panoramic artwork: combine the ocean sunset with the mountain peaks, creating a magical landscape where the sea meets the mountains under a golden sky"
    
    image_urls = [
        image_to_base64_url(TEST_IMAGE_1),  # 海滩日落
        image_to_base64_url(TEST_IMAGE_2)   # 山脉
    ]
    
    print(f"📷 输入图片: {TEST_IMAGE_1}, {TEST_IMAGE_2}")
    print(f"📝 融合指令: {prompt[:80]}...")
    
    result = edit_image_openai_format(prompt, image_urls, model="gemini-3-pro-image-preview")
    
    if result.get("error"):
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"result_multi_merge_{timestamp}.png"
    extract_and_save_image(result["content"], filename)
    
    return result


def test_style_transfer():
    """测试3: 风格迁移"""
    print("\n" + "="*60)
    print("🎭 测试3: 风格迁移")
    print("="*60)
    
    if not os.path.exists(TEST_IMAGE_1):
        print(f"❌ 图片不存在: {TEST_IMAGE_1}")
        return None
    
    prompt = "Transform this sunset beach scene into a Japanese ukiyo-e woodblock print style, with bold outlines and traditional color palette"
    image_url = image_to_base64_url(TEST_IMAGE_1)
    
    print(f"📷 输入图片: {TEST_IMAGE_1}")
    print(f"📝 风格指令: {prompt[:60]}...")
    
    result = edit_image_openai_format(prompt, [image_url], model="gemini-3-pro-image-preview")
    
    if result.get("error"):
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"result_style_transfer_{timestamp}.png"
    extract_and_save_image(result["content"], filename)
    
    return result


# ==================== 主程序 ====================

def main():
    print("\n" + "="*60)
    print("🚀 Gemini 多图创作 API 测试")
    print("="*60)
    print(f"\n📖 文档: https://docs.laozhang.ai/api-capabilities/gemini-flash-image-edit")
    print(f"💰 价格: Nano Banana 2 $0.05/次")
    
    results = []
    
    # 测试1: 单图编辑
    r1 = test_single_image_edit()
    if r1:
        results.append(("单图编辑", r1))
    
    # 测试2: 多图融合
    r2 = test_multi_image_merge()
    if r2:
        results.append(("多图融合", r2))
    
    # 测试3: 风格迁移
    r3 = test_style_transfer()
    if r3:
        results.append(("风格迁移", r3))
    
    # 总结
    print("\n\n" + "="*60)
    print("📊 测试总结")
    print("="*60)
    
    for name, r in results:
        status = "✅ 成功" if r.get("success") else "❌ 失败"
        print(f"\n   {name}: {status}")
    
    print("\n" + "="*60)
    print("🎉 测试完成!")
    print("="*60)


if __name__ == "__main__":
    main()

