# QCoder - 量子编程小助手

**面向量子计算学习与开发的 VS Code 侧栏 AI 助手**

QCoder 将大模型对话嵌入编辑器侧栏，聚焦量子算法、量子电路与工具链问题，而不是通用闲聊。允许用户为阿里云、DeepSeek 或**自定义 SCNet 模型**配置自己的 API Key。

---

## 为什么需要 QCoder

- 量子概念抽象，需要可追问、可举例的对话式解释。  
- 电路与 OpenQASM 等片段需要一键插入当前文件。  
---

## 核心功能

### 智能对话

- **多轮聊天**、**流式输出**、**暂停生成**、单条消息与代码块的**复制 / 插入**。  
- **深度思考**：在支持的模型链路上向 API 传递思考相关参数（具体行为因模型与服务商而异）。  
- **回复语言**：根据 `qcoder.uiLanguage`（界面语言）自动附加一条 system 指令，约束模型使用对应自然语言回答（如简体中文 / 繁体 / English）。

### 模型体系

| 类型 | 说明 |
|------|------|
| **内置三条 SCNet 模型** | `MiniMax-M2.5`、`Qwen3-235B-A22B`、`DeepSeek-V3.2`，经超算互联网 OpenAI 兼容端点调用；**密钥写在扩展源码常量中**，用户不能在设置里修改（便于组织统一发证）。 |
| **自定义模型** | 在侧栏「设置」里按服务商添加：`scnet` / 阿里云（Qwen）/ DeepSeek。其中 **自定义 SCNet** 使用用户可编辑的 `qcoder.scnetApiKey`；阿里云、DeepSeek 分别使用 `qcoder.qwenApiKey`、`qcoder.deepseekApiKey`。 |
| **模型选择器** | 可通过 `qcoder.excludedModelKeys` 隐藏部分内置或自定义项。 |

默认选中内置模型 **MiniMax-M2.5**。

### 界面与引导

- **界面语言**：English / 简体中文 / 繁體中文（`qcoder.uiLanguage`，默认 English）。  
- **快速开始**：首次进入可打开交互式引导（含 QLLVM 相关步骤：通过「另存为」下载说明文件，并将保存目录写入 `qcoder.qllvmInstallPath`）。  
- **聊天历史**：侧栏内浏览、加载、删除；会话快照由扩展持久化。

### 公式与 Markdown

- 使用 **markdown-it**、**KaTeX**、**highlight.js** 等在 Webview 中渲染正文与代码块（见 `media/` 与 webpack 打包的 markdown 管线），便于展示量子符号与公式。

---
---

## 快速开始

### 1. 安装

- 在 VS Code 扩展视图搜索安装，或使用 **Install from VSIX…** 安装组织分发的 `.vsix`。

### 2. 配置 API Key（按你实际使用的模型）

打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`）：

| 命令 | 用途 |
|------|------|
| **QCoder: 设置 QCoder Qwen API Key** | 阿里云百炼（自定义 Qwen 模型） |
| **QCoder: 设置 QCoder DeepSeek API Key** | DeepSeek（自定义） |
| **QCoder: 设置 QCoder SCNet API Key** | 仅用于**自定义添加的 SCNet 模型**，与内置三条官方模型无关 |

仅使用**内置三条 SCNet 模型**时，可以不配置 Qwen / DeepSeek / 自定义 SCNet Key。

### 3. 打开聊天

- 点击活动栏 **QCoder** 图标打开侧栏聊天，或运行 **QCoder: 与量子编程小助手聊天**。

### 4. 侧栏设置

标题栏或界面内可打开 **设置**：管理自定义模型列表、界面语言、以及（在支持的构建中）与模型测试相关的 Key 写入。

---

## 命令一览

| 命令 | 说明 |
|------|------|
| 与量子编程小助手聊天 | 打开聊天（侧栏 / 面板） |
| 快速开始 | 打开引导（带多语言标题栏入口） |
| 历史记录 / 新建聊天 / 设置 | 侧栏聊天视图常用操作 |
| 设置 QCoder Qwen / DeepSeek / SCNet API Key | 写入对应用户级密钥（SCNet 项仅自定义模型） |

（完整列表以 `package.json` `contributes.commands` 为准。）

---

## 主要设置项（`settings.json`）

| 键 | 作用 |
|----|------|
| `qcoder.qwenApiKey` | 阿里云百炼 API Key（自定义 Qwen） |
| `qcoder.deepseekApiKey` | DeepSeek API Key（自定义） |
| `qcoder.scnetApiKey` | 自定义 SCNet 模型专用；**内置三条模型不使用此项** |
| `qcoder.customModels` | 自定义模型列表（provider + modelId + label） |
| `qcoder.excludedModelKeys` | 在下拉中隐藏的模型键 |
| `qcoder.uiLanguage` | `en` / `zh-CN` / `zh-TW` |
| `qcoder.qllvmInstallPath` | QLLVM 相关说明保存目录（快速开始流程写入） |
| `qcoder.llmGatewayTimeoutSec` | 经内置网关转发时的超时（秒） |
| `qcoder.logGatewayPayload` | 是否在输出面板记录网关请求（密钥脱敏） |
| `qcoder.debugChatUiSync` | 是否记录聊天与网关字段调试信息 |


---

---

## 项目结构（心智模型）

```
┌──────────────────┐     postMessage      ┌─────────────────────┐
│  Webview (聊天)   │ ◀──────────────────▶ │  Extension Host      │
│  UI / i18n / MD   │                      │  命令 / 配置 / fetch  │
└──────────────────┘                      └──────────┬──────────┘
                                                       │
                       ┌───────────────────────────────┼───────────────────────────────┐
                       ▼                               ▼                               ▼
              （可选）QCoder 网关                 SCNet / 阿里云 / DeepSeek           OpenAI 兼容 API                         
```

- **`src/extension.ts`**：激活、Webview 提供、消息路由、流式聊天、自定义模型保存、QLLVM 下载对话框等。  
- **`src/webview/`**：`index.html` + `js/app.js`、`i18n.js` 等与 UI 相关逻辑。  
- **`src/qcoderCustomModel.ts`**：自定义模型校验与列表解析（与内置模型 ID 冲突检测）。  
- **`dist/`**：Webpack 打出的扩展入口；**`media/`** 为 KaTeX CSS 等与 Markdown 相关的静态资源。

---

## 开发与构建

```bash
npm install
npm run compile    # 生成 dist/extension.js
npm run watch      # 监听编译
npm run package    # 生产打包
npm run lint
npm run test       # 需本机 VS Code 测试环境
```

按 **F5** 可在扩展开发宿主中调试。

---

## 常见问题

- **内置模型提示未配置密钥**：当前构建的 `QCODER_BUILTIN_SCNET_API_KEY` 为空或未更新，需由发行方在源码中填入后重新打包。  
- **自定义 SCNet 报错**：检查是否已设置 **QCoder: 设置 QCoder SCNet API Key** 或在添加模型时填写密钥。  
- **历史记录**：由扩展全局状态等机制持久化，具体条数与策略以当前版本实现为准。

---

## 版本

当前版本见 `package.json` 的 `version`。详细变更可维护于 `CHANGELOG.md`。

---

## 许可证

MIT，见 [LICENSE.md](LICENSE.md)。

---

**让量子编程对话留在编辑器旁，配置清晰、路径可控。**
