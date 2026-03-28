.. _quickstart_en:

Quickstart
==========

This guide will help you quickly get started with the QLLVM compiler and its related tools.

Quantum Circuit Composer
------------------------

Welcome to **Quantum Circuit Composer**! This plugin aims to provide an integrated development environment for quantum programming, supporting multiple quantum programming languages (QASM, Qiskit, QPanda, OriginIR, QCIS) and multiple compilers (QLLVM, Qiskit, QPanda), and implementing remote/local compilation, QIR simulator running, compilation result statistical comparison and other functions.

Introduction
~~~~~~~~~~~~

Quantum Circuit Composer is a Visual Studio Code plugin with the following main features:

- **Multi-compiler support**: Configure multiple compilers (self-developed QLLVM, IBM Qiskit, Origin QPanda) simultaneously, compile in parallel with one click, and automatically generate result comparison tables.
- **Multi-frontend input**: Supports QASM, Qiskit Python code, QPanda Python code, OriginIR, QCIS and other input formats, which are uniformly converted to QASM for compilation.
- **Remote/local compilation**: Uses remote server compilation by default (no local compiler installation required), and can also be switched to local compilation.
- **QIR simulator**: Run QIR simulator directly in the plugin to view measurement result statistics.
- **Statistical comparison**: Automatically extracts the number of gates, two-qubit gates, and depth from each compiler after compilation, and generates a comparison table.
- **Graphical settings**: Manage compiler configurations through the settings panel, easily enable/disable, and edit parameters.

Quick Start
~~~~~~~~~~~

1. **Install the plugin**
   - Search for "Quantum Circuit Composer" in the VSCode extension store and install it.
   - After installation, a circuit board icon will appear in the status bar, click to open the settings panel.

2. **Write quantum circuit**
   - Create a new file, supporting `.qasm` (OpenQASM), `.py` (Qiskit/QPanda code), `.originir`, `.qcis`, etc.
   - For example, a simple Bell state QASM file:

   .. code-block:: text

      OPENQASM 2.0;
      include "qelib1.inc";
      qreg q[2];
      creg c[2];
      h q[0];
      cx q[0],q[1];
      measure q[0] -> c[0];
      measure q[1] -> c[1];

3. **Compile file**
   - Right-click on the file and select **"Compile current quantum circuit file"**.
   - Or open the settings panel and click **"▶ Select file to compile"** at the top.
   - The plugin will use all enabled compilers to compile in parallel and display results and statistical comparison tables in the output channel.

4. **Run QIR simulator**
   - In the compiler list of the settings panel, find the QLLVM compiler and click the **"▶ Run simulator"** button on its right.
   - Enter shots (number of runs) and random seed (optional) in the pop-up input box.
   - After simulation is complete, the output channel will display measurement result statistics.

Compiler Configuration
~~~~~~~~~~~~~~~~~~~~~~

1. **Open settings panel**
   - Click the **"Quantum Compiler"** icon in the status bar.
   - Or execute **"Open quantum compiler settings"** through the command palette (`Ctrl+Shift+P`).

2. **Add/edit compiler**
   - The panel already includes three compiler examples by default: **QLLVM Compiler (default)**, **Qiskit (Python)**, **QPanda (Python)**.
   - Click the **"Edit"** button on the right of each compiler to modify the name, enable status, local/remote mode, compilation parameters, etc.
   - Click **"Save"** after modification.

3. **Parameter explanation**

   **QLLVM compiler**
   - **Device type** (`-qrt`): NISQ (default) or FTQC
   - **Backend type** (`-qpu`): QASM Backend (output .qasm), Origin Quantum (output .json), Tianyan Quantum (output .py), Zhejiang University Quantum (output .txt)
   - **Optimization level**: O0 (no optimization) or O1 (recommended)
   - **Basic gate set**: Only valid for QASM Backend, for example `rx,ry,rz,h,cz`
   - **Topology configuration file**: Specify the backend topology structure file path (non-QASM Backend will automatically use built-in topology)
   - **Initial qubit mapping**: JSON array, such as `[0,1,2,3,4]`
   - **Advanced options**: Print circuit state, print Pass execution count, detailed output, output MLIR/QIR, etc.
   - **QIR simulator running parameters**: Shots and random seed for one-click running

   **Qiskit compiler**
   - **Backend type**: Custom (specify coupling graph/basic gates), IBM Quantum real hardware, third-party platform Scaleway
   - **Optimization level**: 0-3
   - **Coupling graph, basic gates, initial layout**: Custom backend specific
   - **IBM token and backend name**: IBM backend specific
   - **Third-party platform project ID, key, backend name**: Third-party platform specific
   - **Layout method**: Trivial, Dense, Noise Adaptive, SABRE, etc.

   **QPanda compiler**
   - **Backend type**: Custom (specify topology edges/basic gates) or Origin real chip
   - **Topology edges, basic gates, initial mapping**: Custom backend specific
   - **Chip name, API Key**: Origin real chip specific
   - **Decomposition only mode**: Only decompose gates without routing and optimization

4. **Local/remote mode**
   - When **"Use local compilation"** is checked, the plugin will use the locally installed compiler or Python interpreter to execute compilation.
   - When not checked, it uses the remote server (default `http://42.51.100.38:64714`) for compilation, no local environment required.
   - The remote server supports QLLVM, Qiskit, QPanda compilation, and automatically handles input format conversion.

Compilation Features
~~~~~~~~~~~~~~~~~~~~

1. **Compile current file**
   - Open the file in the editor, right-click and select **"Compile current quantum circuit file"**.
   - The plugin will automatically detect the file extension and ask for input format if it cannot be determined.
   - During compilation, a progress bar will be displayed, and compilation logs will be output in real-time in the output channel.

2. **Multi-compiler parallel compilation**
   - All enabled compilers will be executed.
   - After compilation is complete, each compiler's output (file content) will be saved to the same directory as the source file, with the file name format `original filename_backend_topology name_compiled_timestamp.suffix`.
   - The output channel will display the success/failure status of each compiler, output file path, and compilation result statistical comparison table.

3. **Statistical comparison**
   - Compiler statistical information will be extracted from the compilation output:
   - **QLLVM**: Extract the last statistical block (after optimization) from the `-circuit-state` output, including the number of gates, two-qubit gates, and depth.
   - **Qiskit/QPanda**: Match the `STATS: total_gates=X, two_qubit_gates=Y, depth=Z` line from the output.
   - The comparison table clearly displays the number of gates, two-qubit gates, and depth of each compiler.

QIR Simulator Running
~~~~~~~~~~~~~~~~~~~~~~

1. **Running method**
   - In the compiler list of the settings panel, find the enabled QLLVM compiler.
   - Click the **"▶ Run simulator"** button on its right.
   - Enter the number of runs (shots) and random seed (optional).

2. **Running process**
   - The plugin sends the circuit code in the current active editor (or pops up file selection) to the server.
   - The server uses QLLVM to generate QIR bitcode (.bc), then calls qir-runner to execute the simulation.
   - The simulation result is returned as a counts dictionary (such as `{'00': 48, '11': 52}`) and displayed in the output channel.

3. **Local running**
   - If the QLLVM compiler is configured in **"local mode"** and qllvm and qir-runner are installed locally, the simulation will be executed locally.

Multi-frontend Input Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The plugin supports the following input formats and automatically converts them to QASM for compilation:

- **QASM** (`.qasm`): Standard OpenQASM 2.0/3.0
- **Qiskit** (`.py`): Python script containing `QuantumCircuit` object, default variable name is `qc`
- **QPanda** (`.py`): Python script containing `QProg` object, default variable name is `prog`
- **OriginIR** (`.py`): Origin Quantum intermediate representation (compatible with QASM)
- **QCIS** (`.py`): Universal quantum instruction set (compatible with QASM)

> **Note**: For Qiskit and QPanda code, the plugin will try to execute the script and extract the quantum circuit object, so please ensure that the script defines `qc` or `prog` variables. This feature has certain security risks, please only run trusted code.

During compilation, the plugin will automatically infer the input format based on the file extension, and can also be manually specified in the configuration.

Common Issues
~~~~~~~~~~~~~

1. **Compilation failed,提示"No output file generated"**

   **Possible reasons**:
   - Remote server is unreachable or not started.
   - Local compiler path is incorrect or insufficient permissions.
   - Input file format is incorrect.

   **Solution**:
   - Check network connection, confirm server address `http://42.51.100.38:64714` is accessible.
   - Check compiler configuration in the settings panel to ensure the path is correct (local mode).
   - Check if the circuit code has syntax errors.

2. **Statistical comparison table not displayed**

   Ensure the compiler output contains statistical information:
   - QLLVM: Need to enable **"Print circuit state"** option.
   - Qiskit/QPanda: Need to output `STATS:` line in the template (default implementation by the plugin).
   - If using remote compilation, ensure the `output` field returned by the server contains statistical information (not just file content).

3. **QIR simulator running no results**
   - Check if the QLLVM compiler is enabled.
   - Ensure the circuit contains measurement instructions.
   - Check the error information in the output channel to confirm whether the server supports qir-runner.

4. **Local compilation cannot find Python or QLLVM**
   - Specify the correct path in the compiler configuration.
   - Ensure the Python environment has the required libraries installed (qiskit, pyqpanda3).

5. **How to add a new compiler?**
   - In the **"Add new compiler"** area at the bottom of the settings panel, select the type and fill in the name, path, etc., then save.

6. **How to obtain topology files on the remote server?**
   - The plugin has built-in some topology files (wukong72.ini, etc.), which need to be placed in the `config` directory on the server side.
   - For customization, you can provide the `.ini` file path.

Contact and Feedback
~~~~~~~~~~~~~~~~~~~~

If you encounter any problems during use or have improvement suggestions, please contact us through the following methods:

- Submit GitHub Issue: [Project address]
- Send email to: [support@example.com]
- Leave a message on the VSCode plugin market page

Thank you for your use, may your quantum computing journey be smooth!

Qcoder
------

**VS Code Sidebar AI Assistant for Quantum Computing Learning and Development**

QCoder embeds large model dialogue into the editor sidebar, focusing on quantum algorithms, quantum circuits, and toolchain issues, rather than general chat. It allows users to configure their own API Key for Alibaba Cloud, DeepSeek, or **custom SCNet models**.

Why QCoder is Needed
~~~~~~~~~~~~~~~~~~~~

- Quantum concepts are abstract and require conversational explanations that can be asked and exemplified.  
- Circuit and OpenQASM fragments need to be inserted into the current file with one click.  

Core Features
~~~~~~~~~~~~~

Intelligent Dialogue
^^^^^^^^^^^^^^^^^^^^

- **Multi-turn chat**, **streaming output**, **pause generation**, **copy / insert** of single messages and code blocks.  
- **Deep thinking**: Pass thinking-related parameters to the API on supported model links (specific behavior varies by model and service provider).  
- **Reply language**: Automatically attach a system instruction based on `qcoder.uiLanguage` (interface language), constraining the model to answer in the corresponding natural language (such as Simplified Chinese / Traditional Chinese / English).

Model System
^^^^^^^^^^^^

- **Three built-in SCNet models**: `MiniMax-M2.5`, `Qwen3-235B-A22B`, `DeepSeek-V3.2`, called through the supercomputing internet OpenAI compatible endpoint; **keys are written in extension source code constants**, users cannot modify them in settings (facilitating unified certification by the organization).
- **Custom models**: Add by service provider in the sidebar "Settings": `scnet` / Alibaba Cloud (Qwen) / DeepSeek. Among them, **custom SCNet** uses the user-editable `qcoder.scnetApiKey`; Alibaba Cloud and DeepSeek use `qcoder.qwenApiKey` and `qcoder.deepseekApiKey` respectively.
- **Model selector**: Some built-in or custom items can be hidden through `qcoder.excludedModelKeys`.

The built-in model **MiniMax-M2.5** is selected by default.

Interface and Guidance
^^^^^^^^^^^^^^^^^^^^^^

- **Interface language**: English / Simplified Chinese / Traditional Chinese (`qcoder.uiLanguage`, default English).  
- **Quick start**: Interactive guidance can be opened when entering for the first time (including QLLVM-related steps: download the instruction file through "Save As" and write the save directory to `qcoder.qllvmInstallPath`).  
- **Chat history**: Browse, load, and delete in the sidebar; session snapshots are persisted by the extension.

Formulas and Markdown
^^^^^^^^^^^^^^^^^^^^^^

- Use **markdown-it**, **KaTeX**, **highlight.js**, etc. to render text and code blocks in Webview (see `media/` and webpack-packaged markdown pipeline), making it easy to display quantum symbols and formulas.

Quick Start
~~~~~~~~~~~

1. **Installation**
   - Search and install in the VS Code extension view, or use **Install from VSIX…** to install the `.vsix` distributed by the organization.

2. **Configure API Key (according to the model you actually use)**

   Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):
   - **QCoder: Set QCoder Qwen API Key**: Alibaba Cloud (custom Qwen model)
   - **QCoder: Set QCoder DeepSeek API Key**: DeepSeek (custom)
   - **QCoder: Set QCoder SCNet API Key**: Only used for **custom added SCNet models**, unrelated to the three built-in official models

   When only using the **three built-in SCNet models**, you don't need to configure Qwen / DeepSeek / custom SCNet Key.

3. **Open chat**
   - Click the **QCoder** icon in the activity bar to open the sidebar chat, or run **QCoder: Chat with Quantum Programming Assistant**.

4. **Sidebar settings**
   - Open **Settings** in the title bar or interface: manage custom model lists, interface language, and key writing related to model testing (in supported builds).

Command Overview
~~~~~~~~~~~~~~~~

- **Chat with Quantum Programming Assistant**: Open chat (sidebar / panel)
- **Quick Start**: Open guidance (with multi-language title bar entry)
- **History / New Chat / Settings**: Common operations in the sidebar chat view
- **Set QCoder Qwen / DeepSeek / SCNet API Key**: Write corresponding user-level keys (SCNet item only for custom models)

(The complete list is subject to `package.json` `contributes.commands`.)

Main Settings
~~~~~~~~~~~~~

* `qcoder.qwenApiKey` - Alibaba Cloud API Key (custom Qwen)
* `qcoder.deepseekApiKey` - DeepSeek API Key (custom)
* `qcoder.scnetApiKey` - Dedicated to custom SCNet models; not used by the three built-in models
* `qcoder.customModels` - Custom model list (provider + modelId + label)
* `qcoder.excludedModelKeys` - Model keys hidden in the dropdown
* `qcoder.uiLanguage` - `en` / `zh-CN` / `zh-TW`
* `qcoder.qllvmInstallPath` - QLLVM-related instructions save directory (written by quick start process)
* `qcoder.llmGatewayTimeoutSec` - Timeout when forwarding through built-in gateway (seconds)
* `qcoder.logGatewayPayload` - Whether to record gateway requests in the output panel (key desensitization)
* `qcoder.debugChatUiSync` - Whether to record chat and gateway field debugging information

Project Structure (Mental Model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   ┌──────────────────┐     postMessage      ┌─────────────────────┐
   │  Webview (Chat)   │ ◀──────────────────▶ │  Extension Host      │
   │  UI / i18n / MD   │                      │  Commands / Config / Fetch  │
   └──────────────────┘                      └──────────┬──────────┘
                                                    │
                       ┌───────────────────────────────┼───────────────────────────────┐
                       ▼                               ▼                               ▼
              (Optional) QCoder Gateway                 SCNet / Alibaba Cloud / DeepSeek           OpenAI Compatible API                         

- **`src/extension.ts`**: Activation, Webview provision, message routing, streaming chat, custom model saving, QLLVM download dialog, etc.  
- **`src/webview/`**: `index.html` + `js/app.js`, `i18n.js`, etc. related to UI logic.  
- **`src/qcoderCustomModel.ts`**: Custom model validation and list parsing (conflict detection with built-in model IDs).  
- **`dist/`**: Webpack-built extension entry; **`media/`** contains static resources related to Markdown such as KaTeX CSS.

Development and Build
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   npm install
   npm run compile    # Generate dist/extension.js
   npm run watch      # Watch compilation
   npm run package    # Production packaging
   npm run lint
   npm run test       # Requires local VS Code test environment

Press **F5** to debug in the extension development host.

Common Issues
~~~~~~~~~~~~~

- **Built-in model prompts no key configured**: The current build's `QCODER_BUILTIN_SCNET_API_KEY` is empty or not updated, and needs to be filled in the source code by the distributor and repackaged.  
- **Custom SCNet error**: Check if **QCoder: Set QCoder SCNet API Key** has been set or if the key was filled in when adding the model.  
- **History**: Persisted by extension global state and other mechanisms, the specific number and strategy are subject to the current version implementation.

Version
~~~~~~~

The current version is found in the `version` field of `package.json`. Detailed changes can be maintained in `CHANGELOG.md`.

License
~~~~~~~

MIT, see [LICENSE.md](LICENSE.md).

**Let quantum programming dialogue stay beside the editor, with clear configuration and controllable paths.**
