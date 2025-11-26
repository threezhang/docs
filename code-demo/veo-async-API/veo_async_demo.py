#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veo-3.1 异步视频生成 API 测试脚本

功能：
1. 文生视频测试
2. 图生视频测试（使用图片URL）

使用方法：
    python veo_async_demo.py

作者：老张API
文档：https://docs.laozhang.ai/api-capabilities/veo/veo-31-async-api
"""

import requests
import time
import json
import os
from datetime import datetime

# ==================== 配置区域 ====================

API_KEY = "sk-9SOAt1Bkvcv97WDXE0464d8b0712406f86594f4968524fBd"
BASE_URL = "https://api.laozhang.ai/v1"

# 测试图片URL（用于图生视频测试）
TEST_IMAGE_URL = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800"

# ==================== 核心函数 ====================

def create_video_task(prompt: str, model: str = "veo-3.1") -> dict:
    """
    创建视频生成任务
    
    Args:
        prompt: 视频描述提示词
        model: 模型名称，默认 veo-3.1
        
    Returns:
        dict: 包含任务ID等信息的响应
    """
    url = f"{BASE_URL}/videos"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt
    }
    
    print(f"\n📤 创建任务请求:")
    print(f"   URL: {url}")
    print(f"   Model: {model}")
    print(f"   Prompt: {prompt[:50]}..." if len(prompt) > 50 else f"   Prompt: {prompt}")
    
    response = requests.post(url, headers=headers, json=data)
    
    print(f"\n📥 响应状态: {response.status_code}")
    
    if response.status_code != 200:
        print(f"❌ 错误响应: {response.text}")
        return {"error": response.text, "status_code": response.status_code}
    
    result = response.json()
    print(f"✅ 任务创建成功!")
    print(f"   任务ID: {result.get('id', 'N/A')}")
    print(f"   状态: {result.get('status', 'N/A')}")
    
    return result


def query_task_status(video_id: str) -> dict:
    """
    查询任务状态
    
    Args:
        video_id: 视频任务ID
        
    Returns:
        dict: 任务状态信息
    """
    url = f"{BASE_URL}/videos/{video_id}"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": response.text, "status_code": response.status_code}
    
    return response.json()


def get_video_content(video_id: str) -> dict:
    """
    获取视频内容
    
    Args:
        video_id: 视频任务ID
        
    Returns:
        dict: 包含视频URL的响应
    """
    url = f"{BASE_URL}/videos/{video_id}/content"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": response.text, "status_code": response.status_code}
    
    return response.json()


def wait_for_video(video_id: str, poll_interval: int = 5, timeout: int = 600) -> dict:
    """
    等待视频生成完成
    
    Args:
        video_id: 视频任务ID
        poll_interval: 轮询间隔（秒）
        timeout: 超时时间（秒）
        
    Returns:
        dict: 完成的任务信息（包含 video_url）
    """
    start_time = time.time()
    last_status = ""
    
    print(f"\n⏳ 等待视频生成...")
    print(f"   轮询间隔: {poll_interval}秒")
    print(f"   超时时间: {timeout}秒")
    
    while True:
        elapsed = time.time() - start_time
        
        if elapsed > timeout:
            print(f"\n⏱️ 超时! 已等待 {int(elapsed)} 秒")
            return {"error": "timeout", "elapsed": elapsed}
        
        task = query_task_status(video_id)
        
        if "error" in task:
            print(f"\n❌ 查询错误: {task.get('error')}")
            return task
        
        status = task.get("status", "unknown")
        progress = task.get("progress", 0)
        
        # 只在状态变化时打印
        if status != last_status:
            print(f"\n   [{int(elapsed)}s] 状态: {status} (进度: {progress}%)")
            last_status = status
        else:
            print(f".", end="", flush=True)
        
        if status == "completed":
            print(f"\n\n✅ 视频生成完成! 总耗时: {int(elapsed)}秒")
            # 视频URL在状态响应中
            video_url = task.get("video_url") or task.get("result_url") or task.get("url")
            if video_url:
                print(f"   视频URL: {video_url[:80]}...")
            return task
        elif status == "failed":
            print(f"\n\n❌ 视频生成失败!")
            return task
        
        time.sleep(poll_interval)


def download_video(video_url: str, save_path: str) -> bool:
    """
    下载视频文件
    
    Args:
        video_url: 视频URL
        save_path: 保存路径
        
    Returns:
        bool: 是否下载成功
    """
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
        
        print(f"\n✅ 视频已保存到: {save_path}")
        return True
        
    except Exception as e:
        print(f"\n❌ 下载失败: {e}")
        return False


def save_result(result: dict, filename: str):
    """保存结果到JSON文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"📄 结果已保存到: {filename}")


# ==================== 测试函数 ====================

def test_text_to_video():
    """测试1: 文生视频"""
    print("\n" + "="*60)
    print("🎬 测试1: 文生视频 (Text-to-Video)")
    print("="*60)
    
    prompt = "一只可爱的橘色小猫在阳光明媚的花园里追逐蝴蝶，毛茸茸的尾巴随风摆动"
    model = "veo-3.1-fast"  # 使用快速版省钱
    
    print(f"\n📝 测试参数:")
    print(f"   提示词: {prompt}")
    print(f"   模型: {model}")
    
    # 步骤1: 创建任务
    task = create_video_task(prompt, model)
    
    if "error" in task:
        print(f"\n❌ 测试失败: {task}")
        return None
    
    video_id = task.get("id")
    if not video_id:
        print(f"\n❌ 未获取到任务ID")
        return None
    
    # 步骤2: 等待完成（视频URL在状态响应中）
    completed = wait_for_video(video_id)
    
    if "error" in completed:
        print(f"\n❌ 等待失败: {completed}")
        return completed
    
    # 步骤3: 从状态响应中获取视频URL
    video_url = completed.get("video_url") or completed.get("result_url") or completed.get("url")
    
    print(f"\n📊 视频信息:")
    print(f"   URL: {video_url[:80] if video_url else 'N/A'}...")
    print(f"   时长: {completed.get('seconds', 'N/A')}秒")
    print(f"   分辨率: {completed.get('size', 'N/A')}")
    
    # 步骤4: 下载视频
    if video_url:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"text_to_video_{timestamp}.mp4"
        download_video(video_url, save_path)
    
    # 保存结果
    result = {
        "test_type": "text_to_video",
        "prompt": prompt,
        "model": model,
        "task": task,
        "completed": completed,
        "video_url": video_url,
        "timestamp": datetime.now().isoformat()
    }
    save_result(result, f"result_text_to_video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    
    return result


def test_image_to_video():
    """测试2: 图生视频（使用横屏快速版）"""
    print("\n" + "="*60)
    print("🖼️ 测试2: 横屏快速版文生视频")
    print("="*60)
    
    # 使用横屏快速版测试另一种模型
    prompt = "日落时分，金色的阳光洒在平静的海面上，海鸥在空中翱翔，远处的帆船缓缓驶过"
    model = "veo-3.1-landscape-fast"  # 横屏快速版
    
    print(f"\n📝 测试参数:")
    print(f"   提示词: {prompt}")
    print(f"   模型: {model} (横屏快速版)")
    
    # 步骤1: 创建任务
    task = create_video_task(prompt, model)
    
    if "error" in task:
        print(f"\n❌ 测试失败: {task}")
        return None
    
    video_id = task.get("id")
    if not video_id:
        print(f"\n❌ 未获取到任务ID")
        return None
    
    # 步骤2: 等待完成
    completed = wait_for_video(video_id)
    
    if "error" in completed:
        print(f"\n❌ 等待失败: {completed}")
        return completed
    
    # 步骤3: 从状态响应中获取视频URL
    video_url = completed.get("video_url") or completed.get("result_url") or completed.get("url")
    
    print(f"\n📊 视频信息:")
    print(f"   URL: {video_url[:80] if video_url else 'N/A'}...")
    print(f"   时长: {completed.get('seconds', 'N/A')}秒")
    print(f"   分辨率: {completed.get('size', 'N/A')}")
    
    # 步骤4: 下载视频
    if video_url:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"landscape_video_{timestamp}.mp4"
        download_video(video_url, save_path)
    
    # 保存结果
    result = {
        "test_type": "landscape_video",
        "prompt": prompt,
        "model": model,
        "task": task,
        "completed": completed,
        "video_url": video_url,
        "timestamp": datetime.now().isoformat()
    }
    save_result(result, f"result_landscape_video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    
    return result


# ==================== 主程序 ====================

def main():
    """主函数"""
    print("\n" + "="*60)
    print("🚀 Veo-3.1 异步 API 测试")
    print("="*60)
    print(f"\n⚙️ 配置:")
    print(f"   API Base URL: {BASE_URL}")
    print(f"   API Key: {API_KEY[:10]}...{API_KEY[-4:]}")
    
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
        status = "✅ 成功" if "error" not in r.get("content", {}) else "❌ 失败"
        print(f"\n   测试{i} ({test_type}): {status}")
    
    print("\n" + "="*60)
    print("🎉 测试完成!")
    print("="*60)


if __name__ == "__main__":
    main()

