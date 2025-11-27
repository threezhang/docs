"""
Gemini 音频理解 API 示例 - Example 版本

使用 Gemini 模型进行音频转录、分析和理解
支持多种音频格式：MP3, WAV, M4A, WEBM 等

使用前请先获取 API Key：https://api.laozhang.ai/

作者: 老张 API
文档: https://docs.laozhang.ai/
"""

import requests
import base64
import json
from datetime import datetime
import os


# ============================================================
# ⚠️ 请在这里填入您的 API Key
# 获取地址: https://api.laozhang.ai/
# ============================================================
API_KEY = "sk-your-api-key-here"  # ← 替换为您的实际 API Key
# ============================================================


def gemini_audio_analysis(question, audio_path, model="gemini-2.5-pro", api_key=None):
    """
    使用 Gemini 模型分析本地音频内容
    
    参数:
        question (str): 要问的问题
            - "请转录这段音频的内容"
            - "请总结这段音频的主要内容" 
            - "这段音频讨论了什么主题？"
            - 或其他任何关于音频的问题
            
        audio_path (str): 本地音频文件路径
            支持格式: mp3, wav, m4a, mp4, mpeg, webm
            
        model (str, optional): 使用的模型，默认 "gemini-2.5-pro"
            - "gemini-2.5-pro": 高准确度，强大理解能力
            - "gemini-2.0-flash-exp": 速度快，成本低
            
        api_key (str, optional): API密钥，如果不提供则使用全局配置
    
    返回:
        dict: 包含以下字段
            - result: 音频分析结果
            - model: 使用的模型名称
            - audio_path: 音频文件路径
            - question: 提出的问题
            - success: 是否成功
            - error: 错误信息（如果失败）
    
    示例:
        >>> result = gemini_audio_analysis(
        ...     question="请转录这段音频",
        ...     audio_path="test.mp3"
        ... )
        >>> print(result['result'])
    """
    
    # API 配置
    if api_key is None:
        api_key = API_KEY
    
    # 检查 API Key 是否已配置
    if api_key == "sk-your-api-key-here":
        return {
            "result": "错误：请先配置 API Key",
            "model": model,
            "audio_path": audio_path,
            "question": question,
            "success": False,
            "error": "API Key 未配置，请修改代码顶部的 API_KEY 变量"
        }
    
    base_url = "https://api.laozhang.ai/v1"
    
    # 检查文件是否存在
    if not os.path.exists(audio_path):
        return {
            "result": f"错误：文件不存在 - {audio_path}",
            "model": model,
            "audio_path": audio_path,
            "question": question,
            "success": False,
            "error": "文件不存在"
        }
    
    # 读取音频文件
    print(f"正在读取本地音频: {audio_path}")
    file_size = os.path.getsize(audio_path) / (1024 * 1024)  # MB
    print(f"文件大小: {file_size:.2f} MB")
    
    if file_size > 20:
        print("⚠️  警告：文件大于20MB，可能会影响处理速度")
    
    try:
        # 读取音频文件并转为 base64
        with open(audio_path, "rb") as f:
            audio_b64 = base64.b64encode(f.read()).decode()
        
        # 确定 MIME 类型
        ext = os.path.splitext(audio_path)[1].lower()
        mime_type_map = {
            '.mp3': 'audio/mp3',
            '.wav': 'audio/wav',
            '.m4a': 'audio/m4a',
            '.mp4': 'audio/mp4',
            '.mpeg': 'audio/mpeg',
            '.mpga': 'audio/mpeg',
            '.webm': 'audio/webm'
        }
        mime_type = mime_type_map.get(ext, 'audio/mp3')
        
        audio_source = f"data:{mime_type};base64,{audio_b64}"
        
        # 构建请求数据
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can analyze audio content."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": question},
                        {
                            "type": "image_url",
                            "image_url": {"url": audio_source}
                        }
                    ]
                }
            ],
            "temperature": 0.2,
            "max_tokens": 4096
        }
        
        # 发送请求
        print(f"\n开始分析音频（模型: {model}）...")
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        # 检查响应
        if response.status_code == 200:
            result_data = response.json()
            result_text = result_data['choices'][0]['message']['content']
            
            return {
                "result": result_text,
                "model": model,
                "audio_path": audio_path,
                "question": question,
                "success": True
            }
        else:
            error_msg = f"API 错误 {response.status_code}: {response.text}"
            return {
                "result": error_msg,
                "model": model,
                "audio_path": audio_path,
                "question": question,
                "success": False,
                "error": error_msg
            }
            
    except Exception as e:
        error_msg = f"错误: {str(e)}"
        return {
            "result": error_msg,
            "model": model,
            "audio_path": audio_path,
            "question": question,
            "success": False,
            "error": str(e)
        }


def save_results(data, output_dir=None):
    """
    保存音频分析结果到文件
    
    参数:
        data (dict): 分析结果数据
        output_dir (str, optional): 输出目录，默认为当前目录
    
    返回:
        tuple: (txt_file_path, json_file_path)
    """
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 保存 TXT
    txt_file = os.path.join(output_dir, f"gemini_audio_analysis_{timestamp}.txt")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("Gemini 音频理解分析结果\n")
        f.write("=" * 60 + "\n")
        f.write(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"模型: {data['model']}\n")
        f.write(f"音频文件: {data.get('audio_path', 'N/A')}\n")
        f.write(f"提问内容: {data['question']}\n")
        f.write(f"状态: {'成功' if data.get('success') else '失败'}\n")
        f.write("=" * 60 + "\n\n")
        f.write(data['result'])
        f.write("\n\n" + "=" * 60 + "\n")
    
    # 保存 JSON
    json_file = os.path.join(output_dir, f"gemini_audio_analysis_{timestamp}.json")
    json_data = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        **data
    }
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    return txt_file, json_file


if __name__ == "__main__":
    """
    主程序入口
    
    使用方法:
        1. 先修改代码顶部的 API_KEY 变量
        2. 运行: python gemini_audio_example.py                    # 使用默认测试音频
        3. 或者: python gemini_audio_example.py /path/to/audio.mp3 # 使用指定音频
    """
    print("=" * 60)
    print("Gemini 音频理解示例")
    print("=" * 60)
    
    # 检查 API Key
    if API_KEY == "sk-your-api-key-here":
        print("\n⚠️  请先配置 API Key!")
        print("   1. 打开本文件")
        print("   2. 找到顶部的 API_KEY 变量")
        print("   3. 将 'sk-your-api-key-here' 替换为您的实际 API Key")
        print("\n   获取 API Key: https://api.laozhang.ai/")
        exit(1)
    
    # 设置音频文件路径
    import sys
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
    else:
        audio_path = os.path.join(os.path.dirname(__file__), "test_audio.mp3")
    
    if not os.path.exists(audio_path):
        print(f"\n⚠️  未找到音频文件: {audio_path}")
        print("\n使用方法：")
        print(f"  python {os.path.basename(__file__)} /path/to/your/audio.mp3")
        exit(1)
    
    # 测试问题
    question = "请转录这段音频的内容"
    
    print(f"\n{'=' * 60}")
    print(f"提问: {question}")
    print(f"{'=' * 60}")
    
    try:
        # 运行分析
        result_data = gemini_audio_analysis(
            question=question,
            audio_path=audio_path,
            model="gemini-2.5-pro"  # 可选: "gemini-2.0-flash-exp"
        )
        
        if result_data['success']:
            # 保存结果
            txt_file, json_file = save_results(result_data)
            
            # 控制台输出
            print("\n" + "=" * 60)
            print("分析结果：")
            print("=" * 60)
            print(result_data['result'])
            print("\n" + "=" * 60)
            print(f"✅ 结果已保存:")
            print(f"  📄 TXT: {txt_file}")
            print(f"  📋 JSON: {json_file}")
            print("=" * 60)
        else:
            print(f"\n❌ 分析失败: {result_data['result']}")
        
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        import traceback
        traceback.print_exc()

