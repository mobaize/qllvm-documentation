.. QLLVM documentation master file, created by
   sphinx-quickstart on Mon Mar  9 10:59:14 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



.. image:: ../image/QLLVM0.0.png
   :align: center

QLLVM Documentation
===================
Welcome to the QLLVM project documentation! This documentation provides installation guides, usage tutorials, API references, and other content to help you get started with and deeply understand QLLVM.

QLLVM is a quantum program compilation framework built on **MLIR** and **LLVM IR**. It supports multiple quantum programming language inputs, and outputs code supported by target hardware after optimization and mapping. We provide two usage methods: command-line execution through source code installation and quick execution using VSCode plugins.

.. toctree::
   :maxdepth: 2
   :caption: Documentation Navigation:

   quickstart.en
   installation.en
   tutorials.en
   api.en
   contributing.en

About QLLVM
===========

QLLVM quantum compilation framework is a quantum program compilation framework built on **MLIR** and **LLVM IR**. The framework adopts a three-stage design of front-end, middle-end, and back-end, supporting multiple quantum programming language inputs, and outputting code supported by target hardware after optimization and mapping.

Overall Features
----------------

QLLVM compiles high-level quantum programs into target back-end executable code, with the following main features:

* **Multi-language front-end**: Supports OpenQASM 2.0/3.0, Qiskit QuantumCircuit, Q# and other inputs
* **MLIR optimization**: Single-qubit gate merging, cancellation, diagonal gate removal, gate synthesis and other optimization passes
* **QIR generation**: Lowering MLIR dialects to QIR (quantum intermediate representation in LLVM IR form)
* **SABRE mapping**: C++/Qiskit implementation of qubit layout and SWAP insertion
* **Multi-backend emission**: Output OpenQASM, hardware-specific formats, etc.

**Compilation pipeline:**
```
QASM source file → Preprocessing → MLIR (Quantum dialect) → Optimization Passes → Lowering → LLVM IR (QIR) → Backend emission
```

Technical Route
---------------

* **Front-end**: Responsible for language parsing and intermediate code generation, converting high-level languages to MLIR Quantum dialect
* **Middle-end**: Perform quantum program optimization based on MLIR, and further lower MLIR to QIR (LLVM IR)
* **Back-end**: Based on QIR and QIR runtime library, convert programs to code formats supported by target hardware

Key Advantages
--------------

1. **Industrial-grade IR infrastructure**: Based on MLIR/LLVM, easy to extend new dialects and new passes
2. **Multiple input forms**: OpenQASM, Qiskit, Q# etc., adapting to different programming habits
3. **Flexible optimization**: -O0/-O1 levels, custom pass sequences, synthesis optimization
4. **Physical constraint mapping**: SABRE and other layout and SWAP strategies, adapting to real hardware topology

Quick Start
-----------

1. **Use Plugins (Recommended)**: 

   - **Quantum Circuit Composer**: VSCode extension that allows you to use QLLVM compiler without local installation. Supports multi-compiler parallel compilation, QIR simulator running, and other features.

   - **Qcoder**: VSCode sidebar AI assistant focused on quantum algorithms, quantum circuits, and toolchain issues, providing intelligent dialogue and code insertion capabilities.

   For more details, please refer to the :doc:`quickstart.en` guide.

2. **Install QLLVM**: Refer to the :doc:`installation.en` guide to install QLLVM
3. **Learn usage methods**: Check the tutorials in :doc:`tutorials.en`
4. **Consult API documentation**: Refer to :doc:`api.en` for detailed API information
5. **Contribute code**: If you want to contribute code, please refer to the :doc:`contributing.en` guide

Get Help
--------

If you encounter problems when using QLLVM, you can get help through the following methods:

* Submit an `Issue <https://github.com/QCFlow/QLLVM/issues>`_ on GitHub
* Contact the project maintainers