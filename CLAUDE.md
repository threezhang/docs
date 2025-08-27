# 项目配置 - 老张API文档中心

## 项目概述
这是一个基于 Mintlify 的文档网站项目，为 老张API 提供技术文档和FAQ支持。官网 https://mintlify.com/

## 文档编写规范

### MDX文件格式要求
- **重要**：Mintlify会自动从frontmatter的`title`字段生成H1标题
- **禁止**：在MDX文件内容中使用H1标题（`# 标题`）
- **原因**：会导致页面出现重复的H1标题，影响SEO和用户体验

### 正确的文件结构
```mdx
---
title: "页面标题"
description: "页面描述"
icon: "图标名称"
---

## 第一个章节标题
内容从H2开始...

### 子标题
使用H3及以下级别的标题
```

### 错误的文件结构（避免）
```mdx
---
title: "页面标题"
---

# 页面标题  ← 不要这样做！会重复显示

## 第一个章节标题
```

## 文档系统说明
- 使用Mintlify文档框架
- 支持MDX格式（Markdown + JSX组件）
- 导航结构在`docs.json`中定义
- 图片资源存放在`images/`目录

## FAQ页面组织
- 所有FAQ页面位于`faq/`目录
- 作为独立的顶级标签页展示
- 每个问题一个独立的MDX文件

## 编写新内容时的注意事项
1. 遵循上述MDX格式规范
2. 使用适当的Mintlify组件（Info, Warning, Tip, Card等）
3. 保持中文内容的专业性和友好性
4. 引用图片时使用相对路径`/images/文件名`

### 图片格式要求
#### 推荐格式
- **PNG**：用于图解、流程图、架构图等需要高质量显示的图片
- **JPEG**：用于照片类图像，文件较大但压缩率高
- **外部托管SVG**：如需使用SVG，建议外部托管并通过URL引用

#### 格式使用指南
- **图解说明**：优先使用PNG格式，确保清晰度和兼容性
- **图标**：使用Font Awesome或Lucide内置图标，避免自定义SVG
- **浅色/深色主题**：为不同主题准备两个版本的PNG图片
  ```html
  <img className="block dark:hidden" src="/images/diagram-light.png" alt="浅色主题图解" />
  <img className="hidden dark:block" src="/images/diagram-dark.png" alt="深色主题图解" />
  ```

#### 注意事项
- **避免内联SVG**：Mintlify对内联SVG支持存在问题，可能导致渲染错误
- **文件大小**：PNG文件控制在200KB以内，JPEG控制在500KB以内
- **命名规范**：使用描述性文件名，如 `transformer-architecture-light.png`
- **测试环境**：本地预览正常不代表生产环境正常，务必在部署后检查

### 其他要求
- 注意：不使用 HTML 注释语法，需要使用JSX注释语法
