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

   introduction
   installation
   usage
   contributing

.. 中文注释：
.. 上述toctree指令定义了文档的主要章节，每个条目对应一个.rst文件
.. 例如：installation对应source/installation.rst文件

快速开始
--------

1. **使用插件（推荐）**：

   * **Quantum Circuit Composer**：VSCode插件，只需安装插件即可使用QLLVM编译器，无需本地安装。支持多编译器并行编译、QIR模拟器运行等功能。

   * **Qcoder**：VSCode侧栏AI助手，聚焦量子算法、量子电路与工具链问题，提供智能对话和代码插入功能。

   * 详细信息请参考 :doc:`usage` 指南中的使用示例部分。

2. **安装QLLVM**：参考 :doc:`installation` 指南安装QLLVM
3. **学习使用方法**：查看 :doc:`usage` 中的使用示例和编译参数说明
4. **贡献代码**：如果您想贡献代码，请参考 :doc:`contributing` 指南

获取帮助
--------

如果您在使用QLLVM时遇到问题，可以通过以下方式获取帮助：

* 在GitHub上提交 `Issue <https://github.com/QCFlow/QLLVM/issues>`_
* 联系项目维护者
