QLLVM教程
====================

本部分主要介绍如何使用QLLVM编译量子线路,以及编译参数的详细说明

运行程序示例
----------------

编译OpenQASM文件
~~~~~~~~~~~~~~~~

**基本编译:**

.. code-block:: bash

  # Using qllvm
  qllvm test.qasm -qrt nisq -qpu qasm-backend -O1
  # Output: test_compiled.qasm

**指定输出路径:**

.. code-block:: bash

  qllvm test.qasm -qrt nisq -qpu qasm-backend -O0 -o folder/try
  # Output: folder/try.qasm

**指定基础门组:**

.. code-block:: bash

    qllvm test.qasm -qrt nisq -qpu qasm-backend -O1 -o folder/try \
      -basicgate=[rx,ry,rz,h,cx]

**带后端拓扑(SABRE 映射):**

.. code-block:: bash

    qllvm test.qasm -qrt nisq -qpu qasm-backend -O1 \
      -qpu-config backend.ini -initial-mapping '[0,1,2]' \
      -sabre-cpp

Bell态示例
~~~~~~~~~~~~~~~~
创建bell.qasm:

.. code-block:: text

    OPENQASM 2.0;
    include "qelib1.inc";
    qreg q[2];
    creg q_c[2];
    h q[0];
    CX q[0], q[1];
    measure q[0] -> q_c[0];
    measure q[1] -> q_c[1];

编译并检查输出:

.. code-block:: bash

    qllvm bell.qasm -qrt nisq -qpu qasm-backend -O1
    cat bell_compiled.qasm

直接调用 qllvm-compile
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Without SABRE
    qllvm-compile test.qasm -internal-func-name test \
      -emit-backend=qasm-backend -output-path=test_out.qasm

    # With SABRE (linear chain 0-1-2)
    qllvm-compile test.qasm -internal-func-name test \
      -emit-backend=qasm-backend -output-path=test_sabre.qasm \
      -sabre-coupling-map="0,1;1,2"

打印 MLIR / QIR
~~~~~~~~~~~~~~~~

.. code-block:: bash

    qllvm test.qasm -emitmlir -qrt nisq -qpu qasm-backend -O1
    qllvm test.qasm -emitqir -qrt nisq -qpu qasm-backend -O1

后端拓扑配置示例
~~~~~~~~~~~~~~~~

`backend.ini` 或 `qpu_config_chain3.txt`:

.. code-block:: ini

    # Linear chain: 0-1-2
    connectivity = [[0, 1], [1, 2]]

编译参数说明
------------------------------

本教程将介绍qllvm编译参数的详细说明。

驱动程序（qllvm）参数
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 驱动程序（qllvm ）参数
   :widths: 20 60 20
   :header-rows: 1

   * - 参数
     - 说明
     - 示例
   * - `-O0`
     - 不进行编译优化
     - ``-O0``
   * - `-O1`
     - 使用固定优化遍序列
     - ``-O1``
   * - `-basicgate`
     - 指定基础门组
     - ``-basicgate=[rx,ry,rz,h,cz]``, ``-basicgate=[rx,ry,rz,h,cx]``, ``-basicgate=[su2,x,y,z,cz]`` (for measurement and control)
   * - `-qrt`
     - 指定设备类型
     - ``-qrt nisq``, ``-qrt ftqc``
   * - `-qpu`
     - 指定后端类型
     - ``-qpu qasm-backend``
   * - `-qpu-config`
     - 指定后端拓扑结构（耦合图）
     - ``-qpu-config ./backend.ini``
   * - `-emitmlir`
     - 打印 MLIR 程序
     - ``-emitmlir``
   * - `-emitqir`
     - 打印 QIR 程序
     - ``-emitqir``
   * - `-customPassSequence`
     - 指定优化遍序列文件
     - ``-customPassSequence=./pass.txt``
   * - `-o`
     - 指定输出路径及文件名
     - ``-o folder/name``
   * - `-placement`
     - 指定映射方法
     - ``-placement sabre_swap``, ``-placement swap_shortest_path``
   * - `-initial-mapping`
     - 指定初始比特映射
     - ``-initial-mapping '[0,1,2,3,4]'``
   * - `-sabre-cpp`
     - 在 LLVM IR 阶段使用 C++ SABRE（需配合 `-initial-mapping` 和 `-qpu-config`）
     - ``-sabre-cpp``
   * - `-circuit-state`
     - 打印电路状态（深度、门数）
     - ``-circuit-state``
   * - `-pass-count`
     - 打印各 Pass 执行次数
     - ``-pass-count``
   * - `-v` / `--verbose`
     - 开启详细输出
     - ``-v``
   * - `-cuda-arch`
     - 为混合 CUDA 指定 GPU 架构
     - ``-cuda-arch sm_75``
   * - `-cuda-path`
     - 为混合 CUDA 指定 CUDA 安装路径（可选，默认使用 `CUDA_PATH` 或 nvcc 推导）
     - ``-cuda-path /usr/local/cuda``

**常用基础门组:**

- ``[rx,ry,rz,h,cz]``: 默认
- ``[rx,ry,rz,h,cx]``: 使用 CX
- ``[su2,x,y,z,cz]``: 用于测量和控制系统

qllvm-compile 参数
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: qllvm-compile 参数
   :widths: 30 70
   :header-rows: 1

   * - 参数
     - 说明
   * - `<input.qasm>`
     - positional,输入 OpenQASM 文件
   * - `-internal-func-name`
     - 生成的内核函数名
   * - `-no-entrypoint`
     - 不生成 main 入口
   * - `-O0`
     - 优化等级 0
   * - `-O1`
     - 优化等级 1
   * - `-qpu`
     - 目标量子后端
   * - `-qrt`
     - 量子执行模式（nisq/ftqc）
   * - `-emitmlir`
     - 打印 MLIR
   * - `-emitqir`
     - 打印 QIR
   * - `-emit-backend`
     - 指定发射后端（如 `qasm-backend`）
   * - `-output-path`
     - 输出文件路径
   * - `-output-ll`
     - 输出 LLVM IR 路径（用于混合编译链接）
   * - `-sabre-coupling-map`
     - SABRE 耦合图,边格式 `0,1;1,2;2,3`
   * - `-circuit-state`
     - 打印电路深度和门数
   * - `-pass-count`
     - 打印各 Pass 执行次数
   * - `-basicgate`
     - 基础门组
   * - `-customPassSequence`
     - 自定义 Pass 序列文件
   * - `-verbose-error`
     - 出错时打印完整 MLIR
   * - `--pass-timing`
     - Pass 耗时统计
   * - `--print-ir-after-all`
     - 每 Pass 后打印 IR
   * - `--print-ir-before-all`
     - 每 Pass 前打印 IR
     
CMake 构建参数
~~~~~~~~~~~~~~~

.. list-table:: CMake 构建参数
   :widths: 30 70
   :header-rows: 1

   * - 参数
     - 说明
   * - `-DLLVM_ROOT`
     - LLVM 安装路径（含 MLIR）
   * - `-DXACC_DIR`
     - 可选依赖路径（antlr4/exprtk）；QASM-only 独立构建时设为空：`-DXACC_DIR=`
   * - `-DCMAKE_INSTALL_PREFIX`
     - 安装目录（默认 ~/.qllvm）
   * - `-DQLLVM_QASM_ONLY_BUILD=ON`
     - 启用 QASM-only 独立构建
