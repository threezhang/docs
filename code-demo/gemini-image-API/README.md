# Gemini 图像生成 API - 示例代码

三个场景，一键运行，快速上手 Gemini 图像生成 API。

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install requests
```

### 2. 配置 API Key
编辑 `complete_demo.py`，替换第 22 行的 API Key：
```python
API_KEY = "sk-YOUR_API_KEY"  # 改成你的 Key
```

### 3. 运行演示
```bash
python3 complete_demo.py
```

就这么简单！脚本会自动演示三个场景。

---

## 📸 三个演示场景（逐步递进）

### 场景 1：文生图 → 生成第一张图
**功能**：从文字描述生成图片  
**输入**：提示词 "一只可爱的橘猫"  
**输出**：`result_1_text_to_image.png`

### 场景 2：单图生图 → 用第一张图生成第二张图
**功能**：图片风格转换  
**输入**：`result_1_text_to_image.png`（场景1生成的图）  
**提示词**：把这只猫变成梵高星空风格的油画  
**输出**：`result_2_image_style_transfer.png`

### 场景 3：多图混合 → 用第一张和第二张生成第三张图
**功能**：创意合成  
**输入**：第一张图 + 第二张图  
**提示词**：将这两只猫融合成一个艺术作品  
**输出**：`result_3_multi_image_mix.png`

**逻辑清晰**：场景1 → 场景2 → 场景3，前后衔接，一气呵成！

---

## 🔧 自定义参数

### 切换模型
```python
USE_NANO_BANANA_2 = True   # Nano Banana 2 (4K, $0.05/张)
USE_NANO_BANANA_2 = False  # Nano Banana (1K, $0.025/张)
```

### 修改提示词
在 `main()` 函数中找到对应场景，修改 `prompt` 参数：
```python
# 场景 1
prompt="你的提示词"

# 场景 2
prompt="你的风格转换描述"

# 场景 3
prompt="你的创意合成描述"
```

### 调整分辨率（仅 Nano Banana 2）
```python
image_size="1K"  # 标准分辨率
image_size="2K"  # 高清分辨率
image_size="4K"  # 超高清分辨率
```

### 修改纵横比
```python
aspect_ratio="16:9"  # 横向宽屏
aspect_ratio="1:1"   # 正方形
aspect_ratio="9:16"  # 竖屏
```

---

## 📊 模型对比

| 特性 | Nano Banana | Nano Banana 2 |
|------|-------------|---------------|
| **模型** | `gemini-2.5-flash-image` | `gemini-3-pro-image-preview` |
| **分辨率** | 1K (固定) | 1K / 2K / 4K |
| **价格** | **$0.025/张** | $0.05/张 |
| **官网** | $0.04/张 | $0.24/张 |
| **节省** | 37.5% | **79%** 🔥 |
| **速度** | ~10秒 | ~10秒 |
| **推荐** | 生产环境 | 追求质量/4K |

---

## 💡 选择建议

### 用 Nano Banana（稳定版）如果：
- ✅ 1K 分辨率足够（网页、社交媒体）
- ✅ 需要最低成本（$0.025/张）
- ✅ 生产环境，追求稳定

### 用 Nano Banana 2（最新版）如果：
- ✅ 需要 4K 超高清
- ✅ 追求最佳质量
- ✅ 复杂的图片合成

---

## 📁 其他脚本

### `nano_banana_demo.py`
纯净版，只用稳定版模型，代码最简洁。

### `nano_banana2_demo.py`
展示 Nano Banana 2 的所有高级功能。

### `main.py`
交互式菜单，自动下载测试图片。

---

## ❓ 常见问题

**Q: 三个场景的关系？**  
A: 逐步递进！场景1生成图 → 场景2用它变换风格 → 场景3融合两张图。

**Q: 可以只运行场景1吗？**  
A: 可以！每个场景独立。但按顺序运行体验最好。

**Q: 输出文件在哪？**  
A: 当前目录，文件名清晰：
- `result_1_text_to_image.png` (场景1输出)
- `result_2_image_style_transfer.png` (场景2输出)
- `result_3_multi_image_mix.png` (场景3输出)

**Q: 提示词用中文还是英文？**  
A: 都支持，英文效果更好。中文示例让你快速理解。

**Q: 如何获取 API Key？**  
A: 访问 [api.laozhang.ai](https://api.laozhang.ai)

---

## 📚 完整文档

- [图像生成文档](https://docs.laozhang.ai/api-capabilities/gemini-flash-image)
- [图像编辑文档](https://docs.laozhang.ai/api-capabilities/gemini-flash-image-edit)

---

## 🎯 设计理念

**简单到极致**
- ✅ 只需改一个 API Key
- ✅ 运行一个命令
- ✅ 输出清晰易懂
- ✅ 用户一眼看懂

**生产级质量**
- ✅ 完善的错误处理
- ✅ 清晰的参数说明
- ✅ 可直接集成到项目
- ✅ 中文注释详尽
