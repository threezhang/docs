# Veo-3.1 视频生成 API 示例

使用 Veo-3.1 模型进行视频生成，支持同步和异步两种调用方式。

## 测试结果

### 同步 API 测试 ✅

| 测试类型 | 模型 | 耗时 | 视频大小 | 状态 |
|---------|------|------|----------|------|
| 文生视频 | `veo-3.1-fast` | 352秒 | 3.97 MB | ✅ 成功 |
| 图生视频 | `veo-3.1-fast-fl` | 189秒 | 1.30 MB | ✅ 成功 |

### 异步 API 测试 ✅

| 测试类型 | 模型 | 耗时 | 视频大小 | 状态 |
|---------|------|------|----------|------|
| 文生视频 | `veo-3.1-fast` | 406秒 | 5.5 MB | ✅ 成功 |
| 图生视频 | `veo-3.1-fast-fl` | 151秒 | 1.21 MB | ✅ 成功 |

> ⚠️ **异步 API 图生视频注意事项**: 需要使用 `multipart/form-data` 格式上传本地图片文件，不支持图片 URL。

## 功能特点

- ✅ 同步 API（OpenAI 兼容格式）
- ✅ 异步 API（任务队列方式）
- ✅ 文生视频（Text-to-Video）
- ✅ 图生视频（Image-to-Video）
- ✅ 自动下载视频文件
- ✅ 结果保存为 JSON 格式

## 快速开始

### 1. 安装依赖

```bash
pip install requests
```

### 2. 配置 API Key

编辑脚本文件，替换 API Key：

```python
API_KEY = "sk-your-api-key-here"  # ← 替换为您的实际 API Key
```

### 3. 运行测试

```bash
cd code-demo/veo-async-API

# 同步 API 测试（推荐先测试这个）
python veo_sync_demo.py

# 异步 API 测试
python veo_async_demo.py
```

## 文件说明

```
veo-async-API/
├── veo_sync_demo.py              # 同步 API 测试脚本
├── veo_async_demo.py             # 异步 API 测试脚本
├── README.md                     # 本文档
├── sync_text_to_video_*.mp4      # 同步文生视频结果
├── sync_image_to_video_*.mp4     # 同步图生视频结果
├── text_to_video_test1.mp4       # 异步文生视频结果
└── result_*.json                 # JSON 格式结果文件
```

## 同步 vs 异步

| 特性 | 同步 API | 异步 API |
|------|----------|----------|
| **端点** | `/v1/chat/completions` | `/v1/videos` |
| **调用方式** | 单次请求，流式返回 | 创建任务 → 轮询 → 获取结果 |
| **图生视频** | 支持 URL 和 Base64 | 支持 URL |
| **失败扣费** | 请求成功就扣费 | ⭐ 失败不扣费 |
| **稳定性** | 依赖长连接 | ⭐ 更稳定 |
| **适用场景** | 快速测试、实时反馈 | 生产环境、批量生成 |

## 可用模型

| 模型名称 | 画幅 | 速度 | 图生视频 | 价格 |
|---------|------|------|---------|------|
| `veo-3.1` | 竖屏 | 标准 | ❌ | $0.25/次 |
| `veo-3.1-fl` | 竖屏 | 标准 | ✅ | $0.25/次 |
| `veo-3.1-fast` | 竖屏 | 快速 | ❌ | $0.15/次 |
| `veo-3.1-fast-fl` | 竖屏 | 快速 | ✅ | $0.15/次 |
| `veo-3.1-landscape` | 横屏 | 标准 | ❌ | $0.25/次 |
| `veo-3.1-landscape-fl` | 横屏 | 标准 | ✅ | $0.25/次 |
| `veo-3.1-landscape-fast` | 横屏 | 快速 | ❌ | $0.15/次 |
| `veo-3.1-landscape-fast-fl` | 横屏 | 快速 | ✅ | $0.15/次 |

**命名规则：**
- `landscape` = 横屏（16:9）
- `fast` = 快速版（更便宜）
- `fl` = 支持帧转视频（图生视频）

## 同步 API 示例

```python
import requests

API_KEY = "your-api-key"
BASE_URL = "https://api.laozhang.ai/v1"

# 文生视频
response = requests.post(
    f"{BASE_URL}/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "veo-3.1-fast",
        "messages": [{
            "role": "user",
            "content": [{"type": "text", "text": "一只猫咪在花园里玩耍"}]
        }],
        "stream": True
    },
    stream=True
)

# 处理流式响应...
```

```python
# 图生视频
response = requests.post(
    f"{BASE_URL}/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "veo-3.1-fast-fl",
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "让这只猫咪动起来"},
                {"type": "image_url", "image_url": {"url": "https://example.com/cat.jpg"}}
            ]
        }],
        "stream": True
    },
    stream=True
)
```

## 异步 API 示例

### 文生视频

```python
import requests
import time

API_KEY = "your-api-key"
BASE_URL = "https://api.laozhang.ai/v1"

# 1. 创建任务
response = requests.post(
    f"{BASE_URL}/videos",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "veo-3.1-fast",
        "prompt": "一只猫咪在花园里玩耍"
    }
)
video_id = response.json()["id"]

# 2. 轮询状态
while True:
    response = requests.get(
        f"{BASE_URL}/videos/{video_id}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    data = response.json()
    status = data["status"]
    
    if status == "completed":
        video_url = data.get("video_url") or data.get("url")
        print(f"视频URL: {video_url}")
        break
    elif status == "failed":
        print("生成失败")
        break
    
    time.sleep(5)

# 3. 下载视频
video_data = requests.get(video_url).content
with open("output.mp4", "wb") as f:
    f.write(video_data)
```

### 图生视频（需要上传本地图片）

```python
import requests
import time

API_KEY = "your-api-key"
BASE_URL = "https://api.laozhang.ai/v1"

# 1. 创建任务（使用 multipart/form-data 上传图片）
with open("your_image.jpg", "rb") as f:
    response = requests.post(
        f"{BASE_URL}/videos",
        headers={"Authorization": f"Bearer {API_KEY}"},
        files={"input_reference": ("image.jpg", f, "image/jpeg")},
        data={
            "model": "veo-3.1-fast-fl",  # 必须使用 -fl 后缀的模型
            "prompt": "让这只猫咪动起来"
        }
    )
video_id = response.json()["id"]

# 2. 轮询状态（同上）
# 3. 下载视频（同上）
```

> ⚠️ 异步 API 图生视频**不支持图片 URL**，必须上传本地文件！

## 相关资源

- 📖 [同步 API 文档](https://docs.laozhang.ai/api-capabilities/veo/veo-31-quick-start)
- 📖 [异步 API 文档](https://docs.laozhang.ai/api-capabilities/veo/veo-31-async-api)
- 🔑 [获取 API Key](https://api.laozhang.ai/token)
- 💬 Telegram: https://t.me/laozhang_cn

## 许可证

本示例代码仅供学习和参考使用。
