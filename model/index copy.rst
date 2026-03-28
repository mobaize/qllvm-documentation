.. QLLVM documentation master file, created by
   sphinx-quickstart on Mon Mar  9 10:59:14 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. 中文注释：
.. 本文件是QLLVM项目的主文档文件，定义了文档的整体结构
.. 采用reStructuredText格式编写
.. 使用toctree指令组织文档的层级结构



.. image:: ../image/QLLVM0.0.png
   :align: center

QLLVM文档
==========
欢迎来到QLLVM项目的文档！本文档提供了QLLVM的安装指南、使用教程、API参考等内容，帮助您快速上手和深入了解QLLVM。

QLLVM量子编译框架是一个基于 **MLIR** 和 **LLVM IR** 构建的量子程序编译框架。它支持多种量子编程语言输入，经过优化与映射后输出目标硬件支持的代码。我们提供两种使用方式：通过源码安装的命令行执行和使用VSCode插件的快速执行。

.. toctree::
   :maxdepth: 2
   :caption: 文档导航:

   quickstart
   installation
   tutorials
   api
   contributing

.. 中文注释：
.. 上述toctree指令定义了文档的主要章节，每个条目对应一个.rst文件
.. 例如：installation对应source/installation.rst文件

关于QLLVM
=========

QLLVM量子编译框架是一个基于 **MLIR** 和 **LLVM IR** 构建的量子程序编译框架。框架采用前端、中端、后端的三段式设计，支持多种量子编程语言输入，经过优化与映射后输出目标硬件支持的代码。

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

* **前端**：负责语言解析和中间代码生成，将高级语言转换为 MLIR Quantum 方言
* **中端**：基于 MLIR 进行量子程序优化，并将 MLIR 进一步 Lowering 为 QIR（LLVM IR）
* **后端**：基于 QIR 和 QIR 运行时库，将程序转换为目标硬件支持的代码格式

主要优势
--------

1. **工业级 IR 基础设施**：基于 MLIR/LLVM，便于扩展新方言和新 Pass
2. **多种输入形式**：OpenQASM、Qiskit、Q# 等，适配不同编程习惯
3. **灵活优化**：-O0/-O1 等级、自定义 Pass 序列、合成优化
4. **物理约束映射**：SABRE 等布局与 SWAP 策略，适配真实硬件拓扑

快速开始
--------

1. **使用插件（推荐）**：

   * **Quantum Circuit Composer**：VSCode插件，只需安装插件即可使用QLLVM编译器，无需本地安装。支持多编译器并行编译、QIR模拟器运行等功能。

   * **Qcoder**：VSCode侧栏AI助手，聚焦量子算法、量子电路与工具链问题，提供智能对话和代码插入功能。

   * 详细信息请参考 :doc:`quickstart` 指南。

2. **安装QLLVM**：参考 :doc:`installation` 指南安装QLLVM
3. **学习使用方法**：查看 :doc:`tutorials` 中的教程
4. **查阅API文档**：参考 :doc:`api` 获取详细的API信息
5. **贡献代码**：如果您想贡献代码，请参考 :doc:`contributing` 指南

获取帮助
--------

如果您在使用QLLVM时遇到问题，可以通过以下方式获取帮助：

* 在GitHub上提交 `Issue <https://github.com/QCFlow/QLLVM/issues>`_
* 联系项目维护者
