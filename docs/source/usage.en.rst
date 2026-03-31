Usage
======

This section mainly introduces how to use QLLVM to compile quantum circuits, as well as detailed explanations of compilation parameters.

.. _usage-examples:

Usage Examples
--------------

.. _using-plugins:

Using Plugins
~~~~~~~~~~~~~

Cloud Usage
^^^^^^^^^^^

.. image:: image/006.png
   :align: center
   :width: 80%

.. centered:: VScode Plugin Interface

.. list-table:: Feature Description
   :widths: 20 80
   :header-rows: 1

   * - Area
     - Feature Description
   * - ① Qcoder Sidebar
     - Click to use Qcoder intelligent programming assistant
   * - ② Qcoder Main Interface
     - Intelligent interactive interface
   * - ③ Code Interface
     - Used to display quantum programs
   * - ④ Compile Button
     - Click to compile the code interface or selected quantum program
   * - ⑤ Run Button
     - Click to run the code interface or selected quantum program
   * - ⑥ Output Interface
     - Output the compiled quantum circuit and various parameters

Quantum Circuit Composer
^^^^^^^^^^^^^^^^^^^^^^^^

Quantum Circuit Composer is a Visual Studio Code plugin with the following main features:

- **Multi-compiler support**: Configure multiple compilers (self-developed QLLVM, IBM Qiskit, Origin QPanda) simultaneously, compile in parallel with one click, and automatically generate result comparison tables.
- **Multi-frontend input**: Supports QASM, Qiskit Python code, QPanda Python code, OriginIR, QCIS and other input formats, which are uniformly converted to QASM for compilation.
- **Remote/local compilation**: Uses remote server compilation by default (no local compiler installation required), and can also be switched to local compilation.
- **QIR simulator**: Run QIR simulator directly in the plugin to view measurement result statistics.
- **Statistical comparison**: Automatically extracts the number of gates, two-qubit gates, and depth from each compiler after compilation, and generates a comparison table.
- **Graphical settings**: Manage compiler configurations through the settings panel, easily enable/disable, and edit parameters.

**Quick start:**

1. **Install the plugin**

   * Search for "Quantum Circuit Composer" in the VSCode extension store and install it.
   * After installation, a circuit board icon will appear in the status bar, click to open the settings panel.

2. **Write quantum circuit**

   * Create a new file, supporting `.qasm` (OpenQASM), `.py` (Qiskit/QPanda code), `.originir`, `.qcis`, etc.
   * For example, a simple Bell state QASM file:

   .. code-block:: text

      OPENQASM 2.0;
      include "qelib1.inc";
      qreg q[2];
      creg c[2];
      h q[0];
      cx q[0],q[1];
      measure q[0] -> c[0];
      measure q[1] -> c[1];

3. **Compile file**

   * Right-click on the file and select **"Compile current quantum circuit file"**.
   * Or open the settings panel and click **"▶ Select file to compile"** at the top.
   * The plugin will use all enabled compilers to compile in parallel and display results and statistical comparison tables in the output channel.

4. **Run QIR simulator**

   * In the compiler list of the settings panel, find the QLLVM compiler and click the **"▶ Run simulator"** button on its right.
   * Enter shots (number of runs) and random seed (optional) in the pop-up input box.
   * After simulation is complete, the output channel will display measurement result statistics.

Qcoder
^^^^^^

**VS Code Sidebar AI Assistant for Quantum Computing Learning and Development**

QCoder embeds large model dialogue into the editor sidebar, focusing on quantum algorithms, quantum circuits, and toolchain issues, rather than general chat. It allows users to configure their own API Key for Alibaba Cloud, DeepSeek, or **custom SCNet models**.

**Quick start:**

1. **Installation**

   * Search and install in the VS Code extension view, or use **Install from VSIX…** to install the `.vsix` distributed by the organization.

2. **Configure API Key (according to the model you actually use)**

   Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

   * **QCoder: Set QCoder Qwen API Key**: Alibaba Cloud (custom Qwen model)
   * **QCoder: Set QCoder DeepSeek API Key**: DeepSeek (custom)
   * **QCoder: Set QCoder SCNet API Key**: Only used for **custom added SCNet models**, unrelated to the three built-in official models

   When only using the **three built-in SCNet models**, you don't need to configure Qwen / DeepSeek / custom SCNet Key.

3. **Open chat**

   * Click the **QCoder** icon in the activity bar to open the sidebar chat, or run **QCoder: Chat with Quantum Programming Assistant**.

4. **Sidebar settings**

   * Open **Settings** in the title bar or interface: manage custom model lists, interface language, and key writing related to model testing (in supported builds).



.. _using-command-line:

Using Command Line
~~~~~~~~~~~~~~~~~~

.. _compiling-openqasm-files:

Compiling Pure Quantum Programs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compiling OpenQASM Files
""""""""""""""""""""""""""

**Basic compilation:**

.. code-block:: bash

  # Using qllvm
  qllvm test.qasm -qrt nisq -qpu qasm-backend -O1
  # Output: test_compiled.qasm

**Specify output path:**

.. code-block:: bash

  qllvm test.qasm -qrt nisq -qpu qasm-backend -O0 -o folder/try
  # Output: folder/try.qasm

**Specify basis gate set:**

.. code-block:: bash

    qllvm test.qasm -qrt nisq -qpu qasm-backend -O1 -o folder/try \
      -basicgate=[rx,ry,rz,h,cx]

**With backend topology (SABRE mapping):**

.. code-block:: bash

    qllvm test.qasm -qrt nisq -qpu qasm-backend -O1 \
      -qpu-config backend.ini -initial-mapping '[0,1,2]' \
      -sabre-cpp

.. _bell-state-example:

Bell State Example
""""""""""""""""""""

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

.. _directly-calling-qllvm-compile:

Directly Calling qllvm-compile
""""""""""""""""""""""""""""""""

.. code-block:: bash

    # Without SABRE
    qllvm-compile test.qasm -internal-func-name test \
      -emit-backend=qasm-backend -output-path=test_out.qasm

    # With SABRE (linear chain 0-1-2)
    qllvm-compile test.qasm -internal-func-name test \
      -emit-backend=qasm-backend -output-path=test_sabre.qasm \
      -sabre-coupling-map="0,1;1,2"

.. _printing-mlir-qir:

Printing MLIR / QIR
""""""""""""""""""""""

.. code-block:: bash

    qllvm test.qasm -emitmlir -qrt nisq -qpu qasm-backend -O1
    qllvm test.qasm -emitqir -qrt nisq -qpu qasm-backend -O1

.. _backend-topology-configuration-example:

Backend Topology Configuration Example
""""""""""""""""""""""""""""""""""""""""

`backend.ini` or `qpu_config_chain3.txt`:

.. code-block:: ini

    # Linear chain: 0-1-2
    connectivity = [[0, 1], [1, 2]]

.. _qir-runner-backend:

QIR Runner Backend Configuration Example
"""""""""""""""""""""""""""""""""""""""""""

Output LLVM bitcode (.bc) for QIR Runner simulator loading. qllvm has built-in **QirRunnerCompat** to automatically adapt to qir-runner's QIR base profile (`__quantum__rt__initialize` signature, `__body` suffix, mz result index, etc.).

.. code-block:: bash

    # 1. Install qir-runner (conda qllvm environment)
    conda activate qllvm
    pip install qirrunner

    # 2. Use qllvm-compile to generate .bc
    qllvm-compile bell.qasm -qrt nisq -qpu qir-runner -O1 \
      -emit-backend=qir-runner -output-path=bell.bc

    # 3. Run with qir-runner
    qir-runner -f bell.bc -s 5

.. _qir-runner-output-format-explanation:

qir-runner Output Format Explanation
++++++++++++++++++++++++++++++++++++

Output structure for each shot:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Line
     - Meaning
   * - `START`
     - A shot begins
   * - `METADATA\tEntryPoint`
     - Entry point metadata
   * - `RESULT\t0` or `RESULT\t1`
     - Measurement results for each qubit (in measurement order)
   * - `END\t0`
     - The shot ends

Example (Bell circuit 5 shots):

.. code-block:: text

    START
    METADATA	EntryPoint
    RESULT	0
    RESULT	0
    END	0
    START
    METADATA	EntryPoint
    RESULT	1
    RESULT	1
    END	0
    ...

.. _qir-runner-command-line-parameters:

qir-runner Command Line Parameters
++++++++++++++++++++++++++++++++++

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - Parameter
     - Description
     - Default
   * - `-f, --file <PATH>`
     - QIR bitcode file path (required)
     - -
   * - `-s, --shots <NUM>`
     - Number of simulation shots
     - 1
   * - `-r, --rngseed <NUM>`
     - Random number seed (for reproducibility)
     - Random
   * - `-e, --entrypoint <NAME>`
     - Entry function name
     - EntryPoint

.. _output-as-qiskit-style-counts:

Output as Qiskit-style Counts
"""""""""""""""""""""""""""""""

Use `scripts/qir_runner_counts.py` to convert raw output to Qiskit-style `get_counts()` dictionary:

.. code-block:: bash

    # Pipe method
    qir-runner -f bell.bc -s 100 | python3 scripts/qir_runner_counts.py -

    # Directly specify bc and parameters
    python3 scripts/qir_runner_counts.py bell.bc -s 100 -r 42

- **Output example (Bell state)**: `{'00': 48, '11': 52}`

- **Collaborative test script**: `./scripts/test_qllvm_qirrunner.sh`

`.bc` is standard LLVM bitcode, which can be loaded by tools like [qir-alliance/qir-runner](https://github.com/qir-alliance/qir-runner) (requires Python 3.9+).


.. _classical-quantum-hybrid-compilation:

Compiling Classical-Quantum Hybrid Programs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Optional Dependencies (Install as needed)
+++++++++++++++++++++++++++++++++++++++++

If you need to compile classical-quantum hybrid programs, you need to install qir-runner (`pip install qirrunner`) and the following dependencies:

- **Dependencies**: Clang (supports `-x cuda`), CUDA Toolkit, qir-runner (`pip install qirrunner`).
- **Ubuntu apt install CUDA**: Run `bash scripts/install_cuda_apt.sh` to automatically install nvidia-cuda-toolkit and create Clang-compatible directory (`~/.qllvm/cuda-apt-compat`). See `examples/hybrid_cuda/README.md` for details.

Classical-Quantum Hybrid Compilation
++++++++++++++++++++++++++++++++++++

Supports compiling C++ main programs with QASM quantum circuits into a single executable:

.. code-block:: bash

    # Hybrid compilation (qir-qrt-stub stub implementation)
    qllvm main.cpp circuit.qasm -o hybrid_app

    # Example located in examples/hybrid/
    qllvm examples/hybrid/main.cpp examples/hybrid/bell.qasm -o hybrid_bell
    ./hybrid_bell

.. _using-qir-runner-as-simulator:

Using qir-runner as Simulator
+++++++++++++++++++++++++++++

.. code-block:: bash

    # Hybrid compilation + qir-runner simulation (generates exe and .bc)
    qllvm main.cpp bell.qasm -qpu qir-runner -o hybrid_bell -O1

    # Run (requires qir-runner in PATH)
    ./hybrid_bell -shots 10

- **Workflow**: QASM → QIR .bc (qir-runner) + C++ compilation → Executable indirectly calls qir-runner subprocess to simulate quantum circuits at runtime.

- **Collaborative test script**: `./scripts/test_hybrid_qirrunner.sh`

See `examples/hybrid/README.md` for details.

.. _c-cuda-qasm-hybrid-compilation:

C++ + CUDA + QASM Hybrid Compilation
++++++++++++++++++++++++++++++++++++++

Supports compiling C++ main programs, CUDA kernels, and QASM quantum circuits into a single executable (requires CUDA environment):

.. code-block:: bash

    cd examples/hybrid_cuda

    # Compile (-cuda-arch specifies GPU architecture, e.g., sm_75, sm_86)
    qllvm main.cpp kernel.cu circuit.qasm -o hybrid_app \
          -cuda-arch sm_75 \
          -cuda-path /usr/local/cuda

    # If nvcc is in PATH, you can omit -cuda-path, it will be auto-detected
    qllvm main.cpp kernel.cu circuit.qasm -o hybrid_app -cuda-arch sm_86

    # Run
    ./hybrid_app -shots 1024

.. warning::
   QASM programs currently only support **OPENQASM 2.0** format specification, and do not support compiling QASM programs with multiple quantum registers.


.. _compilation-parameter-explanation:

Compilation Parameter Explanation
---------------------------------

This tutorial will introduce detailed explanations of qllvm compilation parameters.

.. _driver-program-qllvm-parameters:

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
     - Specify basis gate set
     - ``-basicgate=[rx,ry,rz,h,cz]``, ``-basicgate=[rx,ry,rz,h,cx]``, ``-basicgate=[su2,x,y,z,cz]`` (for measurement and control)
   * - `-qrt`
     - Specify device type
     - ``-qrt nisq``, ``-qrt ftqc``
   * - `-qpu`
     - Specify backend type
     - ``-qpu qasm-backend``
   * - `-qpu-config`
     - Specify backend topology structure (coupling graph)
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
     - Use C++ SABRE at LLVM IR stage (requires `-initial-mapping` and `-qpu-config`)
     - ``-sabre-cpp``
   * - `-circuit-state`
     - Print circuit state (depth, gate count)
     - ``-circuit-state``
   * - `-pass-count`
     - Print execution count of each Pass
     - ``-pass-count``
   * - `-v` / `--verbose`
     - Enable verbose output
     - ``-v``
   * - `-cuda-arch`
     - Specify GPU architecture for hybrid CUDA
     - ``-cuda-arch sm_75``
   * - `-cuda-path`
     - Specify CUDA installation path for hybrid CUDA (optional, defaults to `CUDA_PATH` or nvcc inference)
     - ``-cuda-path /usr/local/cuda``

**Common basis gate sets:**

- ``[rx,ry,rz,h,cz]``: Default
- ``[rx,ry,rz,h,cx]``: Use CX
- ``[su2,x,y,z,cz]``: For measurement and control systems

.. _qllvm-compile-parameters:

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
     - SABRE coupling graph, edge format `0,1;1,2;2,3`
   * - `-circuit-state`
     - Print circuit depth and gate count
   * - `-pass-count`
     - Print execution count of each Pass
   * - `-basicgate`
     - Basis gate set
   * - `-customPassSequence`
     - Custom Pass sequence file
   * - `-verbose-error`
     - Print full MLIR on error
   * - `--pass-timing`
     - Pass execution time statistics
   * - `--print-ir-after-all`
     - Print IR after each Pass
   * - `--print-ir-before-all`
     - Print IR before each Pass

.. _cmake-build-parameters:

CMake Build Parameters
~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: CMake Build Parameters
   :widths: 30 70
   :header-rows: 1

   * - Parameter
     - Description
   * - `-DLLVM_ROOT`
     - LLVM installation path (includes MLIR)
   * - `-DXACC_DIR`
     - Optional dependency path (antlr4/exprtk); Set to empty for QASM-only standalone build: `-DXACC_DIR=`
   * - `-DCMAKE_INSTALL_PREFIX`
     - Installation directory (default ~/.qllvm)
   * - `-DQLLVM_QASM_ONLY_BUILD=ON`
     - Enable QASM-only standalone build

.. _optional-dependencies-usage:

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~

QASM-Only Standalone Build
++++++++++++++++++++++++++

If you only need QASM compilation functionality without XACC dependencies, you can enable QASM-only standalone build:

.. code-block:: bash

    mkdir build && cd build
    cmake .. -DQLLVM_QASM_ONLY_BUILD=ON -DXACC_DIR= \
             -DLLVM_ROOT=/path/to/llvm \
             -DCMAKE_INSTALL_PREFIX=~/.qllvm
    make -j$(nproc)
    make install

This will only build the QASM frontend and related passes, without depending on XACC and its dependencies (antlr4, exprtk, etc.).
