#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veo-3.1 同步视频生成 API 示例

功能：
1. 文生视频（Text-to-Video）
2. 图生视频（Image-to-Video）

使用方法：
    1. 替换 API_KEY 为您的密钥
    2. 运行: python veo_sync_example.py

获取密钥：https://api.laozhang.ai/token
文档：https://docs.laozhang.ai/api-capabilities/veo/veo-31-quick-start
"""

import requests
import time
import json
import re
import os
from datetime import datetime

# ==================== 配置区域 ====================

# ⚠️ 请替换为您的 API Key
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

BASE_URL = "https://api.laozhang.ai/v1"

# 测试图片URL（用于图生视频）
TEST_IMAGE_URL = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800"

# ==================== 核心函数 ====================

def generate_video_sync(prompt: str, model: str = "veo-3.1-fast", 
                        image_url: str = None, stream: bool = True) -> dict:
    """
    同步方式生成视频（使用 chat/completions 接口）
    
    Args:
        prompt: 视频描述提示词
        model: 模型名称
        image_url: 可选，图片URL（用于图生视频）
        stream: 是否使用流式响应
        
    Returns:
        dict: 生成结果
    """
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 构建消息内容
    content = [{"type": "text", "text": prompt}]
    
    # 如果有图片URL，添加到内容中
    if image_url:
        content.append({
            "type": "image_url",
            "image_url": {"url": image_url}
        })
    
    data = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": content
        }],
        "stream": stream
    }
    
    print(f"\n📤 发送请求:")
    print(f"   Model: {model}")
    print(f"   Prompt: {prompt[:50]}..." if len(prompt) > 50 else f"   Prompt: {prompt}")
    if image_url:
        print(f"   Image: {image_url[:60]}...")
    
    start_time = time.time()
    
    # 流式响应处理
    response = requests.post(url, headers=headers, json=data, stream=True)
    
    if response.status_code != 200:
        print(f"\n❌ 错误: {response.status_code}")
        print(f"   {response.text}")
        return {"error": response.text, "status_code": response.status_code}
    
    print(f"\n📥 生成中...")
    full_content = ""
    
    for line in response.iter_lines():
        if line:
            line_text = line.decode('utf-8')
            if line_text.startswith("data: "):
                data_str = line_text[6:]
                if data_str == "[DONE]":
                    break
                try:
                    chunk = json.loads(data_str)
                    delta = chunk.get("choices", [{}])[0].get("delta", {})
                    content_piece = delta.get("content", "")
                    if content_piece:
                        print(content_piece, end="", flush=True)
                        full_content += content_piece
                except json.JSONDecodeError:
                    pass
    
    elapsed = time.time() - start_time
    print(f"\n\n⏱️ 耗时: {elapsed:.1f}秒")
    
    # 提取视频URL
    video_url = extract_video_url(full_content)
    
    return {
        "success": True,
        "content": full_content,
        "video_url": video_url,
        "elapsed": elapsed
    }


def extract_video_url(text: str) -> str:
    """从文本中提取视频URL"""
    patterns = [
        r'https://[^\s\)]+\.mp4',
        r'https://[^\s\)]+/assets/[^\s\)]+',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(0).strip('()')
    return None


def download_video(video_url: str, save_path: str) -> bool:
    """下载视频文件"""
    print(f"\n📥 下载视频...")
    
    try:
        response = requests.get(video_url, stream=True)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        file_size = os.path.getsize(save_path)
        print(f"✅ 已保存: {save_path} ({file_size/1024/1024:.2f} MB)")
        return True
        
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        return False


# ==================== 测试函数 ====================

def test_text_to_video():
    """测试: 文生视频"""
    print("\n" + "="*60)
    print("🎬 测试: 文生视频 (Text-to-Video)")
    print("="*60)
    
    prompt = "一只毛茸茸的橘色小猫在阳光下打哈欠"
    model = "veo-3.1-fast"  # 竖屏快速版 $0.15/次
    
    result = generate_video_sync(prompt, model)
    
    if result.get("video_url"):
        print(f"\n🎉 视频URL: {result['video_url']}")
        download_video(result["video_url"], f"text_to_video_{datetime.now().strftime('%H%M%S')}.mp4")
    
    return result


def test_image_to_video():
    """测试: 图生视频"""
    print("\n" + "="*60)
    print("🖼️ 测试: 图生视频 (Image-to-Video)")
    print("="*60)
    
    prompt = "让这只猫咪慢慢眨眼睛"
    model = "veo-3.1-fast-fl"  # 竖屏快速版+图生视频 $0.15/次
    
    result = generate_video_sync(prompt, model, image_url=TEST_IMAGE_URL)
    
    if result.get("video_url"):
        print(f"\n🎉 视频URL: {result['video_url']}")
        download_video(result["video_url"], f"image_to_video_{datetime.now().strftime('%H%M%S')}.mp4")
    
    return result


# ==================== 主程序 ====================

def main():
    print("\n" + "="*60)
    print("🚀 Veo-3.1 同步 API 示例")
    print("="*60)
    print(f"\n📖 文档: https://docs.laozhang.ai/api-capabilities/veo/veo-31-quick-start")
    
    if API_KEY.startswith("sk-xxxx"):
        print("\n⚠️ 请先设置您的 API Key!")
        print("   编辑本文件，替换 API_KEY 变量的值")
        print("   获取密钥: https://api.laozhang.ai/token")
        return
    
    # 测试文生视频
    test_text_to_video()
    
    # 测试图生视频
    test_image_to_video()
    
    print("\n" + "="*60)
    print("🎉 测试完成!")
    print("="*60)


if __name__ == "__main__":
    main()


