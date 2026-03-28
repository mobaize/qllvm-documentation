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

   introduction.en
   installation.en
   usage.en
   contributing.en

Quick Start
-----------

1. **Use Plugins (Recommended)**: 

   - **Quantum Circuit Composer**: VSCode extension that allows you to use QLLVM compiler without local installation. Supports multi-compiler parallel compilation, QIR simulator running, and other features.

   - **Qcoder**: VSCode sidebar AI assistant focused on quantum algorithms, quantum circuits, and toolchain issues, providing intelligent dialogue and code insertion capabilities.

   For more details, please refer to the usage examples section in the :doc:`usage.en` guide.

2. **Install QLLVM**: Refer to the :doc:`installation.en` guide to install QLLVM
3. **Learn usage methods**: Check the usage examples and compilation parameter explanations in :doc:`usage.en`
4. **Contribute code**: If you want to contribute code, please refer to the :doc:`contributing.en` guide

Get Help
--------

If you encounter problems when using QLLVM, you can get help through the following methods:

* Submit an `Issue <https://github.com/QCFlow/QLLVM/issues>`_ on GitHub
* Contact the project maintainers