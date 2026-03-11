# ClawHub 发布指南

## 📋 发布前准备

### 1. 登录 ClawHub

由于 ClawHub 需要浏览器验证登录，请按以下步骤操作：

#### 方法 A: 浏览器登录（推荐）

```bash
# 在终端执行
clawhub login
```

这会：
1. 自动打开浏览器
2. 跳转到 ClawHub 登录页面
3. 使用 GitHub 或邮箱登录
4. 授权 CLI 访问
5. 自动保存 token

#### 方法 B: 手动 Token 登录

1. 访问 https://clawhub.com/settings/tokens
2. 创建新的 API Token
3. 复制 Token
4. 执行：

```bash
clawhub login --token YOUR_TOKEN_HERE
```

---

### 2. 验证登录

```bash
clawhub whoami
```

成功的话会显示你的用户名。

---

## 🚀 发布技能

### 步骤 1: 进入技能目录

```bash
cd ~/.openclaw/workspace/skills/my-notes-skill
```

### 步骤 2: 发布技能

```bash
clawhub publish .
```

或指定路径：

```bash
clawhub publish ~/.openclaw/workspace/skills/my-notes-skill
```

---

## 📊 发布信息

发布时会填写以下信息：

| 字段 | 值 |
|------|------|
| **Name** | my-notes-skill |
| **Version** | 1.0.0 |
| **Description** | 在 Apple Notes 中创建笔记的 OpenClaw 技能 |
| **Category** | productivity |
| **Tags** | notes, apple-notes, memo, macos, 笔记 |
| **License** | MIT |
| **Homepage** | https://github.com/PaulCheng-bot/my-notes-skill |
| **Repository** | https://github.com/PaulCheng-bot/my-notes-skill |

---

## ✅ 发布后验证

### 1. 查看已发布技能

访问：https://clawhub.com/skills/my-notes-skill

或在 CLI 搜索：

```bash
clawhub search my-notes-skill
```

### 2. 测试安装

```bash
# 在另一台机器或新目录测试
clawhub install my-notes-skill
```

---

## 🔧 常见问题

### Q: 发布失败怎么办？

**检查清单**:
- [ ] 已登录 (`clawhub whoami`)
- [ ] SKILL.md 格式正确
- [ ] _meta.json 完整
- [ ] 网络连接正常

### Q: 如何更新技能？

```bash
# 修改版本号为 1.0.1
# 修改 SKILL.md 和 _meta.json

# 重新发布
clawhub publish .
```

### Q: 如何删除已发布的技能？

```bash
clawhub delete my-notes-skill
```

---

## 📝 快速命令参考

```bash
# 登录
clawhub login

# 验证登录
clawhub whoami

# 发布技能
clawhub publish <path>

# 搜索技能
clawhub search <query>

# 安装技能
clawhub install <slug>

# 更新技能
clawhub update <slug>

# 列出已安装
clawhub list

# 登出
clawhub logout
```

---

## 🎯 下一步

1. **执行登录**: `clawhub login`
2. **验证登录**: `clawhub whoami`
3. **发布技能**: `clawhub publish ~/.openclaw/workspace/skills/my-notes-skill`
4. **验证发布**: 访问 https://clawhub.com/skills/my-notes-skill

---

*最后更新：2026-03-11*
