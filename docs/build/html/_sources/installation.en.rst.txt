Installation
============

This guide will help you install the QLLVM project, including installation from plugins and installation from source code.

Installation from Plugins
-------------------------

We provide two VSCode plugins that allow you to use the QLLVM compiler directly without local installation:

1. **Quantum Circuit Composer**: Quantum compilation tool, supporting multi-compiler parallel compilation, QIR simulator running, and other functions.
2. **Qcoder**: Quantum programming assistant, providing intelligent dialogue and code insertion functions.

Install from VSIX File
~~~~~~~~~~~~~~~~~~~~~~

1. Download the plugin installation packages:
   - `quantum-circuit-composer-*.vsix`
   - `qcoder-*.vsix`
2. Open the command palette in VSCode (`Ctrl+Shift+P` / `Cmd+Shift+P`)
3. Type and select **Extensions: Install from VSIX...**
4. Select the downloaded `.vsix` files one by one to complete the installation

Basic Configuration
~~~~~~~~~~~~~~~~~~~~~~

Quantum Circuit Composer Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open compiler settings: Type **Open Quantum Compiler Settings** in the command palette
2. Enable compilers: Check the compilers you need in the configuration interface (such as QLLVM, Qiskit, QPanda)
3. Configure compiler parameters:

   * QLLVM: Set device type (NISQ/FTQC), backend type (qasm-backend/benyuan/tianyan/zheda), optimization level (O0/O1), etc.
   * Python environment: Supports automatic detection of system Python, virtual environments (venv/conda), or manually specifying interpreter path
   * Remote compilation: Can configure SSH connection information to submit compilation tasks to remote servers

Qcoder Configuration
^^^^^^^^^^^^^^^^^^^^^

1. Configure API Key (execute as needed):
   - `Set QCoder Qwen API Key`: Alibaba Cloud
   - `Set QCoder DeepSeek API Key`: DeepSeek
   - `Set QCoder SCNet API Key`: Custom SCNet model
2. Optional configuration:
   - `qcoder.qllvmInstallPath`: QLLVM installation path (for quick start)
   - `qcoder.uiLanguage`: Interface language (en/zh-CN/zh-TW)
   - RAG knowledge enhancement: Enable "Online Service" in chat settings to get enhanced answers based on quantum computing knowledge base

Installation from Source
------------------------

If you need to use QLLVM command line tools directly in your local environment or perform custom development, you can choose to compile and install from source code.

.. _environment-requirements:

Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
   :header-rows: 1
   :widths: 30 70

   * - Dependency
     - Version Requirement
   * - LLVM precompiled version
     - 12.0.0
   * - Ubuntu version
     - 20.04+
   * - Python version
     - 3.10+

Common Dependencies
~~~~~~~~~~~~~~~~~~~~

Execute the following commands in the system to install system basic dependencies

.. code-block:: bash

    # System basic dependencies
    sudo apt-get update
    sudo apt-get install -y build-essential cmake ninja-build \
      libcurl4-openssl-dev libssl-dev liblapack-dev libblas-dev \
      lsb-release git
    # Additional dependencies
    sudo apt-get install -y libantlr4-runtime-dev libeigen3-dev

**LLVM/MLIR**: QLLVM requires LLVM with MLIR. It is recommended to use a pre-built package, or build from source using `llvm-project-csp <https://github.com/ornl-qci/llvm-project-csp>`_ (enable ``clang;mlir``).

Download the LLVM 12.0.0 pre-built package and extract it to ``$HOME/.llvm``:

.. code-block:: bash

   # Manual download and extraction
   # Visit https://github.com/llvm/llvm-project/releases/tag/llvmorg-12.0.0
   # Select clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz to download
   cd ~/Downloads
   tar -xf clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz
   mv clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04 ~/.llvm

   # Or download and extract directly using wget
   wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz
   tar -xf clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz
   mv clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04 ~/.llvm

   # Add LLVM to PATH (optional)
   echo 'export PATH=$HOME/.llvm/bin:$PATH' >> ~/.bashrc
   source ~/.bashrc

QLLVM Build
~~~~~~~~~~~~

.. code-block:: bash

    # Clone repository
    git clone https://github.com/QCFlow/QLLVM.git
    cd QLLVM

    # Build and install
    mkdir build && cd build
    cmake .. -G Ninja \
      -DQLLVM_QASM_ONLY_BUILD=ON \
      -DLLVM_ROOT=$HOME/.llvm
    ninja
    ninja install

**Installation path**: Default installation to ``~/.qllvm``. During ``ninja install``, it will automatically add ``~/.qllvm/bin`` to the current user's shell configuration (.bashrc/.profile). It can be used after opening a new terminal. You can also add it manually:

.. code-block:: bash

    export PATH=$PATH:$HOME/.qllvm/bin

.. _verification-and-testing:

Verification and Testing
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Run test script
    ./scripts/test_openqasm_only.sh

    # Manual verification
    qllvm test/test_bell.qasm -qrt nisq -qpu qasm-backend -O1
    cat test/test_bell_compiled.qasm

.. _optional-dependencies-install-as-needed:

Optional Dependencies (install as needed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Function
     - Dependency
     - Installation Method
   * - QIR Runner Simulator
     - qir-runner, Python 3.9+
     - ``pip install qirrunner``
   * - C++ + CUDA + QASM Hybrid Program Compilation
     - CUDA Toolkit, nvcc, qir-runner
     - See CUDA Environment below

CUDA Environment (only needed for C+++CUDA+QASM hybrid)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to compile ``examples/hybrid_cuda`` and other C++ + CUDA + QASM hybrid programs, you need to install CUDA Toolkit.

**Method 1: Ubuntu apt installation (recommended)**

.. code-block:: bash

    # Execute in the qllvm repository root directory
    bash scripts/install_cuda_apt.sh

The script will install ``nvidia-cuda-toolkit`` and create a Clang compatible directory ``~/.qllvm/cuda-apt-compat``. After installation, when nvcc is available, qllvm will automatically use nvcc to compile ``.cu`` files.

**Method 2: NVIDIA official runfile**

Download runfile from [NVIDIA CUDA download page](https://developer.nvidia.com/cuda-downloads), execute ``--toolkit`` to install only the toolchain. After installation, set:

.. code-block:: bash

    export CUDA_PATH=/usr/local/cuda
    export PATH=$CUDA_PATH/bin:$PATH

**Note**: Compiling hybrid programs does not require a physical GPU; running the generated ``hybrid_app`` requires an NVIDIA graphics card and driver.

.. _troubleshooting:

Troubleshooting
---------------

If you encounter problems during installation, please try the following solutions:

1. **Dependency issues**: Ensure all dependencies are correctly installed
2. **LLVM version**: Ensure the LLVM version used is compatible with QLLVM
3. **Permission issues**: Use administrator privileges or sudo to install
4. **Network issues**: Ensure network connection is normal, especially when cloning code from GitHub
