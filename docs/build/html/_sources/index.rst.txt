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

1. **VSCode插件协同（推荐）**

   * **qcoder-chat**：聚焦于量子代码智能开发。提供AI对话编程、智能代码补全与自主Agent任务执行。向下衔接编译与运行，为 ``qcoder-compiler`` 提供高质量量子代码与任务指令，是开发交互入口。

   * **qcoder-compiler**：聚焦于量子代码编译运行。内置QLLVM、qiskit、pyqpanda编译器云编译环境，具备多编译器并行调度、QIR模拟器运行能力。承接 ``qcoder-chat`` 生成结果，编译优化量子代码，完成运行验证，是功能落地关键。

   * **协作体系**：
     ``qcoder-chat``（智能生成/对话）
     → ``qcoder-compiler``（编译运行承接）
     → QLLVM编译器（云端编译）

     形成层层衔接、高效联动的核心协作体系。
     
   * 详细信息请参考 :doc:`usage` 指南中的使用示例部分。

2. **安装QLLVM**：参考 :doc:`installation` 指南安装QLLVM
3. **学习使用方法**：查看 :doc:`usage` 中的使用示例和编译参数说明
4. **贡献代码**：如果您想贡献代码，请参考 :doc:`contributing` 指南

获取帮助
--------

如果您在使用QLLVM时遇到问题，可以通过以下方式获取帮助：

* 在GitHub上提交 `Issue <https://github.com/QCFlow/QLLVM/issues>`_
* 联系项目维护者
