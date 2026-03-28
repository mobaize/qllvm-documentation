QLLVM Tutorial
====================

This section mainly introduces how to use QLLVM to compile quantum circuits, as well as detailed explanations of compilation parameters

Running Program Examples
------------------------

Compiling OpenQASM Files
~~~~~~~~~~~~~~~~~~~~~~~~

**Basic compilation:**

.. code-block:: bash

  # Using qllvm
  qllvm test.qasm -qrt nisq -qpu qasm-backend -O1
  # Output: test_compiled.qasm

**Specifying output path:**

.. code-block:: bash

  qllvm test.qasm -qrt nisq -qpu qasm-backend -O0 -o folder/try
  # Output: folder/try.qasm

**Specifying basic gate set:**

.. code-block:: bash

    qllvm test.qasm -qrt nisq -qpu qasm-backend -O1 -o folder/try \
      -basicgate=[rx,ry,rz,h,cx]

**With backend topology (SABRE mapping):**

.. code-block:: bash

    qllvm test.qasm -qrt nisq -qpu qasm-backend -O1 \
      -qpu-config backend.ini -initial-mapping '[0,1,2]' \
      -sabre-cpp

Bell State Example
~~~~~~~~~~~~~~~~~~
Create bell.qasm:

.. code-block:: text

    OPENQASM 2.0;
    include "qelib1.inc";
    qreg q[2];
    creg q_c[2];
    h q[0];
    CX q[0], q[1];
    measure q[0] -> q_c[0];
    measure q[1] -> q_c[1];

Compile and check output:

.. code-block:: bash

    qllvm bell.qasm -qrt nisq -qpu qasm-backend -O1
    cat bell_compiled.qasm

Directly Calling qllvm-compile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Without SABRE
    qllvm-compile test.qasm -internal-func-name test \
      -emit-backend=qasm-backend -output-path=test_out.qasm

    # With SABRE (linear chain 0-1-2)
    qllvm-compile test.qasm -internal-func-name test \
      -emit-backend=qasm-backend -output-path=test_sabre.qasm \
      -sabre-coupling-map="0,1;1,2"

Printing MLIR / QIR
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    qllvm test.qasm -emitmlir -qrt nisq -qpu qasm-backend -O1
    qllvm test.qasm -emitqir -qrt nisq -qpu qasm-backend -O1

Backend Topology Configuration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`backend.ini` or `qpu_config_chain3.txt`:

.. code-block:: ini

    # Linear chain: 0-1-2
    connectivity = [[0, 1], [1, 2]]

Compilation Parameter Explanation
----------------------------------

This tutorial will introduce the detailed explanation of qllvm compilation parameters.

Driver Program (qllvm) Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Driver Program (qllvm) Parameters
   :widths: 20 60 20
   :header-rows: 1

   * - Parameter
     - Description
     - Example
   * - `-O0`
     - No compilation optimization
     - ``-O0``
   * - `-O1`
     - Use fixed optimization pass sequence
     - ``-O1``
   * - `-basicgate`
     - Specify basic gate set
     - ``-basicgate=[rx,ry,rz,h,cz]``, ``-basicgate=[rx,ry,rz,h,cx]``, ``-basicgate=[su2,x,y,z,cz]`` (for measurement and control)
   * - `-qrt`
     - Specify device type
     - ``-qrt nisq``, ``-qrt ftqc``
   * - `-qpu`
     - Specify backend type
     - ``-qpu qasm-backend``
   * - `-qpu-config`
     - Specify backend topology (coupling graph)
     - ``-qpu-config ./backend.ini``
   * - `-emitmlir`
     - Print MLIR program
     - ``-emitmlir``
   * - `-emitqir`
     - Print QIR program
     - ``-emitqir``
   * - `-customPassSequence`
     - Specify optimization pass sequence file
     - ``-customPassSequence=./pass.txt``
   * - `-o`
     - Specify output path and filename
     - ``-o folder/name``
   * - `-placement`
     - Specify mapping method
     - ``-placement sabre_swap``, ``-placement swap_shortest_path``
   * - `-initial-mapping`
     - Specify initial qubit mapping
     - ``-initial-mapping '[0,1,2,3,4]'``
   * - `-sabre-cpp`
     - Use C++ SABRE in LLVM IR phase (requires `-initial-mapping` and `-qpu-config`)
     - ``-sabre-cpp``
   * - `-circuit-state`
     - Print circuit state (depth, gate count)
     - ``-circuit-state``
   * - `-pass-count`
     - Print execution count of each pass
     - ``-pass-count``
   * - `-v` / `--verbose`
     - Enable detailed output
     - ``-v``
   * - `-cuda-arch`
     - Specify GPU architecture for hybrid CUDA
     - ``-cuda-arch sm_75``
   * - `-cuda-path`
     - Specify CUDA installation path for hybrid CUDA (optional, default uses `CUDA_PATH` or nvcc deduction)
     - ``-cuda-path /usr/local/cuda``

**Common basic gate sets:**

- ``[rx,ry,rz,h,cz]``: Default
- ``[rx,ry,rz,h,cx]``: Using CX
- ``[su2,x,y,z,cz]``: For measurement and control systems

qllvm-compile Parameters
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: qllvm-compile Parameters
   :widths: 30 70
   :header-rows: 1

   * - Parameter
     - Description
   * - `<input.qasm>`
     - positional, input OpenQASM file
   * - `-internal-func-name`
     - Generated kernel function name
   * - `-no-entrypoint`
     - Do not generate main entry
   * - `-O0`
     - Optimization level 0
   * - `-O1`
     - Optimization level 1
   * - `-qpu`
     - Target quantum backend
   * - `-qrt`
     - Quantum execution mode (nisq/ftqc)
   * - `-emitmlir`
     - Print MLIR
   * - `-emitqir`
     - Print QIR
   * - `-emit-backend`
     - Specify emission backend (e.g., `qasm-backend`)
   * - `-output-path`
     - Output file path
   * - `-output-ll`
     - Output LLVM IR path (for hybrid compilation linking)
   * - `-sabre-coupling-map`
     - SABRE coupling map, edge format `0,1;1,2;2,3`
   * - `-circuit-state`
     - Print circuit depth and gate count
   * - `-pass-count`
     - Print execution count of each pass
   * - `-basicgate`
     - Basic gate set
   * - `-customPassSequence`
     - Custom pass sequence file
   * - `-verbose-error`
     - Print complete MLIR on error
   * - `--pass-timing`
     - Pass timing statistics
   * - `--print-ir-after-all`
     - Print IR after each pass
   * - `--print-ir-before-all`
     - Print IR before each pass
     
CMake Build Parameters
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: CMake Build Parameters
   :widths: 30 70
   :header-rows: 1

   * - Parameter
     - Description
   * - `-DLLVM_ROOT`
     - LLVM installation path (including MLIR)
   * - `-DXACC_DIR`
     - Optional dependency path (antlr4/exprtk); set to empty for QASM-only independent build: `-DXACC_DIR=`
   * - `-DCMAKE_INSTALL_PREFIX`
     - Installation directory (default ~/.qllvm)
   * - `-DQLLVM_QASM_ONLY_BUILD=ON`
     - Enable QASM-only independent build