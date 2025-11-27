# Gemini 音频理解 API 示例

使用 Gemini 2.5 Pro 模型进行音频转录、分析和理解，支持两种调用格式。

## 📁 文件说明

### 🎯 用户示例（推荐）

| 文件 | 格式 | 说明 |
|------|------|------|
| `gemini_audio_example.py` | OpenAI Chat | **推荐新手使用**，兼容 OpenAI 格式 |
| `gemini_audio_native_example.py` | Google 原生 | 原生 API 格式 |

### 🔬 内部测试

| 文件 | 格式 | 说明 |
|------|------|------|
| `gemini_audio_demo.py` | OpenAI Chat | 已填入 API Key，内部测试用 |
| `gemini_audio_native_demo.py` | Google 原生 | 已填入 API Key，内部测试用 |

### 📦 其他文件

| 文件 | 说明 |
|------|------|
| `test_audio.mp3` | 测试音频文件 |
| `快速开始.md` | 快速入门指南 |

---

## 🔀 两种调用格式对比

| 特性 | Chat 格式 | 原生格式 |
|------|-----------|----------|
| **端点** | `/v1/chat/completions` | `/v1beta/models/.../generateContent` |
| **兼容性** | ✅ 完美兼容 OpenAI SDK | 需要原生调用 |
| **音频输入** | data URI (base64) | inline_data (base64) |
| **响应格式** | OpenAI 格式 | Google 原生格式 |

### 💡 选择建议

- **新手 / 快速上手**：使用 Chat 格式 (`gemini_audio_example.py`)
- **熟悉 Google API**：使用原生格式 (`gemini_audio_native_example.py`)

---

## 功能特点

- ✅ 支持音频转录（转文字）
- ✅ 支持音频内容分析和总结
- ✅ 支持多种音频格式（MP3, WAV, M4A, WEBM, OGG, FLAC 等）
- ✅ 自动保存结果（TXT + JSON 格式）
- ✅ 高准确度的中英文识别
- ✅ 使用 requests 库，无需额外 SDK

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install requests
```

### 2. 配置 API Key

编辑示例文件，找到顶部的 API_KEY 变量：

```python
# ============================================================
# ⚠️ 请在这里填入您的 API Key
# 获取地址: https://api.laozhang.ai/
# ============================================================
API_KEY = "sk-your-api-key-here"  # ← 替换为您的实际 API Key
# ============================================================
```

### 3. 运行测试

```bash
# Chat 格式（推荐）
python gemini_audio_example.py

# 原生格式
python gemini_audio_native_example.py

# 指定音频文件
python gemini_audio_example.py /path/to/your/audio.mp3
```

---

## 使用示例

### Chat 格式

```python
from gemini_audio_example import gemini_audio_analysis

result = gemini_audio_analysis(
    question="请转录这段音频的内容",
    audio_path="test_audio.mp3"
)
print(result['result'])
```

### 原生格式

```python
from gemini_audio_native_example import gemini_audio_native

result = gemini_audio_native(
    question="请转录这段音频的内容",
    audio_path="test_audio.mp3"
)
print(result['result'])
```

---

## 支持的模型

| 模型 | 特点 | 推荐场景 |
|------|------|---------|
| `gemini-2.5-pro` | 高准确度，强大的理解能力 | 专业转录、深度分析 |
| `gemini-2.0-flash-exp` | 速度快，成本低 | 实时处理、批量任务 |

## 支持的音频格式

- MP3 (.mp3)
- WAV (.wav)
- M4A (.m4a)
- MP4 音频 (.mp4)
- MPEG (.mpeg, .mpga)
- WEBM (.webm)
- OGG (.ogg)
- FLAC (.flac)

**文件大小限制**: 建议不超过 20MB

---

## 提示词建议

| 需求 | 推荐提示词 |
|------|-----------|
| 转录 | "请转录这段音频的内容" |
| 总结 | "请用3-5句话总结这段音频的主要内容" |
| 翻译 | "请将这段音频转录并翻译成英文" |
| 分析 | "请分析这段音频的情绪基调和讨论主题" |
| 提取 | "请提取音频中提到的关键数字和日期" |

---

## 常见问题

### Q: Chat 格式和原生格式有什么区别？

A: 
- **Chat 格式**：使用 OpenAI 兼容的 API 格式，更简单易用
- **原生格式**：使用 Google 原生 API 格式，更接近官方文档

两种格式功能相同，选择您熟悉的即可。

### Q: 为什么使用 requests 而不是 openai 库？

A: 使用 requests 库更加轻量级，不需要安装额外的 SDK，代码更简单易懂，适合学习和定制。

### Q: 如何提高识别准确度？

A: 
1. 使用 `gemini-2.5-pro` 模型（准确度更高）
2. 提供清晰、无噪音的音频
3. 使用具体明确的提示词

---

## 代码结构

```
audio-API/
├── gemini_audio_demo.py           # Chat 格式（内部测试）
├── gemini_audio_example.py        # Chat 格式（用户版）
├── gemini_audio_native_demo.py    # 原生格式（内部测试）
├── gemini_audio_native_example.py # 原生格式（用户版）
├── test_audio.mp3                 # 测试音频
├── README.md                      # 本文档
└── 快速开始.md                    # 快速入门
```

---

## 相关资源

- 📖 [API 文档](https://docs.laozhang.ai/)
- 🔑 [获取 API Key](https://api.laozhang.ai/)
- 💬 技术支持：参考文档中的联系方式
