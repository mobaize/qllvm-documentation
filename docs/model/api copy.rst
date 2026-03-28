QLLVM量子编译框架
========================

QLLVM量子编译框架是一个基于 MLIR 和 LLVM IR 构建的量子程序编译框架。框架采用前端、中端、后端的三段式设计，支持多种量子编程语言输入，经过优化与映射后输出目标硬件支持的代码。

软件介绍
--------

.. list-table:: QLLVM 将高级量子程序编译为目标后端可执行代码，主要功能包括
   :widths: 20 40
   :header-rows: 1

   * - 功能模块
     - 说明
   * - `多语言前端`
     - 支持 OpenQASM 2.0/3.0、Qiskit QuantumCircuit、Q# 等输入
   * - `MLIR 优化`
     - 单比特门合并、抵消、对角门移除、门综合等优化 Pass
   * - `QIR 生成`
     - 将 MLIR 方言 Lowering 为 QIR (LLVM IR 形式的量子中间表示)
   * - `SABRE 映射`
     -  C++/Qiskit 实现的量子比特布局与 SWAP 插入
   * - `多后端发射`
     - 输出 OpenQASM、硬件特定格式等

编译流水线
---------------
``QASM 源文件 → 预处理 → MLIR (Quantum 方言) → 优化 Passes → Lowering → LLVM IR (QIR) → 后端发射``

技术路线
---------------
1. 前端：负责语言解析和中间代码生成，将高级语言转换为 MLIR Quantum 方言
2. 中端：基于 MLIR 进行量子程序优化，并将 MLIR 进一步 Lowering 为 QIR（LLVM IR）
3. 后端：基于 QIR 和 QIR 运行时库，将程序转换为目标硬件支持的代码格式

主要优势
---------------
1. 工业级 IR 基础设施：基于 MLIR/LLVM，便于扩展新方言和新 Pass
2. 多种输入形式：OpenQASM、Qiskit、Q# 等，适配不同编程习惯
3. 灵活优化：-O0/-O1 等级、自定义 Pass 序列、合成优化
4. 物理约束映射：SABRE 等布局与 SWAP 策略，适配真实硬件拓扑

可选依赖
--------

QIR Runner 后端
~~~~~~~~~~~~~~

输出 LLVM 位码（.bc）供 QIR Runner 模拟器加载。qllvm 内置 **QirRunnerCompat**，自动适配 qir-runner 的 QIR base profile（`__quantum__rt__initialize` 签名、`__body` 后缀、mz 结果索引等）。

.. code-block:: bash

    # 1. 安装 qir-runner（conda qllvm 环境）
    conda activate qllvm
    pip install qirrunner

    # 2. 使用 qllvm-compile 生成 .bc
    qllvm-compile bell.qasm -qrt nisq -qpu qir-runner -O1 \
      -emit-backend=qir-runner -output-path=bell.bc

    # 3. 使用 qir-runner 运行
    qir-runner -f bell.bc -s 5

**qir-runner 输出格式说明**

每次 shot 的输出结构：

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 行
     - 含义
   * - `START`
     - 一次 shot 的开始
   * - `METADATA\tEntryPoint`
     - 入口点元数据
   * - `RESULT\t0` 或 `RESULT\t1`
     - 每个比特的测量结果（按测量顺序）
   * - `END\t0`
     - 一次 shot 的结束

**qir-runner 命令行参数**

.. list-table::
   :widths: 30 40 30
   :header-rows: 1

   * - 参数
     - 说明
     - 默认值
   * - `-f, --file <PATH>`
     - QIR 位码文件路径（必需）
     - -
   * - `-s, --shots <NUM>`
     - 模拟的 shot 数
     - 1
   * - `-r, --rngseed <NUM>`
     - 随机数种子（可复现）
     - 随机
   * - `-e, --entrypoint <NAME>`
     - 入口函数名
     - EntryPoint

**输出为 Qiskit 风格的 counts**

使用 `scripts/qir_runner_counts.py` 将原始输出转换为 Qiskit 风格的 `get_counts()` 字典：

.. code-block:: bash

    # Pipeline方式
    qir-runner -f bell.bc -s 100 | python3 scripts/qir_runner_counts.py -

    # 直接指定 bc 和参数
    python3 scripts/qir_runner_counts.py bell.bc -s 100 -r 42

- **输出示例（Bell 态）**：`{'00': 48, '11': 52}`

- **配套测试脚本**：`./scripts/test_qllvm_qirrunner.sh`

.bc 是标准 LLVM 位码，可被 [qir-alliance/qir-runner](https://github.com/qir-alliance/qir-runner) 等工具加载（需要 Python 3.9+）。

经典-量子混合编译
~~~~~~~~~~~~~~~~~~

依托 LLVM 生态，QLLVM 可实现与经典编译 Pass、CUDA 编程模型、HPC 运行时的融合，从而实现高效的经典-量子混合任务编译。

支持 C++ 主程序与 QASM 量子电路的混合编译，生成单一可执行文件：

.. code-block:: bash

    # 混合编译（qir-qrt-stub 实现）
    qllvm main.cpp circuit.qasm -o hybrid_app

    # 示例位于 examples/hybrid/
    qllvm examples/hybrid/main.cpp examples/hybrid/bell.qasm -o hybrid_bell
    ./hybrid_bell

**使用 qir-runner 作为模拟器**

.. code-block:: bash

    # 混合编译 + qir-runner 模拟（生成 exe 和 .bc）
    qllvm main.cpp bell.qasm -qpu qir-runner -o hybrid_bell -O1

    # 运行（需要 qir-runner 在 PATH 中）
    ./hybrid_bell -shots 10

- **工作流**：QASM → QIR .bc（qir-runner）+ C++ 编译 → 可执行文件在运行时间接调用 qir-runner 子进程模拟量子电路。

- **配套测试脚本**：`./scripts/test_hybrid_qirrunner.sh`

**C++ + CUDA + QASM 混合编译**

支持 C++ 主程序、CUDA 内核、QASM 量子电路的混合编译，生成单一可执行文件（需 CUDA 环境）：

.. code-block:: bash

    cd examples/hybrid_cuda

    # 编译（-cuda-arch 指定 GPU 架构，如 sm_75、sm_86）
    qllvm main.cpp kernel.cu circuit.qasm -o hybrid_app \
          -cuda-arch sm_75 \
          -cuda-path /usr/local/cuda

    # 如果 nvcc 在 PATH 中，-cuda-path 可省略，会自动推导
    qllvm main.cpp kernel.cu circuit.qasm -o hybrid_app -cuda-arch sm_86

    # 运行
    ./hybrid_app -shots 1024

- **依赖**：Clang（支持 `-x cuda`）、CUDA Toolkit、qir-runner（`pip install qirrunner`）。

- **Ubuntu apt 安装 CUDA**：运行 `bash scripts/install_cuda_apt.sh` 自动安装 nvidia-cuda-toolkit 并创建 Clang 兼容目录（`~/.qllvm/cuda-apt-compat`）。

QLLVM使用指南
---------------

1. 安装QLLVM :doc:`installation` 指南，了解QLLVM的安装方法。
2. 使用QLLVM :doc:`tutorials` 指南，了解如何使用QLLVM编译量子线路。


