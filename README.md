# My Notes Skill for OpenClaw 📝

在 Mac 的 Apple Notes 应用中创建新笔记的 OpenClaw 技能。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://docs.openclaw.ai)
[![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey)](https://apple.com/macos)

---

## ✨ 功能特性

- ✅ 在 Apple Notes 中创建新笔记
- ✅ 自动添加时间戳
- ✅ 支持标签分类
- ✅ 支持自定义标题
- ✅ 使用 memo CLI 工具
- ✅ 无需 API 密钥

---

## 🚀 快速开始

### 前置要求

- macOS 10.15+
- [memo CLI](https://github.com/nickoneill/memo)
- OpenClaw

### 安装 memo CLI

```bash
brew install memo
```

### 安装技能

```bash
# 克隆到 OpenClaw 技能目录
git clone https://github.com/paulcheng/my-notes-skill.git ~/.openclaw/workspace/skills/my-notes-skill

# 重启 OpenClaw Gateway
openclaw gateway restart
```

---

## 📖 使用方法

### 基本用法

在 OpenClaw 聊天中说：

```
记录笔记：今天下午买了咖啡，花了 35 元
```

### 更多示例

```
记一下：明天上午 10 点开会
保存：这个想法很重要 - 开发一个自动化笔记技能
记录笔记 [工作会议]：明天上午 10 点开会，准备 Q2 报告
```

### 触发词

- 记录笔记
- 记一下
- 保存
- 添加到笔记
- create note
- add to notes
- remember this

---

## 📋 输出示例

**User**: 记录笔记：今天下午买了咖啡，花了 35 元

**Assistant**: 
```
✅ 已创建笔记："今天下午买了咖啡，花了 35 元"
📁 位置：Apple Notes
🕐 时间：2026-03-11 16:30
```

---

## ⚙️ 配置说明

### 默认配置

编辑 `config.json`:

```json
{
  "defaultFolder": "Notes",
  "addTimestamp": true,
  "addTags": true
}
```

### 配置项说明

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `defaultFolder` | 默认笔记文件夹 | `"Notes"` |
| `addTimestamp` | 自动添加时间戳 | `true` |
| `addTags` | 支持标签 | `true` |

---

## 🔧 开发

### 项目结构

```
my-notes-skill/
├── SKILL.md              # 技能描述和触发条件
├── _meta.json            # 元数据
├── config.json           # 配置文件
├── README.md             # 本文件
└── scripts/              # 脚本目录（可选）
```

### 本地测试

```bash
# 测试 memo CLI
memo notes -fl

# 创建测试笔记
memo notes -a -f Notes
```

---

## 📚 文档

- [SKILL.md](./SKILL.md) - 完整技能文档
- [OpenClaw 文档](https://docs.openclaw.ai)
- [memo CLI 文档](https://github.com/nickoneill/memo)

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](./LICENSE) 文件了解详情。

---

## 👤 作者

**Paul Cheng**

- GitHub: [@paulcheng](https://github.com/paulcheng)
- Email: pcclawp1@163.com

---

## 🙏 致谢

- [OpenClaw](https://github.com/openclaw/openclaw) - AI 助手框架
- [memo](https://github.com/nickoneill/memo) - Apple Notes CLI 工具

---

## 📝 更新日志

### v1.0.0 (2026-03-11)

- ✅ 初始版本发布
- ✅ 支持创建笔记
- ✅ 支持标签和标题
- ✅ 自动时间戳

---

## 📞 支持

如有问题，请：

1. 查看 [常见问题](#常见问题)
2. 提交 [Issue](https://github.com/paulcheng/my-notes-skill/issues)
3. 联系作者

---

## ❓ 常见问题

### Q: 笔记保存在哪里？

A: 保存在 Mac 的 Apple Notes 应用中，可通过 Notes App 查看。

### Q: 可以在 iPhone 上查看吗？

A: 可以，如果开启了 iCloud 同步，笔记会自动同步到所有设备。

### Q: 如何搜索笔记？

A: 在 Notes App 中使用搜索功能。

### Q: 支持 Markdown 格式吗？

A: 支持，memo CLI 会保留 Markdown 格式。

---

<div align="center">

**⭐ 如果这个技能对你有帮助，请给个 Star！**

Made with ❤️ by Paul Cheng

</div>
