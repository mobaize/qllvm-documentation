安装
======

本指南将帮助您安装QLLVM项目，包括从插件进行安装和从源码进行安装两种方式。

.. _installation-from-plugins:

从插件进行安装
--------------

我们提供了两个VSCode插件，让您可以直接使用QLLVM编译器，无需本地安装：

1. **qcoder-chat**：量子编程小助手，提供AI对话编程、智能代码补全与自主Agent任务执行。
2. **qcoder-compiler**：量子编译工具，支持多编译器并行编译、QIR模拟器运行等功能。

.. _install-from-VSCode-extension-store:

从VSCode插件商店安装
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: image/007.png
   :align: center
   :width: 80%

.. centered:: VSCode插件商店检索

通过云端 VSCode 一键安装插件，操作简单快捷：

1. 打开云端 VSCode 左侧的 **扩展面板**（快捷键：:kbd:`Ctrl+Shift+X`）；
2. 在扩展搜索框中输入 ``qcflow-publisher.qcoder-chat`` 并搜索；
3. 点击 **安装** 按钮，系统将自动安装以下两个插件：

   - ``qcflow-publisher.qcoder-chat``
   - ``qcflow-publisher.qcoder-compiler``

4. 安装完成后，插件自动生效，即可使用智能编程、编译及运行服务。


.. _install-from-vsix-file:

从VSIX文件安装
~~~~~~~~~~~~~~~~~~~~

**1. 获取插件安装包**

下载仓库中的插件安装包：

- ``./plugin/qcflow-publisher.qcoder-compiler-0.1.0.vsix``
- ``./plugin/qcflow-publisher.qcoder-chat-0.1.1.vsix``

**2. 安装 VSIX 文件**

.. list-table::
   :widths: auto
   :header-rows: 0

   * - | ① 打开命令面板
     - 使用快捷键 :kbd:`Ctrl+Shift+P` (Windows/Linux) 或 :kbd:`Cmd+Shift+P` (macOS)
   * - | ② 输入并选择命令
     - ``Extensions: Install from VSIX...``
   * - | ③ 选择文件
     - 依次选择已下载的 ``.vsix`` 文件完成安装


.. _basic-configuration:

基本配置
~~~~~~~~~~~~~~

.. _quantum-circuit-composer-configuration:

Quantum Compiler配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 打开编译器设置：在命令面板中输入 Open Quantum Compiler Settings
2. 启用编译器：在配置界面中勾选需要的编译器（如QLLVM、Qiskit、QPanda）
3. 配置编译器参数：

   * QLLVM：设置设备类型（NISQ/FTQC）、后端类型（qasm-backend/benyuan/tianyan/zheda）、优化等级（O0/O1）等
   * Python环境：支持自动检测系统Python、虚拟环境（venv/conda），或手动指定解释器路径

.. _qcoder-configuration:

qcoder-chat配置
^^^^^^^^^^^^^^^^^^^

.. image:: image/018.png
   :align: center
   :width: 60%

|

1. 通过 **模型管理** 添加模型信息

   .. image:: image/019.png
      :align: center
      :width: 60%

|

2. 可选配置：

   * **Ask/Agent模式**：Ask模式仅提供聊天交互功能；Agent模式提供写入文件、查询报错信息、调用QLLVM编译、调用QLLVM运行等工具。

   * **深度思考模式**：用于选择大模型是否进行深度思考。部分模型因自身限制只能深度思考，无法取消。

   * **在线服务**：用于启用量子领域专用知识库，通过RAG技术增强量子编程能力。

.. _installation-from-source:

从源码进行安装
--------------

如果您需要直接在本地环境中使用QLLVM命令行工具或进行自定义开发，可以选择从源码编译安装。

.. _environment-requirements:

环境要求
~~~~~~~~

.. list-table:: 
   :header-rows: 1
   :widths: 30 70

   * - 依赖项
     - 版本要求
   * - LLVM 预编译版本
     - 12.0.0
   * - Ubuntu 版本
     - 20.04+
   * - Python 版本
     - 3.10+

.. _common-dependencies:

通用依赖
~~~~~~~~~~~~~~

在系统中执行以下命令，安装系统基础依赖

.. code-block:: bash

    # 系统基础依赖
    sudo apt-get update
    sudo apt-get install -y build-essential cmake ninja-build \
      libcurl4-openssl-dev libssl-dev liblapack-dev libblas-dev \
      lsb-release git
    # 额外依赖
    sudo apt-get install -y libantlr4-runtime-dev libeigen3-dev

**LLVM/MLIR**：QLLVM 需要带 MLIR 的 LLVM。推荐使用预编译包，或从 `llvm-project-csp <https://github.com/ornl-qci/llvm-project-csp>`_ 源码编译（启用 ``clang;mlir``）。

下载并安装 LLVM 12.0.0 预编译包

下载并解压到 ``$HOME/.llvm``：

.. code-block:: bash

  # 使用 wget 直接下载并解压
  wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz
  tar -xf clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz
  mv clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04 ~/.llvm

  # 将 LLVM 添加到环境变量：

  echo 'export PATH="$HOME/.llvm/bin:$PATH"' >> ~/.bashrc
  echo 'export LLVM_HOME="$HOME/.llvm"' >> ~/.bashrc
  echo 'export LD_LIBRARY_PATH="$HOME/.llvm/lib:$LD_LIBRARY_PATH"' >> ~/.bashrc
  source ~/.bashrc

  # 安装依赖包：
  sudo apt install zlib1g-dev libtinfo-dev


.. _qllvm-build:

QLLVM构建
~~~~~~~~~~~~~~

.. code-block:: bash

    # 克隆仓库
    git clone https://github.com/QCFlow/QLLVM.git
    cd QLLVM

    # 构建和安装
    mkdir build && cd build
    cmake .. -G Ninja \
      -DQLLVM_QASM_ONLY_BUILD=ON \
      -DLLVM_ROOT=$HOME/.llvm
    ninja
    ninja install

**安装路径**：默认安装到 ``~/.qllvm``。在 ``ninja install`` 过程中，会自动将 ``~/.qllvm/bin`` 添加到当前用户的 shell 配置（.bashrc/.profile）。打开新终端后即可使用。也可以手动添加：

.. code-block:: bash

    export PATH=$PATH:$HOME/.qllvm/bin

.. _verification-and-testing:

验证和测试
~~~~~~~~~~~~~~

.. code-block:: bash

    # 运行测试脚本
    ./scripts/test_openqasm_only.sh

    # 手动验证
    qllvm test/test_bell.qasm -qrt nisq -qpu qasm-backend -O1
    cat test/test_bell_compiled.qasm

.. _optional-dependencies-install-as-needed:

可选依赖（按需安装）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - 功能
     - 依赖
     - 安装方法
   * - QIR Runner 模拟器
     - qir-runner, Python 3.9+
     - ``pip install qirrunner``
   * - C++ + CUDA + QASM 混合程序编译
     - CUDA Toolkit, nvcc, qir-runner
     - 见下文 CUDA 环境

.. _cuda-environment-only-needed-for-c-cuda-qasm-hybrid:

CUDA环境（仅C+++CUDA+QASM混合需要）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

如果需要编译 ``examples/hybrid_cuda`` 等 C++ + CUDA + QASM 混合程序，需要安装 CUDA Toolkit。

**方法一：Ubuntu apt 安装（推荐）**

.. code-block:: bash

    # 在 qllvm 仓库根目录执行
    bash scripts/install_cuda_apt.sh

该脚本会安装 ``nvidia-cuda-toolkit`` 并创建 Clang 兼容目录 ``~/.qllvm/cuda-apt-compat``。安装后，当 nvcc 可用时，qllvm 会自动使用 nvcc 编译 ``.cu`` 文件。

**方法二：NVIDIA 官方 runfile**

从 [NVIDIA CUDA 下载页面](https://developer.nvidia.com/cuda-downloads) 下载 runfile，执行 ``--toolkit`` 仅安装工具链。安装后设置：

.. code-block:: bash

    export CUDA_PATH=/usr/local/cuda
    export PATH=$CUDA_PATH/bin:$PATH

**注意**：编译混合程序不需要物理 GPU；运行生成的 ``hybrid_app`` 需要 NVIDIA 显卡和驱动。

.. _troubleshooting:

故障排除
--------

如果您在安装过程中遇到问题，请尝试以下解决方法：

1. **依赖问题**：确保所有依赖项都已正确安装
2. **LLVM版本**：确保使用的LLVM版本与QLLVM兼容
3. **权限问题**：使用管理员权限或sudo安装
4. **网络问题**：确保网络连接正常，尤其是在从GitHub克隆代码时

如果问题仍然存在，请在GitHub上提交 `Issue <https://github.com/QCFlow/QLLVM/issues>`_。
