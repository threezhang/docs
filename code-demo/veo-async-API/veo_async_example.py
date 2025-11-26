#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veo-3.1 异步视频生成 API 示例

功能：
1. 文生视频（Text-to-Video）
2. 图生视频（Image-to-Video）- 需要上传本地图片

使用方法：
    1. 替换 API_KEY 为您的密钥
    2. 运行: python veo_async_example.py

获取密钥：https://api.laozhang.ai/token
文档：https://docs.laozhang.ai/api-capabilities/veo/veo-31-async-api
"""

import requests
import time
import json
import os
from datetime import datetime

# ==================== 配置区域 ====================

# ⚠️ 请替换为您的 API Key
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

BASE_URL = "https://api.laozhang.ai/v1"

# ==================== 核心函数 ====================

def create_video_task(prompt: str, model: str = "veo-3.1-fast", 
                      image_path: str = None) -> dict:
    """
    创建视频生成任务
    
    Args:
        prompt: 视频描述提示词
        model: 模型名称
        image_path: 可选，本地图片路径（用于图生视频）
        
    Returns:
        dict: 任务信息
    """
    url = f"{BASE_URL}/videos"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    print(f"\n📤 创建任务:")
    print(f"   Model: {model}")
    print(f"   Prompt: {prompt[:50]}..." if len(prompt) > 50 else f"   Prompt: {prompt}")
    
    if image_path:
        # 图生视频：使用 multipart/form-data 上传图片
        print(f"   Image: {image_path}")
        
        if not os.path.exists(image_path):
            return {"error": f"图片文件不存在: {image_path}"}
        
        with open(image_path, 'rb') as f:
            files = {"input_reference": (os.path.basename(image_path), f, "image/jpeg")}
            data = {"model": model, "prompt": prompt}
            response = requests.post(url, headers=headers, files=files, data=data)
    else:
        # 文生视频：使用 JSON 格式
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers, json={"model": model, "prompt": prompt})
    
    if response.status_code != 200:
        print(f"\n❌ 错误: {response.status_code}")
        print(f"   {response.text}")
        return {"error": response.text}
    
    result = response.json()
    print(f"✅ 任务创建成功! ID: {result.get('id')}")
    return result


def wait_for_video(video_id: str, poll_interval: int = 5, timeout: int = 600) -> dict:
    """
    等待视频生成完成
    
    Args:
        video_id: 任务ID
        poll_interval: 轮询间隔（秒）
        timeout: 超时时间（秒）
        
    Returns:
        dict: 完成的任务信息
    """
    url = f"{BASE_URL}/videos/{video_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    print(f"\n⏳ 等待生成...")
    start_time = time.time()
    last_status = ""
    
    while True:
        elapsed = time.time() - start_time
        
        if elapsed > timeout:
            return {"error": "timeout"}
        
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return {"error": response.text}
        
        task = response.json()
        status = task.get("status", "unknown")
        progress = task.get("progress", 0)
        
        if status != last_status:
            print(f"   [{int(elapsed)}s] 状态: {status}, 进度: {progress}%")
            last_status = status
        
        if status == "completed":
            print(f"\n✅ 生成完成! 耗时: {int(elapsed)}秒")
            return task
        elif status == "failed":
            print(f"\n❌ 生成失败!")
            return task
        
        time.sleep(poll_interval)


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
    print("🎬 测试: 异步文生视频 (Text-to-Video)")
    print("="*60)
    
    prompt = "日落时分，金色阳光洒在平静的海面上，海鸥在空中翱翔"
    model = "veo-3.1-fast"  # 竖屏快速版 $0.15/次
    
    # 1. 创建任务
    task = create_video_task(prompt, model)
    if "error" in task:
        return None
    
    video_id = task.get("id")
    
    # 2. 等待完成
    completed = wait_for_video(video_id)
    if "error" in completed:
        return None
    
    # 3. 获取视频URL并下载
    video_url = completed.get("video_url") or completed.get("url")
    if video_url:
        print(f"\n🎉 视频URL: {video_url}")
        download_video(video_url, f"async_t2v_{datetime.now().strftime('%H%M%S')}.mp4")
    
    return completed


def test_image_to_video():
    """测试: 图生视频（需要本地图片）"""
    print("\n" + "="*60)
    print("🖼️ 测试: 异步图生视频 (Image-to-Video)")
    print("="*60)
    
    # 检查是否有测试图片
    test_image = "test_image.jpg"
    
    if not os.path.exists(test_image):
        print(f"\n⚠️ 请先准备测试图片: {test_image}")
        print("   异步API图生视频需要上传本地图片文件")
        print("\n   您可以运行以下命令下载测试图片:")
        print(f'   curl -o {test_image} "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800"')
        return None
    
    prompt = "让这只猫咪慢慢眨眼睛，然后转头看向镜头"
    model = "veo-3.1-fast-fl"  # 竖屏快速版+图生视频 $0.15/次
    
    # 1. 创建任务（上传图片）
    task = create_video_task(prompt, model, image_path=test_image)
    if "error" in task:
        return None
    
    video_id = task.get("id")
    
    # 2. 等待完成
    completed = wait_for_video(video_id)
    if "error" in completed:
        return None
    
    # 3. 获取视频URL并下载
    video_url = completed.get("video_url") or completed.get("url")
    if video_url:
        print(f"\n🎉 视频URL: {video_url}")
        download_video(video_url, f"async_i2v_{datetime.now().strftime('%H%M%S')}.mp4")
    
    return completed


# ==================== 主程序 ====================

def main():
    print("\n" + "="*60)
    print("🚀 Veo-3.1 异步 API 示例")
    print("="*60)
    print(f"\n📖 文档: https://docs.laozhang.ai/api-capabilities/veo/veo-31-async-api")
    print("\n💡 异步API优势: 更稳定 | 失败不扣费 | 支持批量处理")
    
    if API_KEY.startswith("sk-xxxx"):
        print("\n⚠️ 请先设置您的 API Key!")
        print("   编辑本文件，替换 API_KEY 变量的值")
        print("   获取密钥: https://api.laozhang.ai/token")
        return
    
    # 测试文生视频
    test_text_to_video()
    
    # 测试图生视频（需要本地图片）
    test_image_to_video()
    
    print("\n" + "="*60)
    print("🎉 测试完成!")
    print("="*60)


if __name__ == "__main__":
    main()

