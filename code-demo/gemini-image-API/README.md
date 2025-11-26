# Gemini 图像 API - 示例代码

完整的 Gemini 图像生成/编辑 API 示例代码，支持两种调用格式。

## 📁 文件说明

### 🎯 快速上手（推荐）

| 文件 | 格式 | 类型 | 说明 |
|------|------|------|------|
| `gemini_chat_example.py` | OpenAI Chat | 用户版 | **推荐新手使用**，兼容 OpenAI SDK |
| `gemini_native_example.py` | Google 原生 | 用户版 | 支持自定义纵横比和 4K |

### 🔬 测试文件（内部）

| 文件 | 格式 | 类型 | 说明 |
|------|------|------|------|
| `gemini_chat_demo.py` | OpenAI Chat | 测试版 | 带测试 Key，内部测试用 |
| `gemini_native_demo.py` | Google 原生 | 测试版 | 带测试 Key，内部测试用 |

### 📦 其他文件

| 文件 | 说明 |
|------|------|
| `complete_demo.py` | 完整演示（三个场景串联）|
| `nano_banana_demo.py` | Nano Banana 稳定版演示 |
| `nano_banana2_demo.py` | Nano Banana 2 最新版演示 |
| `config.py` | API Key 配置文件 |

---

## 🚀 快速开始

### 1. 安装依赖

```bash
# Chat 格式需要
pip install openai requests

# 原生格式只需要
pip install requests
```

### 2. 配置 API Key

编辑示例文件，修改 `API_KEY` 变量：
```python
API_KEY = "sk-YOUR_API_KEY"  # 替换为您的 API Key
```

获取 API Key：https://api.laozhang.ai/token

### 3. 运行示例

```bash
# Chat 格式（推荐新手）
python3 gemini_chat_example.py

# 原生格式（更多功能）
python3 gemini_native_example.py
```

---

## 🔀 两种调用格式对比

| 特性 | Chat 格式 | 原生格式 |
|------|-----------|----------|
| **端点** | `/v1/chat/completions` | `/v1beta/models/.../generateContent` |
| **兼容性** | ✅ 完美兼容 OpenAI SDK | 需要原生调用 |
| **图片输入** | URL 或 Base64 | Base64 |
| **纵横比** | ❌ 固定 1:1 | ✅ 支持 10 种 |
| **分辨率** | ❌ 固定 1K | ✅ 1K/2K/4K |
| **使用场景** | 快速迁移、简单需求 | 自定义尺寸、高分辨率 |

### 💡 选择建议

- **新手 / 快速上手**：使用 Chat 格式 (`gemini_chat_example.py`)
- **需要自定义纵横比**：使用原生格式 (`gemini_native_example.py`)
- **需要 4K 超高清**：使用原生格式 + Nano Banana 2

---

## 📊 模型对比

| 特性 | Nano Banana | Nano Banana 2 |
|------|-------------|---------------|
| **模型** | `gemini-2.5-flash-image` | `gemini-3-pro-image-preview` |
| **版本** | 稳定版 | 最新版 (Preview) |
| **分辨率** | 1K (固定) | 1K / 2K / 4K |
| **价格** | **$0.025/张** | $0.05/张 |
| **官网价** | $0.04/张 | $0.24/张 |
| **节省** | 37.5% | **79%** 🔥 |
| **速度** | ~10秒 | ~10秒 |
| **推荐** | 生产环境 | 追求质量/4K |

---

## 📸 功能场景

### ✅ 支持的功能

1. **文生图** - 从文字描述生成图片
2. **单图编辑** - 添加元素、风格转换
3. **多图合成** - 创意融合多张图片
4. **4K 超高清** - 生成 4K 分辨率图片（仅 Nano Banana 2）

### 📐 支持的纵横比（原生格式）

| 类型 | 比例 |
|------|------|
| 横向 | 21:9 (超宽屏), 16:9 (宽屏), 4:3, 3:2 |
| 正方形 | 1:1 |
| 纵向 | 9:16 (竖屏), 3:4, 2:3 |
| 其他 | 5:4, 4:5 |

---

## ❓ 常见问题

**Q: Chat 格式和原生格式有什么区别？**  
A: Chat 格式兼容 OpenAI SDK，更简单；原生格式支持更多参数（纵横比、分辨率）。

**Q: 如何使用 4K 分辨率？**  
A: 必须使用原生格式 + Nano Banana 2 模型，设置 `image_size="4K"`。

**Q: 提示词用中文还是英文？**  
A: 都支持，英文效果通常更好。

**Q: demo 和 example 有什么区别？**  
A: demo 是内部测试版（带测试 Key），example 是用户版（需要填入自己的 Key）。

---

## 📚 相关文档

- [图像生成文档](https://docs.laozhang.ai/api-capabilities/gemini-flash-image)
- [图像编辑文档](https://docs.laozhang.ai/api-capabilities/gemini-flash-image-edit)
- [获取 API Key](https://api.laozhang.ai/token)

---

## 🎯 设计理念

**简单到极致**
- ✅ 只需改一个 API Key
- ✅ 运行一个命令
- ✅ 输出清晰易懂

**两种格式，按需选择**
- ✅ Chat 格式：快速上手，兼容性好
- ✅ 原生格式：功能完整，参数灵活

**生产级质量**
- ✅ 完善的错误处理
- ✅ 清晰的参数说明
- ✅ 可直接集成到项目
