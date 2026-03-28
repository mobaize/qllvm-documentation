贡献指南
==================

感谢您对QLLVM项目的关注和支持！我们欢迎各种形式的贡献，包括代码、文档、测试、问题报告等。本指南将帮助您了解如何为QLLVM项目做出贡献。

行为准则
--------

参与QLLVM项目的所有贡献者都应遵守以下行为准则：

- 尊重他人，保持友好和专业的态度
- 接受建设性批评
- 关注社区的最佳利益
- 对其他贡献者表示同理心

如何贡献
--------

报告问题
~~~~~~~~~

如果您发现了bug或有新功能建议，请在GitHub上提交 `Issue <https://github.com/QCFlow/QLLVM/issues>`_。在提交Issue时，请提供以下信息：

- 问题的详细描述
- 重现问题的步骤
- 期望的行为
- 实际的行为
- 环境信息（操作系统、Python版本、QLLVM版本等）
- 相关的错误信息或日志

贡献代码
~~~~~~~~~

如果您想贡献代码，请按照以下步骤操作：

1. **Fork仓库**

   * 在GitHub上fork QLLVM仓库到您自己的账户

2. **克隆仓库**

   * 克隆您fork的仓库到本地

.. code-block:: bash

   git clone https://github.com/QCFlow/QLLVM.git
   cd qllvm

3. **创建分支**

   * 创建一个新的分支来进行您的修改
   
.. code-block:: bash

   git checkout -b feature/your-feature-name

4. **安装开发依赖**

   * 安装开发依赖

.. code-block:: bash

   pip install -e .[dev]

5. **进行修改**

   * 进行您的代码修改
   * 确保代码风格符合项目要求
   * 添加适当的测试

6. **运行测试**

   * 运行测试确保您的修改没有破坏现有功能

.. code-block:: bash

   pytest

7. **提交更改**

   * 提交您的更改，使用清晰的提交信息

.. code-block:: bash

   git add .
   git commit -m "Add feature: your feature description"

8. **推送分支**

   * 推送您的分支到GitHub

.. code-block:: bash

   git push origin feature/your-feature-name

9. **创建Pull Request**

   * 在GitHub上创建一个Pull Request，描述您的更改
   * 等待项目维护者的审核

贡献文档
~~~~~~~~~

如果您想贡献文档，请按照以下步骤操作：

1. Fork和克隆仓库（同代码贡献步骤1-2）

2. 创建分支（同代码贡献步骤3）

3. **安装文档依赖**

   * 安装文档构建依赖

.. code-block:: bash

   pip install -e .[docs]

4. **修改文档**

   * 修改或添加文档内容
   * 确保文档风格一致
   * 检查链接是否有效

5. **构建文档**

   * 构建文档确保没有错误

.. code-block:: bash

   cd docs
   make html

6. 提交更改（同代码贡献步骤7-9）

贡献测试
~~~~~~~~~

如果您想贡献测试，请按照以下步骤操作：

1. Fork和克隆仓库（同代码贡献步骤1-2）

2. 创建分支（同代码贡献步骤3）

3. **安装测试依赖**

   * 安装测试依赖

4. **添加测试**

   * 添加新的测试用例
   * 确保测试覆盖新功能或修复的bug

5. **运行测试**

   * 运行测试确保测试通过

6. 提交更改（同代码贡献步骤7-9）

代码风格
--------

QLLVM项目遵循以下代码风格：

- **Python代码**：遵循PEP 8规范
  - 使用4个空格进行缩进
  - 行长度不超过79个字符
  - 导入顺序：标准库、第三方库、本地模块
  - 使用文档字符串记录函数和类

- **文档**：遵循reStructuredText格式
  - 使用清晰的标题层级
  - 代码示例使用正确的语法高亮
  - 链接使用相对路径

- **提交信息**：使用清晰的提交信息
  - 第一行：简短的描述（不超过50个字符）
  - 空行
  - 详细描述（如果需要）
  - 引用相关的Issue（如果有）


沟通渠道
--------

- **GitHub Issues**：用于报告问题和讨论功能
- **GitHub Discussions**：用于讨论项目相关的话题
- **邮件列表**：如果有邮件列表，请在这里提供

贡献者指南
----------

首次贡献
~~~~~~~~~

如果您是第一次贡献开源项目，以下资源可能会有所帮助：

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [First Contributions](https://firstcontributions.github.io/)
- [GitHub Docs: Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

代码审查
~~~~~~~~~

所有的Pull Request都会经过代码审查。在审查过程中，您可能需要根据审查意见进行修改。请保持耐心和开放的态度，代码审查是提高代码质量的重要环节。

许可证
~~~~~~~

通过贡献代码到QLLVM项目，您同意您的贡献将在项目的许可证下发布。

致谢
----

感谢所有为QLLVM项目做出贡献的人！您的贡献是项目成功的关键。
