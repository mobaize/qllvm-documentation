Installation Guide
==================

This guide will help you install the QLLVM project on Linux systems.

Common Dependencies
-------------------
Execute the following commands in the system to install system basic dependencies

.. code-block:: bash

    # System basic dependencies
    sudo apt-get update
    sudo apt-get install -y build-essential cmake ninja-build \
      libcurl4-openssl-dev libssl-dev liblapack-dev libblas-dev \
      lsb-release git

**LLVM/MLIR**: QLLVM requires LLVM with MLIR. It is recommended to use the ``llvm`` precompiled package, or compile from [llvm-project-csp](https://github.com/ornl-qci/llvm-project-csp) source code (enable ``clang;mlir``).

.. code-block:: bash

    # Additional dependencies required for QLLVM build
    sudo apt-get install -y libantlr4-runtime-dev libeigen3-dev

QLLVM Build
-----------

.. code-block:: bash

    # Clone repository
    git clone https://github.com/QCFlow/QLLVM qllvm
    cd qllvm

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

Optional Dependencies (install as needed)
----------------------------------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Function
     - Dependency
     - Installation Method
   * - QIR Runner Simulation
     - qir-runner, Python 3.9+
     - ``pip install qirrunner``
   * - Classical-Quantum Hybrid Compilation
     - qir-runner
     - ``pip install qirrunner``
   * - C++ + CUDA + QASM Hybrid
     - CUDA Toolkit, nvcc, qir-runner
     - See CUDA Environment below

CUDA Environment (only needed for C+++CUDA+QASM hybrid)
------------------------------------------------------

If you need to compile C++ + CUDA + QASM hybrid programs such as ``examples/hybrid_cuda``, you need to install CUDA Toolkit.

**Method 1: Ubuntu apt installation (recommended)**

.. code-block:: bash

    # Execute in the qllvm repository root directory
    bash scripts/install_cuda_apt.sh

The script will install ``nvidia-cuda-toolkit`` and create a Clang compatible directory ``~/.qllvm/cuda-apt-compat``. After installation, qllvm will automatically use nvcc to compile ``.cu`` files when nvcc is available.

**Method 2: NVIDIA official runfile**

Download the runfile from [NVIDIA CUDA download page](https://developer.nvidia.com/cuda-downloads), execute ``--toolkit`` to install only the toolchain. After installation, set:

.. code-block:: bash

    export CUDA_PATH=/usr/local/cuda
    export PATH=$CUDA_PATH/bin:$PATH

**Note**: Compiling hybrid programs does not require a physical GPU; running the generated ``hybrid_app`` requires an NVIDIA graphics card and driver.

Verification and Testing
-----------------------

.. code-block:: bash

    # Run test script
    ./scripts/test_openqasm_only.sh

    # Manual verification
    qllvm test/test_bell.qasm -qrt nisq -qpu qasm-backend -O1
    cat test/test_bell_compiled.qasm

Troubleshooting
---------------

If you encounter problems during installation, please try the following solutions:

1. **Dependency issues**: Ensure all dependencies are correctly installed
2. **LLVM version**: Ensure the LLVM version used is compatible with QLLVM
3. **Permission issues**: Use administrator privileges or sudo to install
4. **Network issues**: Ensure network connection is normal, especially when cloning code from GitHub

If the problem still exists, please submit an `Issue <https://github.com/QCFlow/QLLVM/issues>`_ on GitHub.