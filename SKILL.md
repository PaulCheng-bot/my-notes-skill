---
name: my-notes-skill
version: 1.0.0
description: Create notes in Apple Notes on Mac. Use when user asks to record notes, save important information, or create reminders.
author: Paul Cheng
tags:
  - notes
  - apple-notes
  - memo
  - recording
license: MIT
---

# My Notes Skill 📝

在 Mac 的 Apple Notes 应用中创建新笔记。当你需要记录重要事项、想法或信息时使用。

## 何时使用

- 用户说"记录笔记"、"记一下"、"保存这个"
- 用户需要记录重要信息
- 用户想要创建待办事项或提醒
- 用户需要保存想法或灵感

## 触发词

```
记录笔记
记一下
保存
添加到笔记
create note
add to notes
remember this
```

## 使用方法

### 基本用法

```
记录笔记：今天天气很好，去公园散步了
记一下：明天上午 10 点开会
保存：这个想法很重要 - 开发一个自动化笔记技能
```

### 带标题

```
记录笔记 [工作会议]：明天上午 10 点开会，准备 Q2 报告
```

### 带标签

```
记录笔记 #重要 #工作：明天上午 10 点开会
```

## 示例

**User**: 记录笔记：今天下午买了咖啡，花了 35 元

**Assistant**: 
✅ 已创建笔记："今天下午买了咖啡，花了 35 元"
📁 位置：Apple Notes
🕐 时间：2026-03-11 16:30

---

**User**: 记一下：明天上午 10 点开会，准备 Q2 报告

**Assistant**: 
✅ 已创建笔记："明天上午 10 点开会，准备 Q2 报告"
📁 位置：Apple Notes
🕐 时间：2026-03-11 16:30

---

**User**: 保存这个想法：开发一个自动化笔记技能，可以用语音输入

**Assistant**: 
✅ 已创建笔记："开发一个自动化笔记技能，可以用语音输入"
📁 位置：Apple Notes
🕐 时间：2026-03-11 16:30

## 功能特性

| 功能 | 说明 | 状态 |
|------|------|------|
| 创建新笔记 | 每次写入生成新 Note | ✅ |
| 自动时间戳 | 记录创建时间 | ✅ |
| 支持标签 | 使用 #标签 分类 | ✅ |
| 支持标题 | 使用 [标题] 格式 | ✅ |
| 多行内容 | 支持换行和格式 | ✅ |
| 搜索笔记 | 在 Notes 中搜索 | ✅ |

## 配置说明

### 默认配置

```json
{
  "defaultFolder": "Notes",
  "addTimestamp": true,
  "addTags": true
}
```

### 自定义配置

编辑 `config.json`:

```json
{
  "defaultFolder": "Work Notes",
  "addTimestamp": true,
  "addTags": true,
  "defaultTags": ["openclaw", "auto"]
}
```

## 命令参考

### memo CLI 命令

```bash
# 创建新笔记
memo create "笔记内容"

# 列出所有笔记
memo list

# 查看笔记
memo show <id>

# 搜索笔记
memo search "关键词"

# 删除笔记
memo delete <id>
```

## 输出格式

成功创建笔记后，返回以下格式：

```
✅ 已创建笔记："[笔记内容]"
📁 位置：Apple Notes
🕐 时间：YYYY-MM-DD HH:mm
🏷️ 标签：#tag1 #tag2 (如有)
```

## 错误处理

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| memo 未找到 | 未安装 memo CLI | `brew install memo` |
| 权限错误 | Notes 权限未开启 | 系统设置 → 隐私 → Notes |
| 内容为空 | 未提供笔记内容 | 提醒用户提供内容 |

## 依赖项

- **memo CLI**: `brew install memo`
- **macOS**: 10.15+
- **Apple Notes**: 系统自带

## 安装 memo CLI

```bash
# 使用 Homebrew 安装
brew install memo

# 验证安装
memo --version

# 测试
memo create "测试笔记"
```

## 隐私说明

- 笔记存储在本地 Apple Notes
- 不上传到外部服务器
- 同步通过 iCloud（如开启）
- 无数据收集

## 常见问题

### Q: 笔记保存在哪里？

A: 保存在 Mac 的 Apple Notes 应用中，可通过 Notes App 查看。

### Q: 可以在 iPhone 上查看吗？

A: 可以，如果开启了 iCloud 同步，笔记会自动同步到所有设备。

### Q: 如何搜索笔记？

A: 在 Notes App 中使用搜索功能，或使用 `memo search "关键词"`。

### Q: 支持 Markdown 格式吗？

A: 支持，memo CLI 会保留 Markdown 格式。

### Q: 如何删除笔记？

A: 在 Notes App 中手动删除，或使用 `memo delete <id>`。

## 相关技能

- [apple-reminders](../apple-reminders/) - 管理提醒事项
- [apple-notes](../apple-notes/) - 完整的 Notes 管理

## 更新日志

### v1.0.0 (2026-03-11)

- ✅ 初始版本
- ✅ 支持创建笔记
- ✅ 支持标签和标题
- ✅ 自动时间戳

## License

MIT

## 作者

Paul Cheng

## 参考链接

- [memo CLI GitHub](https://github.com/nickoneill/memo)
- [Apple Notes](https://support.apple.com/notes)
- [OpenClaw 文档](https://docs.openclaw.ai)
