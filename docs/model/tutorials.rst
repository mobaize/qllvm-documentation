QLLVM教程
==========

本部分包含QLLVM的各种教程，从基础到高级。

教程概述
--------

基础教程
~~~~~~~~

- **教程1**：介绍QLLVM的基本使用方法，包括模块创建、函数添加和执行。
- **教程2**：深入了解QLLVM的核心功能，包括优化和代码转换。

高级教程
~~~~~~~~

- **教程3**：QLLVM的高级应用，如性能分析和代码生成。
- **教程4**：QLLVM与其他工具的集成。

如何使用教程
-------------

1. 首先阅读 :doc:`installation` 指南，确保QLLVM已正确安装。
2. 阅读 :doc:`quickstart` 指南，了解QLLVM的基本概念和使用方法。
3. 按照教程的顺序学习，从基础教程开始，逐步深入。
4. 尝试运行教程中的示例代码，加深理解。
5. 如果遇到问题，请参考 :doc:`faq` 或在GitHub上提交 `Issue <https://github.com/yourusername/qllvm/issues>`_。

贡献教程
--------

如果您有好的教程内容，欢迎贡献给QLLVM项目。请参考 :doc:`contributing` 指南了解如何贡献。

教程1：QLLVM基础使用
--------------------

本教程将介绍QLLVM的基本使用方法，包括模块创建、函数添加、模块编译和函数执行等核心功能。

准备工作
~~~~~~~~

在开始本教程之前，请确保您已经：

1. 安装了QLLVM（参考 :doc:`installation` 指南）
2. 了解了QLLVM的基本概念（参考 :doc:`quickstart` 指南）

步骤1：创建模块
~~~~~~~~~~~~~~~~

首先，我们需要创建一个QLLVM模块。模块是QLLVM中的基本代码组织单位，类似于一个代码文件。

.. code-block:: python

    import qllvm

    # 创建一个名为"my_module"的模块
    module = qllvm.Module("my_module")
    print(f"创建了模块: {module.name}")

运行上述代码，您将看到输出：

.. code-block::

    创建了模块: my_module

步骤2：添加函数
~~~~~~~~~~~~~~~~

现在，我们可以向模块中添加函数。函数是QLLVM中的基本执行单元。

添加函数示例
~~~~~~~~~~~~~

示例1：添加一个简单的加法函数
+++++++++++++++++++++++++++++

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 定义一个加法函数
    def add(a, b):
        """返回两个数的和"""
        return a + b

    # 将函数添加到模块
    module.add_function(add)
    print(f"添加了函数: add")

    # 查看模块中的函数
    functions = module.get_functions()
    print(f"模块中的函数: {functions}")

运行上述代码，您将看到输出：

.. code-block::

    添加了函数: add
    模块中的函数: ['add']

示例2：添加一个更复杂的函数
+++++++++++++++++++++++++++++

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 定义一个计算阶乘的函数
    def factorial(n):
        """返回n的阶乘"""
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    # 将函数添加到模块
    module.add_function(factorial)
    print(f"添加了函数: factorial")

    # 查看模块中的函数
    functions = module.get_functions()
    print(f"模块中的函数: {functions}")

运行上述代码，您将看到输出：

.. code-block::

    添加了函数: factorial
    模块中的函数: ['factorial']

步骤3：编译模块
~~~~~~~~~~~~~~~~

添加函数后，我们需要编译模块，以便执行其中的函数。

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加一个加法函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 编译模块
    module.compile()
    print("模块编译成功")

运行上述代码，您将看到输出：

.. code-block::

    模块编译成功

步骤4：执行函数
~~~~~~~~~~~~~~~~

编译模块后，我们可以执行其中的函数。

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加一个加法函数
    def add(a, b):
        return a + b

    module.add_function(add)
    module.compile()

    # 执行add函数
    result = module.execute("add", 5, 3)
    print(f"5 + 3 = {result}")

    # 执行多次
    result1 = module.execute("add", 10, 20)
    print(f"10 + 20 = {result1}")

    result2 = module.execute("add", -5, 7)
    print(f"-5 + 7 = {result2}")

运行上述代码，您将看到输出：

.. code-block::

    5 + 3 = 8
    10 + 20 = 30
    -5 + 7 = 2

步骤5：保存和加载模块
~~~~~~~~~~~~~~~~~~~~~

我们可以将模块保存到文件，以便以后使用。

保存和加载模块示例
~~~~~~~~~~~~~~~~~~~~

保存模块
+++++++++

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加一个加法函数
    def add(a, b):
        return a + b

    module.add_function(add)
    module.compile()

    # 保存模块到文件
    module.save("my_module.bc")
    print("模块保存成功")

运行上述代码，您将看到输出：

.. code-block::

    模块保存成功

加载模块
+++++++++

.. code-block:: python

    import qllvm

    # 加载模块
    loaded_module = qllvm.load_module("my_module.bc")
    print(f"加载了模块: {loaded_module.name}")

    # 查看模块中的函数
    functions = loaded_module.get_functions()
    print(f"模块中的函数: {functions}")

    # 执行函数
    result = loaded_module.execute("add", 100, 200)
    print(f"100 + 200 = {result}")

运行上述代码，您将看到输出：

.. code-block::

    加载了模块: my_module
    模块中的函数: ['add']
    100 + 200 = 300

步骤6：查看LLVM IR代码
~~~~~~~~~~~~~~~~~~~~~~

QLLVM基于LLVM，我们可以查看生成的LLVM IR代码，了解QLLVM如何将Python函数转换为LLVM IR。

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加一个加法函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 查看LLVM IR代码
    ir_code = module.get_ir()
    print("生成的LLVM IR代码:")
    print(ir_code)

运行上述代码，您将看到类似以下输出：

.. code-block::

    生成的LLVM IR代码:
    ; ModuleID = 'my_module'
    source_filename = "my_module"

    define i32 @add(i32 %a, i32 %b) {
    entry:
      %add = add nsw i32 %a, %b
      ret i32 %add
    }

总结
~~~~

在本教程中，我们学习了QLLVM的基本使用方法：

1. 创建模块
2. 添加函数
3. 编译模块
4. 执行函数
5. 保存和加载模块
6. 查看LLVM IR代码

这些是QLLVM的核心功能，掌握这些功能后，您可以开始使用QLLVM进行更复杂的任务。

教程2：QLLVM优化与代码转换
------------------------------

本教程将介绍QLLVM的优化和代码转换功能，帮助您提高代码性能和理解代码转换过程。

准备工作
~~~~~~~~

在开始本教程之前，请确保您已经：

1. 安装了QLLVM（参考 :doc:`installation` 指南）
2. 完成了教程1，了解了QLLVM的基本使用方法

步骤1：了解优化级别
~~~~~~~~~~~~~~~~~~~~

QLLVM提供了不同级别的优化，从0（无优化）到3（最高优化）。不同级别的优化会应用不同的优化策略。

.. code-block:: python

    import qllvm

    module = qllvm.Module("optimization_example")

    # 添加一个简单的函数
    def simple_function(x):
        y = x + 1
        z = y * 2
        return z

    module.add_function(simple_function)

    # 查看不同优化级别下的LLVM IR代码
    for level in range(4):
        print(f"\n优化级别 {level}:")
        module.optimize(level=level)
        print(module.get_ir())

运行上述代码，您将看到不同优化级别下生成的LLVM IR代码的差异。

步骤2：应用特定优化
~~~~~~~~~~~~~~~~~~~~

除了使用预设的优化级别，QLLVM还允许您应用特定的优化通道。

.. code-block:: python

    import qllvm

    module = qllvm.Module("specific_optimization")

    # 添加一个函数
    def complex_function(a, b, c):
        x = a + b
        y = x * c
        z = y - a
        return z

    module.add_function(complex_function)

    # 查看优化前的代码
    print("优化前:")
    print(module.get_ir())

    # 应用特定优化
    print("\n应用指令组合优化:")
    module.transform("instcombine")
    print(module.get_ir())

    print("\n应用死代码消除优化:")
    module.transform("dce")
    print(module.get_ir())

    print("\n应用控制流图简化优化:")
    module.transform("simplify-cfg")
    print(module.get_ir())

运行上述代码，您将看到每次应用特定优化后代码的变化。

步骤3：性能分析
~~~~~~~~~~~~~~~~~~~~

QLLVM提供了性能分析功能，可以帮助您了解代码的执行情况。

.. code-block:: python

    import qllvm

    module = qllvm.Module("profiling_example")

    # 添加一个计算斐波那契数列的函数
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    module.add_function(fibonacci)
    module.compile()

    # 启用性能分析
    module.enable_profiling()

    # 执行函数
    print("执行斐波那契数列计算...")
    result = module.execute("fibonacci", 30)
    print(f"Fibonacci(30) = {result}")

    # 获取性能数据
    profiling_data = module.get_profiling_data()
    print("\n性能分析数据:")
    print(profiling_data)

运行上述代码，您将看到函数的执行时间和调用次数等性能数据。

步骤4：代码转换
~~~~~~~~~~~~~~~~~~~~

QLLVM允许您对代码进行各种转换，例如指令重排序、常量折叠等。

代码转换示例
~~~~~~~~~~~~~~~

示例1：常量折叠
+++++++++++++++

.. code-block:: python

    import qllvm

    module = qllvm.Module("constant_folding")

    # 添加一个包含常量表达式的函数
    def constant_function():
        # 这些是编译时可以计算的常量表达式
        a = 1 + 2
        b = 3 * 4
        c = a + b
        return c

    module.add_function(constant_function)

    # 查看优化前的代码
    print("优化前:")
    print(module.get_ir())

    # 应用常量折叠优化
    module.optimize(level=2)
    print("\n优化后:")
    print(module.get_ir())

运行上述代码，您将看到常量表达式被计算为常量值。

示例2：循环优化
+++++++++++++++

.. code-block:: python

    import qllvm

    module = qllvm.Module("loop_optimization")

    # 添加一个包含循环的函数
    def loop_function(n):
        sum = 0
        for i in range(n):
            sum += i
        return sum

    module.add_function(loop_function)

    # 查看优化前的代码
    print("优化前:")
    print(module.get_ir())

    # 应用循环优化
    module.optimize(level=3)
    print("\n优化后:")
    print(module.get_ir())

运行上述代码，您将看到循环被优化的情况。

步骤5：查看优化统计信息
~~~~~~~~~~~~~~~~~~~~~~~

QLLVM提供了优化统计信息，可以帮助您了解优化过程中发生了什么。

.. code-block:: python

    import qllvm

    module = qllvm.Module("optimization_stats")

    # 添加一个函数
    def example_function(x, y):
        z = x + y
        w = z * 2
        if w > 10:
            return w
        else:
            return z

    module.add_function(example_function)

    # 启用优化统计
    module.enable_optimization_stats()

    # 应用优化
    module.optimize(level=3)

    # 获取优化统计信息
    stats = module.get_optimization_stats()
    print("优化统计信息:")
    print(stats)

运行上述代码，您将看到优化过程中应用的各种优化通道及其效果。

步骤6：自定义优化管道
~~~~~~~~~~~~~~~~~~~~~

QLLVM允许您创建自定义的优化管道，按照您的需求应用特定的优化通道。

.. code-block:: python

    import qllvm

    module = qllvm.Module("custom_optimization")

    # 添加一个函数
    def custom_function(a, b):
        x = a + b
        y = x * a
        z = y - b
        return z

    module.add_function(custom_function)

    # 创建自定义优化管道
    optimization_pipeline = [
        "instcombine",  # 指令组合
        "simplify-cfg",  # 控制流图简化
        "reassociate",  # 重新关联表达式
        "gvn",  # 全局值编号
        "dce"  # 死代码消除
    ]

    # 应用自定义优化管道
    print("优化前:")
    print(module.get_ir())

    for pass_name in optimization_pipeline:
        print(f"\n应用 {pass_name}:")
        module.transform(pass_name)
        print(module.get_ir())

运行上述代码，您将看到每次应用优化通道后代码的变化。

步骤7：代码生成
~~~~~~~~~~~~~~~~~~~~~

QLLVM允许您生成不同目标平台的代码。

.. code-block:: python

    import qllvm

    module = qllvm.Module("code_generation")

    # 添加一个函数
    def multiply(a, b):
        return a * b

    module.add_function(multiply)
    module.compile()

    # 生成不同目标平台的代码
    targets = ["x86_64", "arm64", "wasm32"]

    for target in targets:
        print(f"\n生成 {target} 目标代码:")
        code = module.generate_code(target)
        print(code)

运行上述代码，您将看到为不同目标平台生成的代码。

总结
~~~~

在本教程中，我们学习了QLLVM的优化和代码转换功能：

1. 了解不同的优化级别
2. 应用特定的优化通道
3. 使用性能分析功能
4. 进行代码转换
5. 查看优化统计信息
6. 创建自定义优化管道
7. 为不同目标平台生成代码

这些功能可以帮助您提高代码性能，理解代码优化过程，以及为不同平台生成高效的代码。

下一步
------

- 参考 :doc:`../api` 查看详细的API文档
- 阅读 :doc:`../faq` 了解常见问题
- 学习如何使用QLLVM与其他工具集成
