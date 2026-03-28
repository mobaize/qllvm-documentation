安装指南
==========

本指南将帮助您在Linux系统中安装QLLVM项目。

通用依赖
--------
在系统中执行以下命令，安装系统基础依赖

.. code-block:: bash

    # 系统基础依赖
    sudo apt-get update
    sudo apt-get install -y build-essential cmake ninja-build \
      libcurl4-openssl-dev libssl-dev liblapack-dev libblas-dev \
      lsb-release git

**LLVM/MLIR**：QLLVM 需要带 MLIR 的 LLVM。推荐使用 ``llvm`` 预编译包，或从 [llvm-project-csp](https://github.com/ornl-qci/llvm-project-csp) 源码编译（启用 ``clang;mlir``）。

.. code-block:: bash

    # 额外依赖
    sudo apt-get install -y libantlr4-runtime-dev libeigen3-dev

QLLVM构建
--------

.. code-block:: bash

    # 克隆仓库
    git clone https://github.com/QCFlow/QLLVM qllvm
    cd qllvm

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

可选依赖（按需安装）
------------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - 功能
     - 依赖
     - 安装方法
   * - QIR Runner 模拟
     - qir-runner, Python 3.9+
     - ``pip install qirrunner``
   * - 经典-量子混合编译
     - qir-runner
     - ``pip install qirrunner``
   * - C++ + CUDA + QASM 混合
     - CUDA Toolkit, nvcc, qir-runner
     - 见下文 CUDA 环境

CUDA环境（仅C+++CUDA+QASM混合需要）
----------------------------------

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

验证和测试
--------

.. code-block:: bash

    # 运行测试脚本
    ./scripts/test_openqasm_only.sh

    # 手动验证
    qllvm test/test_bell.qasm -qrt nisq -qpu qasm-backend -O1
    cat test/test_bell_compiled.qasm

故障排除
--------

如果您在安装过程中遇到问题，请尝试以下解决方法：

1. **依赖问题**：确保所有依赖项都已正确安装
2. **LLVM版本**：确保使用的LLVM版本与QLLVM兼容
3. **权限问题**：使用管理员权限或sudo安装
4. **网络问题**：确保网络连接正常，尤其是在从GitHub克隆代码时

如果问题仍然存在，请在GitHub上提交 `Issue <https://github.com/QCFlow/QLLVM/issues>`_。