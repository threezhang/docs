#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veo-3.1 同步视频生成 API 测试脚本

功能：
1. 文生视频测试（使用 chat/completions 接口）
2. 图生视频测试（使用图片URL）

使用方法：
    python veo_sync_demo.py

作者：老张API
文档：https://docs.laozhang.ai/api-capabilities/veo/veo-31-quick-start
"""

import requests
import time
import json
import re
import os
from datetime import datetime

# ==================== 配置区域 ====================

API_KEY = "sk-9SOAt1Bkvcv97WDXE0464d8b0712406f86594f4968524fBd"
BASE_URL = "https://api.laozhang.ai/v1"

# 测试图片URL（可爱猫咪图片）
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
    print(f"   URL: {url}")
    print(f"   Model: {model}")
    print(f"   Prompt: {prompt[:50]}..." if len(prompt) > 50 else f"   Prompt: {prompt}")
    if image_url:
        print(f"   Image: {image_url[:60]}...")
    print(f"   Stream: {stream}")
    
    start_time = time.time()
    
    if stream:
        # 流式响应处理
        response = requests.post(url, headers=headers, json=data, stream=True)
        
        if response.status_code != 200:
            print(f"\n❌ 错误: {response.status_code}")
            print(f"   {response.text}")
            return {"error": response.text, "status_code": response.status_code}
        
        print(f"\n📥 流式响应开始...")
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
        print(f"\n\n⏱️ 总耗时: {elapsed:.1f}秒")
        
        # 提取视频URL
        video_url = extract_video_url(full_content)
        
        return {
            "success": True,
            "content": full_content,
            "video_url": video_url,
            "elapsed": elapsed
        }
    else:
        # 非流式响应
        response = requests.post(url, headers=headers, json=data)
        elapsed = time.time() - start_time
        
        if response.status_code != 200:
            print(f"\n❌ 错误: {response.status_code}")
            return {"error": response.text, "status_code": response.status_code}
        
        result = response.json()
        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        video_url = extract_video_url(content)
        
        print(f"\n📥 响应内容:")
        print(content)
        print(f"\n⏱️ 总耗时: {elapsed:.1f}秒")
        
        return {
            "success": True,
            "content": content,
            "video_url": video_url,
            "elapsed": elapsed
        }


def extract_video_url(text: str) -> str:
    """从文本中提取视频URL"""
    # 匹配常见的视频URL模式
    patterns = [
        r'https://[^\s\)]+\.mp4',
        r'https://[^\s\)]+/assets/[^\s\)]+',
        r'\(https://[^\)]+\)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            url = match.group(0)
            # 清理URL
            url = url.strip('()')
            return url
    
    return None


def download_video(video_url: str, save_path: str) -> bool:
    """下载视频文件"""
    print(f"\n📥 下载视频...")
    print(f"   URL: {video_url[:80]}...")
    
    try:
        response = requests.get(video_url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(save_path, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r   进度: {percent:.1f}%", end="", flush=True)
        
        file_size = os.path.getsize(save_path)
        print(f"\n✅ 视频已保存: {save_path} ({file_size/1024/1024:.2f} MB)")
        return True
        
    except Exception as e:
        print(f"\n❌ 下载失败: {e}")
        return False


# ==================== 测试函数 ====================

def test_text_to_video():
    """测试1: 文生视频"""
    print("\n" + "="*60)
    print("🎬 测试1: 同步文生视频 (Text-to-Video)")
    print("="*60)
    
    prompt = "一只毛茸茸的橘色小猫在阳光下打哈欠，然后慢慢闭上眼睛睡着了"
    model = "veo-3.1-fast"  # 竖屏快速版
    
    print(f"\n📝 测试参数:")
    print(f"   提示词: {prompt}")
    print(f"   模型: {model} (竖屏快速版, $0.15/次)")
    
    result = generate_video_sync(prompt, model)
    
    if result.get("error"):
        print(f"\n❌ 测试失败!")
        return None
    
    video_url = result.get("video_url")
    if video_url:
        print(f"\n🎉 视频URL: {video_url}")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_video(video_url, f"sync_text_to_video_{timestamp}.mp4")
    else:
        print("\n⚠️ 未能提取视频URL")
    
    # 保存结果
    result["test_type"] = "text_to_video"
    result["prompt"] = prompt
    result["model"] = model
    result["timestamp"] = datetime.now().isoformat()
    
    with open(f"result_sync_t2v_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    return result


def test_image_to_video():
    """测试2: 图生视频"""
    print("\n" + "="*60)
    print("🖼️ 测试2: 同步图生视频 (Image-to-Video)")
    print("="*60)
    
    prompt = "让这只猫咪慢慢转过头来，好奇地看着镜头，眨眨眼睛"
    model = "veo-3.1-fast-fl"  # 竖屏快速版 + 支持图生视频
    
    print(f"\n📝 测试参数:")
    print(f"   提示词: {prompt}")
    print(f"   模型: {model} (竖屏快速版+图生视频, $0.15/次)")
    print(f"   图片: {TEST_IMAGE_URL[:60]}...")
    
    result = generate_video_sync(prompt, model, image_url=TEST_IMAGE_URL)
    
    if result.get("error"):
        print(f"\n❌ 测试失败!")
        return None
    
    video_url = result.get("video_url")
    if video_url:
        print(f"\n🎉 视频URL: {video_url}")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_video(video_url, f"sync_image_to_video_{timestamp}.mp4")
    else:
        print("\n⚠️ 未能提取视频URL")
    
    # 保存结果
    result["test_type"] = "image_to_video"
    result["prompt"] = prompt
    result["model"] = model
    result["image_url"] = TEST_IMAGE_URL
    result["timestamp"] = datetime.now().isoformat()
    
    with open(f"result_sync_i2v_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    return result


# ==================== 主程序 ====================

def main():
    """主函数"""
    print("\n" + "="*60)
    print("🚀 Veo-3.1 同步 API 测试")
    print("="*60)
    print(f"\n⚙️ 配置:")
    print(f"   API Base URL: {BASE_URL}")
    print(f"   API Key: {API_KEY[:10]}...{API_KEY[-4:]}")
    print(f"   接口: /v1/chat/completions (OpenAI 兼容)")
    
    results = []
    
    # 测试1: 文生视频
    print("\n\n" + "🔹"*30)
    result1 = test_text_to_video()
    if result1:
        results.append(result1)
    
    # 测试2: 图生视频
    print("\n\n" + "🔹"*30)
    result2 = test_image_to_video()
    if result2:
        results.append(result2)
    
    # 总结
    print("\n\n" + "="*60)
    print("📊 测试总结")
    print("="*60)
    
    for i, r in enumerate(results, 1):
        test_type = r.get("test_type", "unknown")
        video_url = r.get("video_url")
        elapsed = r.get("elapsed", 0)
        status = "✅ 成功" if video_url else "⚠️ 无视频URL"
        print(f"\n   测试{i} ({test_type}): {status}")
        print(f"      耗时: {elapsed:.1f}秒")
        if video_url:
            print(f"      视频: {video_url[:60]}...")
    
    print("\n" + "="*60)
    print("🎉 测试完成!")
    print("="*60)


if __name__ == "__main__":
    main()

