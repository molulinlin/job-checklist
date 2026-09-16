# JobPulse v9 Firebase 发布设置

v9 使用 Firebase 的免费套餐提供“同步 ID + 密码”账户和按用户隔离的个人档案。公共 `company_database.json` 仍由 GitHub Pages 发布，不写入 Firebase。

## 发布前必须完成

1. 在 Firebase 项目 `find-job---checklist` 的 Authentication 中启用 `Email/Password` 登录方式。项目当前接口返回 `PASSWORD_LOGIN_DISABLED`，未启用前用户无法注册。
2. 在 Firestore Database 的 Rules 页面，用 `firestore.rules` 的完整内容替换并发布规则。
3. 确认 Firestore 已创建为 Native mode 数据库。v9 会为每位用户写入唯一位置：`users/{uid}/private/state`。
4. 推送 v9 页面后，用一个新的测试同步 ID 注册；用第二个浏览器或设备登录同一同步 ID，确认只读到自己的档案。

## 账户模型

- 用户界面只暴露“同步 ID + 密码”。前端把同步 ID 标准化后转换为项目内认证邮箱，例如 `momo2026@jobpulse.local`；用户不需要提供真实邮箱。
- 密码由 Firebase Authentication 保存与校验，页面不保存明文密码。
- 登录会话的刷新令牌保存在该设备浏览器的 `localStorage` 中；退出时只清除此会话记录，不清除当前设备的本地投递数据。
- 不提供密码找回，因为同步 ID 不绑定真实邮箱。用户应自行保存同步 ID 和密码；如需要找回能力，后续版本必须增加已验证邮箱或手机号。

## 数据迁移

旧版 Gist 同步入口仍保留为“旧版同步码迁移”。已有用户应先在旧设备确认本地数据完整，再注册 v9 账户；首次登录会询问是否将该设备的本地投递数据迁入新账户。迁移完成并在另一台设备验证前，不要删除旧 Gist 或清空原浏览器数据。

## 免费范围和限制

Email/Password 认证与 Firestore 的免费套餐适合 JobPulse 当前个人求职场景，但免费额度和条款会随服务商调整。v9 以单账户一份状态文档保存数据，并使用约 5 分钟一次的变更检查；它不是无限并发或强实时协同系统。
