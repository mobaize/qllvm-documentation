.. _quickstart:

快速开始
========

本指南将帮助您快速上手使用QLLVM编译器及其相关工具。

Quantum Circuit Composer
------------------------

欢迎使用 **Quantum Circuit Composer**！本插件旨在为量子编程提供一个集成开发环境，支持多种量子编程语言（QASM、Qiskit、QPanda、OriginIR、QCIS）和多编译器（QLLVM、Qiskit、QPanda），并实现远程/本地编译、QIR 模拟器运行、编译结果统计对比等功能。

简介
~~~~

Quantum Circuit Composer 是一款 Visual Studio Code 插件，主要功能包括：

- **多编译器支持**：可同时配置多个编译器（自研 QLLVM、IBM Qiskit、本源 QPanda），一键并行编译，并自动生成结果对比表格。
- **多前端输入**：支持 QASM、Qiskit Python 代码、QPanda Python 代码、OriginIR、QCIS 等多种输入格式，统一转换为 QASM 后进行编译。
- **远程/本地编译**：默认使用远程服务器编译（无需本地安装编译器），也可切换为本地编译。
- **QIR 模拟器**：直接在插件内运行 QIR 模拟器，查看测量结果统计。
- **统计对比**：编译完成后自动提取各编译器的门数、两比特门数、深度，并生成对比表格。
- **图形化设置**：通过设置面板管理编译器配置，轻松启用/禁用、编辑参数。

快速开始
~~~~~~~~

1. **安装插件**
   - 在 VSCode 扩展商店中搜索 "Quantum Circuit Composer" 并安装。
   - 安装后，状态栏会出现一个电路板图标，点击可打开设置面板。

2. **编写量子电路**
   - 新建一个文件，支持 `.qasm`（OpenQASM）、`.py`（Qiskit/QPanda 代码）、`.originir`、`.qcis` 等。
   - 例如，一个简单的 Bell 态 QASM 文件：

   .. code-block:: text

      OPENQASM 2.0;
      include "qelib1.inc";
      qreg q[2];
      creg c[2];
      h q[0];
      cx q[0],q[1];
      measure q[0] -> c[0];
      measure q[1] -> c[1];

3. **编译文件**
   - 右键单击文件，选择 **"编译当前量子电路文件"**。
   - 或打开设置面板，点击顶部的 **"▶ 选择文件进行编译"**。
   - 插件将使用已启用的所有编译器并行编译，并在输出通道中显示结果和统计对比表格。

4. **运行 QIR 模拟器**
   - 在设置面板的编译器列表中，找到 QLLVM 编译器，点击其右侧的 **"▶ 运行模拟器"** 按钮。
   - 在弹出的输入框中输入 shots（运行次数）和随机种子（可选）。
   - 模拟完成后，输出通道会显示测量结果统计。

编译器配置
~~~~~~~~~~~~

1. **打开设置面板**
   - 点击状态栏的 **"量子编译器"** 图标。
   - 或通过命令面板（`Ctrl+Shift+P`）执行 **"打开量子编译器设置"**。

2. **添加/编辑编译器**
   - 面板默认已包含三个编译器示例：**QLLVM Compiler（默认）**、**Qiskit（Python）**、**QPanda（Python）**。
   - 点击每个编译器右侧的 **"编辑"** 按钮，可以修改名称、启用状态、本地/远程模式、编译参数等。
   - 修改完成后点击 **"保存"**。

3. **参数说明**

   **QLLVM 编译器**
   - **设备类型** (`-qrt`)：NISQ（默认）或 FTQC
   - **后端类型** (`-qpu`)：QASM Backend（输出 .qasm）、本源量子（输出 .json）、天衍量子（输出 .py）、浙大量子（输出 .txt）
   - **优化等级**：O0（不优化）或 O1（推荐）
   - **基础门组**：仅 QASM Backend 有效，例如 `rx,ry,rz,h,cz`
   - **拓扑配置文件**：指定后端拓扑结构文件路径（非 QASM Backend 会自动使用内置拓扑）
   - **初始比特映射**：JSON 数组，如 `[0,1,2,3,4]`
   - **高级选项**：打印电路状态、打印 Pass 执行次数、详细输出、输出 MLIR/QIR 等
   - **QIR 模拟器运行参数**：Shots 和随机种子，用于一键运行

   **Qiskit 编译器**
   - **后端类型**：自定义（指定耦合图/基础门）、IBM Quantum 真实硬件、第三方平台 Scaleway
   - **优化等级**：0-3
   - **耦合图、基础门、初始布局**：自定义后端专用
   - **IBM 令牌和后端名**：IBM 后端专用
   - **第三方平台项目 ID、密钥、后端名**：第三方平台专用
   - **布局方法**：Trivial、Dense、Noise Adaptive、SABRE 等

   **QPanda 编译器**
   - **后端类型**：自定义（指定拓扑边/基础门）或本源真实芯片
   - **拓扑边、基础门、初始映射**：自定义后端专用
   - **芯片名称、API Key**：本源真实芯片专用
   - **仅分解模式**：只分解门而不进行路由和优化

4. **本地/远程模式**
   - 勾选 **"使用本地编译"** 时，插件会使用本地安装的编译器或 Python 解释器执行编译。
   - 不勾选时，使用远程服务器（默认 `http://42.51.100.38:64714`）进行编译，无需本地环境。
   - 远程服务器支持 QLLVM、Qiskit、QPanda 编译，且自动处理输入格式转换。

编译功能
~~~~~~~~~~

1. **编译当前文件**
   - 在编辑器中打开文件，右键选择 **"编译当前量子电路文件"**。
   - 插件会自动检测文件扩展名，并询问输入格式（若无法确定）。
   - 编译过程中，会显示进度条，并在输出通道实时输出编译日志。

2. **多编译器并行编译**
   - 所有启用的编译器都会被执行。
   - 编译完成后，每个编译器的输出（文件内容）会保存到源文件同目录，文件名格式为 `原文件名_后端_拓扑名_compiled_时间戳.后缀`。
   - 输出通道会显示每个编译器的成功/失败状态、输出文件路径，以及编译结果统计对比表格。

3. **统计对比**
   - 编译器的统计信息会从编译输出中提取：
   - **QLLVM**：从 `-circuit-state` 输出中提取最后一个统计块（优化后）的门数、两比特门数、深度。
   - **Qiskit/QPanda**：从输出中匹配 `STATS: total_gates=X, two_qubit_gates=Y, depth=Z` 行。
   - 对比表格以清晰的形式展示各编译器的门数、两比特门数和深度。

QIR 模拟器运行
~~~~~~~~~~~~~~~~

1. **运行方式**
   - 在设置面板的编译器列表中，找到已启用的 QLLVM 编译器。
   - 点击其右侧的 **"▶ 运行模拟器"** 按钮。
   - 输入运行次数（shots）和随机种子（可选）。

2. **运行流程**
   - 插件将当前活动编辑器中的电路代码（或弹出文件选择）发送到服务器。
   - 服务器端使用 QLLVM 生成 QIR 位码（.bc），再调用 qir-runner 执行模拟。
   - 模拟结果以 counts 字典形式返回（如 `{'00': 48, '11': 52}`），并显示在输出通道。

3. **本地运行**
   - 如果 QLLVM 编译器配置为 **"本地模式"**，且本地已安装 qllvm 和 qir-runner，则模拟会在本地执行。

多前端输入支持
~~~~~~~~~~~~~~~~

插件支持以下输入格式，并自动转换为 QASM 进行编译：

- **QASM** (`.qasm`)：标准 OpenQASM 2.0/3.0
- **Qiskit** (`.py`)：包含 `QuantumCircuit` 对象的 Python 脚本，默认变量名为 `qc`
- **QPanda** (`.py`)：包含 `QProg` 对象的 Python 脚本，默认变量名为 `prog`
- **OriginIR** (`.py`)：本源量子中间表示（兼容 QASM）
- **QCIS** (`.py`)：通用量子指令集（兼容 QASM）

> **注意**：对于 Qiskit 和 QPanda 代码，插件会尝试执行脚本并提取量子电路对象，因此请确保脚本中定义了 `qc` 或 `prog` 变量。该功能存在一定安全风险，请仅运行可信代码。

在编译时，插件会根据文件扩展名自动推断输入格式，也可在配置中手动指定。

常见问题
~~~~~~~~~~

1. **编译失败，提示"未生成输出文件"**

   **可能原因**：
   - 远程服务器不可达或未启动。
   - 本地编译器路径错误或权限不足。
   - 输入文件格式有误。

   **解决方法**：
   - 检查网络连接，确认服务器地址 `http://42.51.100.38:64714` 可访问。
   - 在设置面板中检查编译器配置，确保路径正确（本地模式）。
   - 检查电路代码是否有语法错误。

2. **统计对比表格未显示**

   确保编译器输出中包含统计信息：
   - QLLVM：需启用 **"打印电路状态"** 选项。
   - Qiskit/QPanda：需在模板中输出 `STATS:` 行（插件已默认实现）。
   - 如果使用远程编译，请确保服务器端返回的 `output` 字段包含统计信息（而非仅文件内容）。

3. **QIR 模拟器运行无结果**
   - 检查 QLLVM 编译器是否已启用。
   - 确保电路包含测量指令。
   - 查看输出通道中的错误信息，确认服务器端是否支持 qir-runner。

4. **本地编译找不到 Python 或 QLLVM**
   - 在编译器配置中指定正确的路径。
   - 确保 Python 环境中已安装所需的库（qiskit、pyqpanda3）。

5. **如何添加新的编译器？**
   - 在设置面板底部 **"添加新编译器"** 区域，选择类型并填写名称、路径等，保存即可。

6. **如何获取远程服务器上的拓扑文件？**
   - 插件内置了部分拓扑文件（wukong72.ini 等），在服务器端 `config` 目录下需放置对应文件。
   - 如需自定义，可提供 `.ini` 文件路径。

联系与反馈
~~~~~~~~~~~~

如果您在使用中遇到任何问题，或有改进建议，欢迎通过以下方式联系我们：

- 提交 GitHub Issue：[项目地址]
- 发送邮件至：[support@example.com]
- 在 VSCode 插件市场页面留言

感谢您的使用，愿量子计算之路畅通无阻！

Qcoder
------

**面向量子计算学习与开发的 VS Code 侧栏 AI 助手**

QCoder 将大模型对话嵌入编辑器侧栏，聚焦量子算法、量子电路与工具链问题，而不是通用闲聊。允许用户为阿里云、DeepSeek 或**自定义 SCNet 模型**配置自己的 API Key。

为什么需要 QCoder
~~~~~~~~~~~~~~~~~~

- 量子概念抽象，需要可追问、可举例的对话式解释。  
- 电路与 OpenQASM 等片段需要一键插入当前文件。  

核心功能
~~~~~~~~~~

智能对话
^^^^^^^^^^

- **多轮聊天**、**流式输出**、**暂停生成**、单条消息与代码块的**复制 / 插入**。  
- **深度思考**：在支持的模型链路上向 API 传递思考相关参数（具体行为因模型与服务商而异）。  
- **回复语言**：根据 'qcoder.uiLanguage'（界面语言）自动附加一条 system 指令，约束模型使用对应自然语言回答（如简体中文 / 繁体 / English）。

模型体系
^^^^^^^^^^

- **内置三条 SCNet 模型**：`MiniMax-M2.5`、`Qwen3-235B-A22B`、`DeepSeek-V3.2`，经超算互联网 OpenAI 兼容端点调用；**密钥写在扩展源码常量中**，用户不能在设置里修改（便于组织统一发证）。
- **自定义模型**：在侧栏「设置」里按服务商添加：`scnet` / 阿里云（Qwen）/ DeepSeek。其中 **自定义 SCNet** 使用用户可编辑的 `qcoder.scnetApiKey`；阿里云、DeepSeek 分别使用 `qcoder.qwenApiKey`、`qcoder.deepseekApiKey`。
- **模型选择器**：可通过 `qcoder.excludedModelKeys` 隐藏部分内置或自定义项。

默认选中内置模型 **MiniMax-M2.5**。

界面与引导
^^^^^^^^^^

- **界面语言**：English / 简体中文 / 繁體中文（`qcoder.uiLanguage`，默认 English）。  
- **快速开始**：首次进入可打开交互式引导（含 QLLVM 相关步骤：通过「另存为」下载说明文件，并将保存目录写入 `qcoder.qllvmInstallPath`）。  
- **聊天历史**：侧栏内浏览、加载、删除；会话快照由扩展持久化。

公式与 Markdown
^^^^^^^^^^^^^^^^

- 使用 **markdown-it**、**KaTeX**、**highlight.js** 等在 Webview 中渲染正文与代码块（见 `media/` 与 webpack 打包的 markdown 管线），便于展示量子符号与公式。

快速开始
~~~~~~~~

1. **安装**
   - 在 VS Code 扩展视图搜索安装，或使用 **Install from VSIX…** 安装组织分发的 `.vsix`。

2. **配置 API Key（按你实际使用的模型）**

   打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`）：
   - **QCoder: 设置 QCoder Qwen API Key**：阿里云百炼（自定义 Qwen 模型）
   - **QCoder: 设置 QCoder DeepSeek API Key**：DeepSeek（自定义）
   - **QCoder: 设置 QCoder SCNet API Key**：仅用于**自定义添加的 SCNet 模型**，与内置三条官方模型无关

   仅使用**内置三条 SCNet 模型**时，可以不配置 Qwen / DeepSeek / 自定义 SCNet Key。

3. **打开聊天**
   - 点击活动栏 **QCoder** 图标打开侧栏聊天，或运行 **QCoder: 与量子编程小助手聊天**。

4. **侧栏设置**
   - 标题栏或界面内可打开 **设置**：管理自定义模型列表、界面语言、以及（在支持的构建中）与模型测试相关的 Key 写入。

命令一览
~~~~~~~~~~

- **与量子编程小助手聊天**：打开聊天（侧栏 / 面板）
- **快速开始**：打开引导（带多语言标题栏入口）
- **历史记录 / 新建聊天 / 设置**：侧栏聊天视图常用操作
- **设置 QCoder Qwen / DeepSeek / SCNet API Key**：写入对应用户级密钥（SCNet 项仅自定义模型）

（完整列表以 `package.json` `contributes.commands` 为准。）

主要设置项
~~~~~~~~~~~~

* `qcoder.qwenApiKey` - 阿里云百炼 API Key（自定义 Qwen）
* `qcoder.deepseekApiKey` - DeepSeek API Key（自定义）
* `qcoder.scnetApiKey` - 自定义 SCNet 模型专用；内置三条模型不使用此项
* `qcoder.customModels` - 自定义模型列表（provider + modelId + label）
* `qcoder.excludedModelKeys` - 在下拉中隐藏的模型键
* `qcoder.uiLanguage` - `en` / `zh-CN` / `zh-TW`
* `qcoder.qllvmInstallPath` - QLLVM 相关说明保存目录（快速开始流程写入）
* `qcoder.llmGatewayTimeoutSec` - 经内置网关转发时的超时（秒）
* `qcoder.logGatewayPayload` - 是否在输出面板记录网关请求（密钥脱敏）
* `qcoder.debugChatUiSync` - 是否记录聊天与网关字段调试信息

项目结构（心智模型）
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   ┌──────────────────┐     postMessage      ┌─────────────────────┐
   │  Webview (聊天)   │ ◀──────────────────▶ │  Extension Host      │
   │  UI / i18n / MD   │                      │  命令 / 配置 / fetch  │
   └──────────────────┘                      └──────────┬──────────┘
                                                    │
                       ┌───────────────────────────────┼───────────────────────────────┐
                       ▼                               ▼                               ▼
              （可选）QCoder 网关                 SCNet / 阿里云 / DeepSeek           OpenAI 兼容 API                         

- **`src/extension.ts`**：激活、Webview 提供、消息路由、流式聊天、自定义模型保存、QLLVM 下载对话框等。  
- **`src/webview/`**：`index.html` + `js/app.js`、`i18n.js` 等与 UI 相关逻辑。  
- **`src/qcoderCustomModel.ts`**：自定义模型校验与列表解析（与内置模型 ID 冲突检测）。  
- **`dist/`**：Webpack 打出的扩展入口；**`media/`** 为 KaTeX CSS 等与 Markdown 相关的静态资源。

开发与构建
~~~~~~~~~~~~

.. code-block:: bash

   npm install
   npm run compile    # 生成 dist/extension.js
   npm run watch      # 监听编译
   npm run package    # 生产打包
   npm run lint
   npm run test       # 需本机 VS Code 测试环境

按 **F5** 可在扩展开发宿主中调试。

常见问题
~~~~~~~~~~

- **内置模型提示未配置密钥**：当前构建的 `QCODER_BUILTIN_SCNET_API_KEY` 为空或未更新，需由发行方在源码中填入后重新打包。  
- **自定义 SCNet 报错**：检查是否已设置 **QCoder: 设置 QCoder SCNet API Key** 或在添加模型时填写密钥。  
- **历史记录**：由扩展全局状态等机制持久化，具体条数与策略以当前版本实现为准。

版本
~~~~~

当前版本见 `package.json` 的 `version`。详细变更可维护于 `CHANGELOG.md`。

许可证
~~~~~~~

MIT，见 [LICENSE.md](LICENSE.md)。

**让量子编程对话留在编辑器旁，配置清晰、路径可控。**
