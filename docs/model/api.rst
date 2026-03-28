API模块
========

本部分包含QLLVM的API参考文档，详细介绍了QLLVM的模块、类和函数。

API概述
--------

QLLVM的API主要分为以下几个模块：

1. **核心模块**：包含QLLVM的主要功能，如模块管理、函数操作等。
2. **优化模块**：包含代码优化相关的功能。
3. **代码生成模块**：包含代码生成相关的功能。
4. **工具模块**：包含各种辅助工具和实用函数。

如何使用API文档
---------------

1. 首先阅读 :doc:`quickstart` 指南，了解QLLVM的基本概念和使用方法。
2. 根据您的需求，查看相应模块的API文档。
3. 参考文档中的示例代码，了解如何使用API。
4. 如果遇到问题，请参考 :doc:`faq` 或在GitHub上提交 `Issue <https://github.com/yourusername/qllvm/issues>`_。

API设计原则
------------

QLLVM的API设计遵循以下原则：

1. **简洁明了**：API设计简洁明了，易于理解和使用。
2. **一致性**：API命名和参数设计保持一致。
3. **可扩展性**：API设计具有良好的可扩展性，便于添加新功能。
4. **安全性**：API设计考虑安全性，避免常见的安全问题。

版本兼容性
----------

QLLVM的API在不同版本之间可能会有变化。为了确保代码的兼容性，建议：

1. 在代码中指定QLLVM的版本要求。
2. 定期更新QLLVM到最新版本。
3. 关注版本更新日志，了解API的变化。

核心模块 API
-------------

本模块包含QLLVM的核心功能，如模块管理、函数操作等。

Module 类
~~~~~~~~~~

Module类是QLLVM的核心类，用于管理LLVM模块。

构造函数
++++++++

.. code-block:: python

    qllvm.Module(name)

**参数：**
- ``name`` (str): 模块名称

**返回值：**
- Module对象

**示例：**

.. code-block:: python

    import qllvm

    # 创建一个名为"my_module"的模块
    module = qllvm.Module("my_module")

方法
+++++

add_function
+++++++++++++

.. code-block:: python

    module.add_function(func)

添加一个函数到模块中。

**参数：**
- ``func`` (callable): 要添加的函数

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 定义一个函数
    def add(a, b):
        return a + b

    # 添加函数到模块
    module.add_function(add)

get_functions
+++++++++++++

.. code-block:: python

    module.get_functions()

获取模块中的所有函数名称。

**参数：**
- 无

**返回值：**
- ``list``: 函数名称列表

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 获取函数列表
    functions = module.get_functions()
    print(functions)  # 输出: ['add']

get_function
+++++++++++++

.. code-block:: python

    module.get_function(name)

获取指定名称的函数。

**参数：**
- ``name`` (str): 函数名称

**返回值：**
- 函数对象

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 获取函数
    func = module.get_function("add")

remove_function
+++++++++++++++

.. code-block:: python

    module.remove_function(name)

从模块中删除指定名称的函数。

**参数：**
- ``name`` (str): 函数名称

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 删除函数
    module.remove_function("add")

compile
++++++++

.. code-block:: python

    module.compile()

编译模块。

**参数：**
- 无

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 编译模块
    module.compile()

execute
++++++++

.. code-block:: python

    module.execute(name, *args)

执行模块中的函数。

**参数：**
- ``name`` (str): 函数名称
- ``*args``: 函数参数

**返回值：**
- 函数执行结果

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)
    module.compile()

    # 执行函数
    result = module.execute("add", 5, 3)
    print(result)  # 输出: 8

save
+++++

.. code-block:: python

    module.save(path)

将模块保存到文件。

**参数：**
- ``path`` (str): 文件路径

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)
    module.compile()

    # 保存模块
    module.save("my_module.bc")

get_ir
+++++++

.. code-block:: python

    module.get_ir()

获取模块的LLVM IR代码。

**参数：**
- 无

**返回值：**
- ``str``: LLVM IR代码

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 获取LLVM IR代码
    ir_code = module.get_ir()
    print(ir_code)

optimize
++++++++

.. code-block:: python

    module.optimize(level=2)

优化模块。

**参数：**
- ``level`` (int): 优化级别，范围为0-3

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 优化模块
    module.optimize(level=3)

transform
+++++++++

.. code-block:: python

    module.transform(pass_name)

应用特定的优化通道。

**参数：**
- ``pass_name`` (str): 优化通道名称

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 应用指令组合优化
    module.transform("instcombine")

全局函数
~~~~~~~~

load_module
++++++++++++

.. code-block:: python

    qllvm.load_module(path)

加载一个模块从文件。

**参数：**
- ``path`` (str): 文件路径

**返回值：**
- Module对象

**示例：**

.. code-block:: python

    import qllvm

    # 加载模块
    module = qllvm.load_module("my_module.bc")

version
++++++++

.. code-block:: python

    qllvm.version()

获取QLLVM的版本号。

**参数：**
- 无

**返回值：**
- ``str``: 版本号

**示例：**

.. code-block:: python

    import qllvm

    # 获取版本号
    version = qllvm.version()
    print(version)

优化与性能分析模块 API
-------------------------

本模块包含QLLVM的优化和性能分析功能，帮助您提高代码性能和分析代码执行情况。

优化相关方法
~~~~~~~~~~~~

enable_optimization_stats
+++++++++++++++++++++++++

.. code-block:: python

    module.enable_optimization_stats()

启用优化统计信息。

**参数：**
- 无

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("optimization_stats")

    # 添加函数
    def example_function(x, y):
        z = x + y
        w = z * 2
        return w

    module.add_function(example_function)

    # 启用优化统计
    module.enable_optimization_stats()

    # 应用优化
    module.optimize(level=3)

get_optimization_stats
++++++++++++++++++++++

.. code-block:: python

    module.get_optimization_stats()

获取优化统计信息。

**参数：**
- 无

**返回值：**
- ``dict``: 优化统计信息

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("optimization_stats")

    # 添加函数
    def example_function(x, y):
        z = x + y
        w = z * 2
        return w

    module.add_function(example_function)
    module.enable_optimization_stats()
    module.optimize(level=3)

    # 获取优化统计信息
    stats = module.get_optimization_stats()
    print(stats)

generate_code
+++++++++++++

.. code-block:: python

    module.generate_code(target)

为指定目标平台生成代码。

**参数：**
- ``target`` (str): 目标平台，如 "x86_64", "arm64", "wasm32" 等

**返回值：**
- ``str``: 生成的代码

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("code_generation")

    # 添加函数
    def multiply(a, b):
        return a * b

    module.add_function(multiply)
    module.compile()

    # 生成x86_64目标代码
    code = module.generate_code("x86_64")
    print(code)

性能分析相关方法
~~~~~~~~~~~~~~~~

enable_profiling
++++++++++++++++

.. code-block:: python

    module.enable_profiling()

启用性能分析。

**参数：**
- 无

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("profiling_example")

    # 添加函数
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    module.add_function(fibonacci)
    module.compile()

    # 启用性能分析
    module.enable_profiling()

get_profiling_data
+++++++++++++++++++

.. code-block:: python

    module.get_profiling_data()

获取性能分析数据。

**参数：**
- 无

**返回值：**
- ``dict``: 性能分析数据，包含函数执行时间、调用次数等信息

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("profiling_example")

    # 添加函数
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    module.add_function(fibonacci)
    module.compile()
    module.enable_profiling()

    # 执行函数
    result = module.execute("fibonacci", 30)

    # 获取性能分析数据
    profiling_data = module.get_profiling_data()
    print(profiling_data)

disable_profiling
+++++++++++++++++

.. code-block:: python

    module.disable_profiling()

禁用性能分析。

**参数：**
- 无

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("profiling_example")

    # 添加函数
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    module.add_function(fibonacci)
    module.compile()
    module.enable_profiling()

    # 执行函数
    result = module.execute("fibonacci", 30)

    # 禁用性能分析
    module.disable_profiling()

工具函数
~~~~~~~~

get_optimization_passes
+++++++++++++++++++++++

.. code-block:: python

    qllvm.get_optimization_passes()

获取所有可用的优化通道。

**参数：**
- 无

**返回值：**
- ``list``: 优化通道名称列表

**示例：**

.. code-block:: python

    import qllvm

    # 获取所有可用的优化通道
    passes = qllvm.get_optimization_passes()
    print(passes)

get_targets
++++++++++++

.. code-block:: python

    qllvm.get_targets()

获取所有支持的目标平台。

**参数：**
- 无

**返回值：**
- ``list``: 目标平台名称列表

**示例：**

.. code-block:: python

    import qllvm

    # 获取所有支持的目标平台
    targets = qllvm.get_targets()
    print(targets)

optimize_module
++++++++++++++++

.. code-block:: python

    qllvm.optimize_module(module, level=2)

优化模块（全局函数版本）。

**参数：**
- ``module`` (Module): 要优化的模块
- ``level`` (int): 优化级别，范围为0-3

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 优化模块
    qllvm.optimize_module(module, level=3)

transform_module
++++++++++++++++

.. code-block:: python

    qllvm.transform_module(module, pass_name)

应用特定的优化通道到模块（全局函数版本）。

**参数：**
- ``module`` (Module): 要转换的模块
- ``pass_name`` (str): 优化通道名称

**返回值：**
- 无

**示例：**

.. code-block:: python

    import qllvm

    module = qllvm.Module("my_module")

    # 添加函数
    def add(a, b):
        return a + b

    module.add_function(add)

    # 应用指令组合优化
    qllvm.transform_module(module, "instcombine")

示例：综合使用优化和性能分析
++++++++++++++++++++++++++++

.. code-block:: python

    import qllvm

    # 创建模块
    module = qllvm.Module("optimization_profiling_example")

    # 添加一个计算斐波那契数列的函数
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    module.add_function(fibonacci)
    module.compile()

    # 启用性能分析
    module.enable_profiling()

    # 执行未优化的函数
    print("执行未优化的函数...")
    result = module.execute("fibonacci", 30)
    print(f"Fibonacci(30) = {result}")

    # 获取未优化的性能数据
    profiling_data_before = module.get_profiling_data()
    print("\n未优化的性能数据:")
    print(profiling_data_before)

    # 优化模块
    print("\n优化模块...")
    module.optimize(level=3)

    # 重置性能分析数据
    module.enable_profiling()  # 重新启用以重置数据

    # 执行优化后的函数
    print("执行优化后的函数...")
    result = module.execute("fibonacci", 30)
    print(f"Fibonacci(30) = {result}")

    # 获取优化后的性能数据
    profiling_data_after = module.get_profiling_data()
    print("\n优化后的性能数据:")
    print(profiling_data_after)

    # 比较性能
    print("\n性能比较:")
    time_before = profiling_data_before.get("fibonacci", {}).get("time", 0)
    time_after = profiling_data_after.get("fibonacci", {}).get("time", 0)
    speedup = time_before / time_after if time_after > 0 else 0
    print(f"优化前执行时间: {time_before:.4f}秒")
    print(f"优化后执行时间: {time_after:.4f}秒")
    print(f"性能提升: {speedup:.2f}x")

这个示例展示了如何使用QLLVM的优化和性能分析功能来提高代码性能并分析优化效果。
