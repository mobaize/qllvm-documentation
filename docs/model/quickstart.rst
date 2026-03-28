快速入门
==========

本指南将帮助您快速上手QLLVM项目。

基本概念
--------

在开始使用QLLVM之前，了解以下基本概念将有助于您更好地理解和使用该项目：

- **QLLVM**：一个基于LLVM的Python封装库，提供了简洁、Pythonic的API来操作和优化LLVM模块。
- **LLVM**：一个编译器基础设施，用于构建编译器、优化器和运行时环境。
- **模块**：QLLVM中的基本代码组织单位。
- **函数**：QLLVM中的基本执行单元。
- **指令**：QLLVM中的基本操作单元。

第一个示例
----------

让我们通过一个简单的示例来了解QLLVM的基本使用方法。

示例：创建一个简单的模块
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import qllvm

    # 创建一个新的模块
    module = qllvm.Module("example")

    # 添加一个函数
    def add(a, b):
        return a + b

    # 将函数添加到模块
    module.add_function(add)

    # 编译模块
    module.compile()

    # 执行函数
    result = module.execute("add", 1, 2)
    print(f"1 + 2 = {result}")

运行上述代码，您将看到输出：

.. code-block::

    1 + 2 = 3

核心功能演示
------------

1. 模块管理
~~~~~~~~~~~

QLLVM允许您创建、加载和保存模块：

.. code-block:: python

    import qllvm

    # 创建新模块
    module = qllvm.Module("my_module")

    # 加载现有模块
    loaded_module = qllvm.load_module("path/to/module.bc")

    # 保存模块
    module.save("path/to/output.bc")

2. 函数操作
~~~~~~~~~~~

您可以添加、修改和删除函数：

.. code-block:: python

    import qllvm

    module = qllvm.Module("functions")

    # 添加函数
    def multiply(a, b):
        return a * b

    module.add_function(multiply)

    # 获取函数
    func = module.get_function("multiply")

    # 删除函数
    module.remove_function("multiply")

3. 优化
~~~~~~~

QLLVM提供了多种优化选项：

.. code-block:: python

    import qllvm

    module = qllvm.Module("optimization")

    # 添加函数
    def complex_function(x):
        y = x + 1
        z = y * 2
        return z

    module.add_function(complex_function)

    # 应用优化
    module.optimize(level=3)  # 3是最高优化级别

    # 查看优化后的代码
    print(module.get_ir())

常见用例
--------

1. 代码生成
~~~~~~~~~~~

使用QLLVM生成LLVM IR代码：

.. code-block:: python

    import qllvm

    module = qllvm.Module("codegen")

    # 添加函数
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    module.add_function(factorial)

    # 生成LLVM IR
    ir_code = module.get_ir()
    print(ir_code)

2. 性能分析
~~~~~~~~~~~

使用QLLVM分析代码性能：

.. code-block:: python

    import qllvm

    module = qllvm.Module("profiling")

    # 添加函数
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    module.add_function(fibonacci)

    # 启用性能分析
    module.enable_profiling()

    # 执行函数
    result = module.execute("fibonacci", 30)
    print(f"Fibonacci(30) = {result}")

    # 获取性能数据
    profiling_data = module.get_profiling_data()
    print(profiling_data)

3. 代码转换
~~~~~~~~~~~

使用QLLVM进行代码转换：

.. code-block:: python

    import qllvm

    # 加载模块
    module = qllvm.load_module("input.bc")

    # 应用转换
    module.transform("simplify-cfg")  # 简化控制流图
    module.transform("instcombine")  # 指令组合

    # 保存转换后的模块
    module.save("output.bc")

下一步
------

现在您已经了解了QLLVM的基本使用方法，您可以：

- 查看 :doc:`tutorials` 了解更多教程
- 参考 :doc:`api` 查看详细的API文档
- 阅读 :doc:`faq` 了解常见问题
