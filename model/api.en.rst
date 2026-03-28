QLLVM Quantum Compilation Framework
====================================

QLLVM quantum compilation framework is a quantum program compilation framework built on MLIR and LLVM IR. The framework adopts a three-stage design of front-end, middle-end, and back-end, supporting multiple quantum programming language inputs, and outputting code supported by target hardware after optimization and mapping.

Software Introduction
--------------------

.. list-table:: QLLVM compiles high-level quantum programs into target back-end executable code, with the following main features:
   :widths: 20 40
   :header-rows: 1

   * - Function Module
     - Description
   * - `Multi-language front-end`
     - Supports OpenQASM 2.0/3.0, Qiskit QuantumCircuit, Q# and other inputs
   * - `MLIR optimization`
     - Single-qubit gate merging, cancellation, diagonal gate removal, gate synthesis and other optimization passes
   * - `QIR generation`
     - Lowering MLIR dialects to QIR (quantum intermediate representation in LLVM IR form)
   * - `SABRE mapping`
     - C++/Qiskit implementation of qubit layout and SWAP insertion
   * - `Multi-backend emission`
     - Output OpenQASM, hardware-specific formats, etc.

Compilation Pipeline
--------------------
``QASM source file → Preprocessing → MLIR (Quantum dialect) → Optimization Passes → Lowering → LLVM IR (QIR) → Backend emission``

Technical Route
---------------
1. Front-end: Responsible for language parsing and intermediate code generation, converting high-level languages to MLIR Quantum dialect
2. Middle-end: Perform quantum program optimization based on MLIR, and further lower MLIR to QIR (LLVM IR)
3. Back-end: Based on QIR and QIR runtime library, convert programs to code formats supported by target hardware

Key Advantages
---------------
1. Industrial-grade IR infrastructure: Based on MLIR/LLVM, easy to extend new dialects and new passes
2. Multiple input forms: OpenQASM, Qiskit, Q# etc., adapting to different programming habits
3. Flexible optimization: -O0/-O1 levels, custom pass sequences, synthesis optimization
4. Physical constraint mapping: SABRE and other layout and SWAP strategies, adapting to real hardware topology

Optional Dependencies
--------------------

QIR Runner Backend
~~~~~~~~~~~~~~~~~~

Output LLVM bitcode (.bc) for QIR Runner simulator loading. qllvm has built-in **QirRunnerCompat** to automatically adapt to qir-runner's QIR base profile (`__quantum__rt__initialize` signature, `__body` suffix, mz result index, etc.).

.. code-block:: bash

    # 1. Install qir-runner (conda qllvm environment)
    conda activate qllvm
    pip install qirrunner

    # 2. Generate .bc with qllvm-compile
    qllvm-compile bell.qasm -qrt nisq -qpu qir-runner -O1 \
      -emit-backend=qir-runner -output-path=bell.bc

    # 3. Run with qir-runner
    qir-runner -f bell.bc -s 5

**qir-runner Output Format Explanation**

Output structure for each shot:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Line
     - Meaning
   * - `START`
     - Start of a shot
   * - `METADATA\tEntryPoint`
     - Entry point metadata
   * - `RESULT\t0` or `RESULT\t1`
     - Measurement results for each qubit (in measurement order)
   * - `END\t0`
     - End of the shot

**qir-runner Command Line Parameters**

.. list-table::
   :widths: 30 40 30
   :header-rows: 1

   * - Parameter
     - Description
     - Default Value
   * - `-f, --file <PATH>`
     - QIR bitcode file path (required)
     - -
   * - `-s, --shots <NUM>`
     - Number of simulated shots
     - 1
   * - `-r, --rngseed <NUM>`
     - Random number seed (reproducible)
     - Random
   * - `-e, --entrypoint <NAME>`
     - Entry function name
     - EntryPoint

**Output as Qiskit-style counts**

Use `scripts/qir_runner_counts.py` to convert raw output to Qiskit-style `get_counts()` dictionary:

.. code-block:: bash

    # Pipeline方式
    qir-runner -f bell.bc -s 100 | python3 scripts/qir_runner_counts.py -

    # Directly specify bc and parameters
    python3 scripts/qir_runner_counts.py bell.bc -s 100 -r 42

- **Output example (Bell state)**: `{'00': 48, '11': 52}`

- **Coordinated test script**: `./scripts/test_qllvm_qirrunner.sh`

.bc is standard LLVM bitcode, which can be loaded by tools such as [qir-alliance/qir-runner](https://github.com/qir-alliance/qir-runner) (requires Python 3.9+).

Classical-Quantum Hybrid Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Relying on the LLVM ecosystem, QLLVM can realize integration with classical compilation passes, CUDA programming model, and HPC runtime, thereby achieving efficient classical-quantum hybrid task compilation.

Supports hybrid compilation of C++ main program and QASM quantum circuit into a single executable file:

.. code-block:: bash

    # Hybrid compilation (qir-qrt-stub implementation)
    qllvm main.cpp circuit.qasm -o hybrid_app

    # Example located at examples/hybrid/
    qllvm examples/hybrid/main.cpp examples/hybrid/bell.qasm -o hybrid_bell
    ./hybrid_bell

**Using qir-runner as Simulator**

.. code-block:: bash

    # Hybrid compilation + qir-runner simulation (generate exe and .bc)
    qllvm main.cpp bell.qasm -qpu qir-runner -o hybrid_bell -O1

    # Run (requires qir-runner in PATH)
    ./hybrid_bell -shots 10

- **Workflow**: QASM → QIR .bc (qir-runner) + C++ compilation → Executable file indirectly calls qir-runner subprocess to simulate quantum circuit at runtime.

- **Coordinated test script**: `./scripts/test_hybrid_qirrunner.sh`

**C++ + CUDA + QASM Hybrid Compilation**

Supports hybrid compilation of C++ main program, CUDA kernel, and QASM quantum circuit into a single executable file (requires CUDA environment):

.. code-block:: bash

    cd examples/hybrid_cuda

    # Compile (-cuda-arch specifies GPU architecture, such as sm_75, sm_86)
    qllvm main.cpp kernel.cu circuit.qasm -o hybrid_app \
          -cuda-arch sm_75 \
          -cuda-path /usr/local/cuda

    # If nvcc is in PATH, -cuda-path can be omitted, it will be automatically deduced
    qllvm main.cpp kernel.cu circuit.qasm -o hybrid_app -cuda-arch sm_86

    # Run
    ./hybrid_app -shots 1024

- **Dependencies**: Clang (supports `-x cuda`), CUDA Toolkit, qir-runner (`pip install qirrunner`).

- **Ubuntu apt install CUDA**: Run `bash scripts/install_cuda_apt.sh` to automatically install nvidia-cuda-toolkit and create a Clang compatible directory (`~/.qllvm/cuda-apt-compat`).

QLLVM Usage Guide
------------------

1. Install QLLVM: Refer to the :doc:`installation.en` guide to learn how to install QLLVM.
2. Use QLLVM: Refer to the :doc:`tutorials.en` guide to learn how to use QLLVM to compile quantum circuits.