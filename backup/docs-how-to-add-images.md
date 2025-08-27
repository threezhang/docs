 📸 文档系统配图最佳实践

  1. 图片存储位置

  - 统一存储：所有图片都应放在 /docs/images/ 目录下
  - 组织结构：如果图片较多，可以在 images 目录下创建子文件夹，如：
    - /docs/images/scenarios/
    - /docs/images/api-examples/
    - /docs/images/ui-screenshots/

  2. 图片路径引用

  # ✅ 正确的引用方式
  ![图片描述](/images/图片名.png)

  # ❌ 错误的引用方式
  ![图片描述](./images/图片名.png)  # 相对路径可能导致图片无法显示
  ![图片描述](images/图片名.png)     # 缺少前导斜杠

  3. 图片命名规范

  - 使用小写字母：cursor-setting.png 而不是 Cursor-Setting.png
  - 使用连字符：api-key-setup.png 而不是 api_key_setup.png
  - 描述性命名：cursor-model-configuration.png 比 image1.png 更好
  - 避免空格：使用 - 代替空格

  4. 图片格式建议

  - 截图：使用 PNG 格式，清晰度高
  - 流程图/图表：PNG 或 SVG
  - 照片：JPG/JPEG（文件较小）
  - 动画演示：GIF（适度使用）

  5. 图片优化

  - 尺寸控制：宽度通常不超过 1200px
  - 文件大小：尽量控制在 500KB 以内
  - 清晰度：确保文字和界面元素清晰可读

  6. 替代文本

  # 提供有意义的替代文本
  ![Cursor 编辑器中配置 API 密钥的设置界面](/images/cursor-api-setup.png)

  # 而不是
  ![图片](/images/image1.png)

  7. 图片标注和说明

  ![Cursor 配置界面](/images/cursor-setting.png)

  <Caption>
    图 1：在 Cursor 中配置 老张API 的设置界面
  </Caption>

  8. 响应式考虑

  如果需要控制图片显示大小：
  <img 
    src="/images/cursor-setting.png" 
    alt="Cursor 配置界面" 
    width="600"
  />

  9. 多图组织

  使用 Mintlify 的组件：
  <CardGroup cols={2}>
    <img src="/images/step-1.png" alt="步骤 1" />
    <img src="/images/step-2.png" alt="步骤 2" />
  </CardGroup>

  10. 实际示例

  假设您要在文档中添加新图片：

  1. 保存图片：将图片保存到 /docs/images/ 目录
  /docs/images/cursor-model-selection.png
  2. 在 MDX 中引用：
  ## 模型选择

  在 Cursor 中选择合适的 AI 模型：

  ![Cursor 模型选择界面](/images/cursor-model-selection.png)
  3. 添加说明（如需要）：
  ![Cursor 模型选择界面](/images/cursor-model-selection.png)
