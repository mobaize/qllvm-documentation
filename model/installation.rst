安装指南
==========

本指南将帮助您安装QLLVM项目。

系统要求
--------

在安装QLLVM之前，请确保您的系统满足以下要求：

- **操作系统**：Linux、macOS或Windows
- **Python版本**：Python 3.8或更高版本
- **LLVM**：LLVM 12.0或更高版本
- **其他依赖**：请参考``requirements.txt``文件

安装方法
--------

使用pip安装
~~~~~~~~~~~

如果您只需要使用QLLVM，可以通过pip安装：

```bash
pip install qllvm
```

从源码安装
~~~~~~~~~~~

如果您需要修改或贡献代码，可以从源码安装：

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/qllvm.git
cd qllvm
```

2. 安装开发依赖：

```bash
pip install -e .
```

3. 安装测试依赖（可选）：

```bash
pip install -e .[test]
```

验证安装
--------

安装完成后，您可以运行以下命令验证安装是否成功：

```bash
python -c "import qllvm; print(qllvm.__version__)"
```

如果安装成功，您将看到QLLVM的版本号。

环境配置
--------

环境变量
~~~~~~~~~

QLLVM可能需要以下环境变量：

- ``LLVM_PATH``：指向LLVM安装目录（如果LLVM不在默认路径）
- ``QLLVM_CONFIG``：指向QLLVM配置文件（可选）

配置文件
~~~~~~~~~

QLLVM使用配置文件来存储设置。默认情况下，配置文件位于：

- Linux/macOS：``~/.config/qllvm/config.json``
- Windows：``%APPDATA%\qllvm\config.json``

您可以通过修改此配置文件来自定义QLLVM的行为。

故障排除
--------

如果您在安装过程中遇到问题，请尝试以下解决方法：

1. **依赖问题**：确保所有依赖项都已正确安装
2. **LLVM版本**：确保使用的LLVM版本与QLLVM兼容
3. **权限问题**：使用管理员权限或sudo安装
4. **网络问题**：确保网络连接正常，尤其是在从GitHub克隆代码时

如果问题仍然存在，请参考：:doc:`faq` 或在GitHub上提交 `Issue <https://github.com/yourusername/qllvm/issues>`_。