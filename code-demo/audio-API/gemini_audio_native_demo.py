"""
Gemini 音频理解 API 示例 - Google 原生格式 (Demo)

使用 Gemini 模型进行音频转录、分析和理解
采用 Google 原生 API 格式调用

作者: 老张 API
文档: https://docs.laozhang.ai/
"""

import requests
import base64
import json
from datetime import datetime
import os


def gemini_audio_native(question, audio_path, model="gemini-2.5-pro", api_key=None):
    """
    使用 Gemini 模型分析本地音频内容（Google 原生格式）
    
    参数:
        question (str): 要问的问题
        audio_path (str): 本地音频文件路径
        model (str, optional): 模型名称，默认 "gemini-2.5-pro"
        api_key (str, optional): API密钥
    
    返回:
        dict: 包含结果的字典
    """
    
    # API 配置 - Demo 版本（内部测试用，已填入 API Key）
    if api_key is None:
        api_key = "sk-9SOAt1Bkvcv97WDXE0464d8b0712406f86594f4968524fBd"
    
    base_url = "https://api.laozhang.ai"
    
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
            '.webm': 'audio/webm',
            '.ogg': 'audio/ogg',
            '.flac': 'audio/flac'
        }
        mime_type = mime_type_map.get(ext, 'audio/mp3')
        
        # 构建 Google 原生格式请求数据
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": question
                        },
                        {
                            "inline_data": {
                                "mime_type": mime_type,
                                "data": audio_b64
                            }
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 4096
            }
        }
        
        # 发送请求
        print(f"\n开始分析音频（模型: {model}，格式: Google 原生）...")
        
        # 原生格式端点
        url = f"{base_url}/v1beta/models/{model}:generateContent"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=120
        )
        
        # 检查响应
        if response.status_code == 200:
            result_data = response.json()
            
            # 解析原生格式响应
            if 'candidates' in result_data and len(result_data['candidates']) > 0:
                candidate = result_data['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    parts = candidate['content']['parts']
                    result_text = ""
                    for part in parts:
                        if 'text' in part:
                            result_text += part['text']
                    
                    return {
                        "result": result_text,
                        "model": model,
                        "audio_path": audio_path,
                        "question": question,
                        "format": "native",
                        "success": True
                    }
            
            return {
                "result": f"无法解析响应: {json.dumps(result_data, ensure_ascii=False)}",
                "model": model,
                "audio_path": audio_path,
                "question": question,
                "format": "native",
                "success": False,
                "error": "响应格式异常"
            }
        else:
            error_msg = f"API 错误 {response.status_code}: {response.text}"
            return {
                "result": error_msg,
                "model": model,
                "audio_path": audio_path,
                "question": question,
                "format": "native",
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
            "format": "native",
            "success": False,
            "error": str(e)
        }


def save_results(data, output_dir=None):
    """保存音频分析结果到文件"""
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 保存 TXT
    txt_file = os.path.join(output_dir, f"gemini_audio_native_{timestamp}.txt")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("Gemini 音频理解分析结果（原生格式）\n")
        f.write("=" * 60 + "\n")
        f.write(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"模型: {data['model']}\n")
        f.write(f"格式: {data.get('format', 'native')}\n")
        f.write(f"音频文件: {data.get('audio_path', 'N/A')}\n")
        f.write(f"提问内容: {data['question']}\n")
        f.write(f"状态: {'成功' if data.get('success') else '失败'}\n")
        f.write("=" * 60 + "\n\n")
        f.write(data['result'])
        f.write("\n\n" + "=" * 60 + "\n")
    
    # 保存 JSON
    json_file = os.path.join(output_dir, f"gemini_audio_native_{timestamp}.json")
    json_data = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        **data
    }
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    return txt_file, json_file


if __name__ == "__main__":
    """主程序入口"""
    print("=" * 60)
    print("Gemini 音频理解测试（Google 原生格式）")
    print("=" * 60)
    
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
        result_data = gemini_audio_native(
            question=question,
            audio_path=audio_path,
            model="gemini-2.5-pro"
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

