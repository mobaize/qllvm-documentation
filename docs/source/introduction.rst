QLLVM介绍
==========

* QLLVM是一个基于LLVM构建的经典-量子混合编译框架，具备卓越的可扩展性以及与经典高性能计算生态的无缝集成能力。

* QLLVM支持多种量子编程语言及后端，所支持的编程语言包括Qiskit、OpenQASM等，目标后端包括qasm模拟器、本源量子计算机、中电信“天衍”量子计算机等。

* QLLVM支持量子程序、CUDA程序和经典C++程序的统一编译，为未来经典-量子软件开发提供了高效、灵活且工业级的编译基础设施。

总体功能
--------

QLLVM 将高级量子程序编译为目标后端可执行代码，主要功能包括：

* **多语言前端**：支持 OpenQASM 2.0/3.0、Qiskit QuantumCircuit、Q# 等输入
* **MLIR 优化**：单比特门合并、抵消、对角门移除、门综合等优化 Pass
* **QIR 生成**：将 MLIR 方言 Lowering 为 QIR（LLVM IR 形式的量子中间表示）
* **SABRE 映射**：C++/Qiskit 实现的量子比特布局与 SWAP 插入
* **多后端发射**：输出 OpenQASM、硬件特定格式等

**编译流水线：**
```
QASM 源文件 → 预处理 → MLIR (Quantum 方言) → 优化 Passes → Lowering → LLVM IR (QIR) → 后端发射
```

技术路线
--------

.. image:: image/001.png
   :align: center
   :width: 80%

.. centered:: QLLVM编译框架

* **前端**：负责语言解析和中间代码生成，将高级语言转换为 MLIR Quantum 方言
* **中端**：基于 MLIR 进行量子程序优化，并将 MLIR 进一步 Lowering 为 QIR（LLVM IR）
* **后端**：基于 QIR 和 QIR 运行时库，将程序转换为目标硬件支持的代码格式

依托 LLVM 生态，QLLVM 能够实现与经典编译 Pass、CUDA 编程模型和 HPC 运行时的集成，从而实现高效的经典量子混合任务编译。

.. image:: image/02.png
   :align: center
   :width: 100%

.. centered:: 经典量子混合程序编译机制

同时基于LLVM编译框架，QLLVM编译器能够和多类经典高性能编译器协同编译，从而支持经典量子混合程序的编译。

.. image:: image/003.png
   :align: center
   :width: 100%

.. centered:: 混合程序代码编写示例

主要优势
--------

1. **工业级 IR 基础设施**：基于 MLIR/LLVM，便于扩展新方言和新 Pass
2. **多种输入形式**：OpenQASM、Qiskit、Q# 等，适配不同编程习惯
3. **灵活优化**：-O0/-O1 等级、自定义 Pass 序列、合成优化
4. **物理约束映射**：SABRE 等布局与 SWAP 策略，适配真实硬件拓扑

项目结构概览
------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 目录
     - 说明
   * - ``mlir/``
     - MLIR 方言、解析器、转换、Lowering
   * - ``mlir/dialect/``
     - Quantum 方言定义
   * - ``mlir/parsers/``
     - OpenQASM3、Qiskit 解析器
   * - ``mlir/transforms/``
     - 优化 Pass（门合并、抵消、综合等）
   * - ``mlir/tools/``
     - ``qllvm-compile`` 主编译器
   * - ``passes/``
     - LLVM IR Pass（SABRE 等）
   * - ``backend/``
     - QIR → 后端代码（如 QasmBackend）
   * - ``tools/driver/``
     - 驱动脚本 ``qllvm.in``
   * - ``test/``
     - 测试与示例 QASM
   * - ``docs/``
     - 安装指南、设计文档