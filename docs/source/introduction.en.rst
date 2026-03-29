QLLVM Introduction
==================

* QLLVM is a classical-quantum hybrid compilation framework built on LLVM, with excellent extensibility and seamless integration with classical high-performance computing ecosystems.

* QLLVM supports multiple quantum programming languages and backends, including Qiskit, OpenQASM, QPanda, Cirq, etc. for programming languages, and qasm simulator, Benyuan quantum computer, China Telecom "Tianyan" quantum computer, etc. for target backends.

* QLLVM supports unified compilation of quantum programs, CUDA programs, and classical C++ programs, providing an efficient, flexible, and industrial-grade compilation infrastructure for future classical-quantum software development.

Overall Features
----------------

QLLVM compiles high-level quantum programs into target back-end executable code, with the following main features:

* **Multi-language front-end**: Supports OpenQASM 2.0/3.0, Qiskit QuantumCircuit, QPanda, Cirq and other inputs
* **MLIR optimization**: Single-qubit gate merging, cancellation, diagonal gate removal, gate synthesis and other optimization passes
* **QIR generation**: Lowering MLIR dialects to QIR (quantum intermediate representation in LLVM IR form)
* **SABRE mapping**: C++/Qiskit implementation of qubit layout and SWAP insertion
* **Multi-backend emission**: Output OpenQASM, hardware-specific formats, etc.


Technical Route
---------------

.. image:: image/001.png
   :align: center
   :width: 80%

.. centered:: QLLVM Compilation Framework

* **Front-end**: Responsible for language parsing and intermediate code generation, converting high-level languages to MLIR Quantum dialect
* **Middle-end**: Perform quantum program optimization based on MLIR, and further lower MLIR to QIR (LLVM IR)
* **Back-end**: Based on QIR and QIR runtime library, convert programs to code formats supported by target hardware

Leveraging the LLVM ecosystem, QLLVM can integrate with classical compilation passes, CUDA programming models, and HPC runtimes, enabling efficient compilation of classical-quantum hybrid tasks.

.. image:: image/02.png
   :align: center
   :width: 100%

.. centered:: Classical-Quantum Hybrid Program Compilation Mechanism

Meanwhile, based on the LLVM compilation framework, the QLLVM compiler can work synergistically with various classical high-performance compilers, thus supporting the compilation of classical-quantum hybrid programs.

.. image:: image/003.png
   :align: center
   :width: 100%

.. centered:: Hybrid Program Code Writing Example

Key Advantages
--------------

1. **Industrial-grade IR infrastructure**: Based on MLIR/LLVM, easy to extend new dialects and new passes
2. **Multiple input forms**: OpenQASM, Qiskit etc., adapting to different programming habits
3. **Flexible optimization**: -O0/-O1 levels, custom pass sequences, synthesis optimization
4. **Physical constraint mapping**: SABRE and other layout and SWAP strategies, adapting to real hardware topology

Project Structure Overview
--------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Directory
     - Description
   * - ``mlir/``
     - MLIR dialects, parsers, transforms, lowerings
   * - ``mlir/dialect/``
     - Quantum dialect definition
   * - ``mlir/parsers/``
     - OpenQASM3, Qiskit parsers
   * - ``mlir/transforms/``
     - Optimization passes (gate merging, cancellation, synthesis, etc.)
   * - ``mlir/tools/``
     - ``qllvm-compile`` main compiler
   * - ``passes/``
     - LLVM IR passes (SABRE, etc.)
   * - ``backend/``
     - QIR → backend code (e.g., QasmBackend)
   * - ``tools/driver/``
     - Driver script ``qllvm.in``
   * - ``test/``
     - Tests and example QASM
   * - ``docs/``
     - Installation guides, design documents