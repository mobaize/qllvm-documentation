Contribution Guide
======================

Thank you for your interest and support for the QLLVM project! We welcome contributions in various forms, including code, documentation, testing, issue reports, etc. This guide will help you understand how to contribute to the QLLVM project.

Code of Conduct
------------------

All contributors participating in the QLLVM project should adhere to the following code of conduct:

- Respect others, maintain a friendly and professional attitude
- Accept constructive criticism
- Focus on the best interests of the community
- Show empathy to other contributors

How to Contribute
------------------

Reporting Issues
------------------

If you find a bug or have a new feature suggestion, please submit an `Issue <https://github.com/QCFlow/QLLVM/issues>`_ on GitHub. When submitting an Issue, please provide the following information:

- Detailed description of the issue
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Environment information (operating system, Python version, QLLVM version, etc.)
- Related error messages or logs

Contributing Code
------------------

Extension Development Guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _extension-development-guide:

Before submitting code, please refer to the following development guides based on your contribution type.

.. _add-new-pass:

Adding MLIR Optimization Pass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1. Create Pass Source Files**

Add new optimization Pass source code under ``qllvm/mlir/transforms/optimizations/``.

- **new.hpp Example**

  .. code-block:: cpp
     :caption: qllvm/mlir/transforms/optimizations/new.hpp
     :linenos:

     #pragma once
     #include "Quantum/QuantumOps.h"
     #include "mlir/Pass/Pass.h"
     #include "mlir/Pass/PassManager.h"
     #include "mlir/Target/LLVMIR.h"
     #include "mlir/Transforms/DialectConversion.h"
     #include "mlir/Transforms/Passes.h"
     #include <unordered_map>
     #include <tr1/unordered_map>
     #include <iostream>
     #include <unordered_set>
     
     using namespace mlir;
     
     namespace qllvm {
     struct new
         : public PassWrapper<new, OperationPass<ModuleOp>> {
       void getDependentDialects(DialectRegistry &registry) const override;
       void runOnOperation() final;
       new() {};
       new(std::unordered_set<std::string> basicgate){
         basic_gate = basicgate;
       }
       new(std::map<std::string, bool> bool_args,int &opt_count, int &opt_depth, int &cir_depth, int &zero_count, int &enable, int &pass_count) {
         if(bool_args.find("pass_effect") != bool_args.end()){
           printCountAndDepth = false;
           p = &opt_count;
           q = &opt_depth;
           c_d = &cir_depth;
         }
         if(bool_args.find("syn_opt") != bool_args.end()||bool_args.find("customPassSequence") != bool_args.end()){
           syn = true;
           o = &zero_count;
           e = &enable;
           c_d = &cir_depth;
         }
         if(bool_args.find("pass_count") != bool_args.end()){
           c = &pass_count;
           f = true;
         }
       }
     
       private:
       bool printCountAndDepth = false;
       bool syn = false;
       bool f = false;
       int *p = nullptr;
       int *q = nullptr;
       int *o = nullptr;
       int *e = nullptr;
       int *c = nullptr;
       int *c_d = nullptr;
       int before_gate_count = 0;
       int before_circuit_depth = 0;
       int after_gate_count = 0;
       int after_circuit_depth = 0;
       std::unordered_set<std::string> basic_gate;
       std::vector<mlir::quantum::ValueSemanticsInstOp> top_op;
       std::string passname = "new";
     };
     }

- **new.cpp Example**

  .. code-block:: cpp
     :caption: qllvm/mlir/transforms/optimizations/new.cpp
     :linenos:

     #include "new.hpp"  
     #include "Quantum/QuantumOps.h"  
     #include "mlir/Dialect/LLVMIR/LLVMDialect.h"  
     #include "mlir/Dialect/StandardOps/IR/Ops.h"  
     #include "mlir/IR/Matchers.h"  
     #include "mlir/IR/PatternMatch.h"  
     #include "mlir/Pass/Pass.h"  
     #include "mlir/Pass/PassManager.h"  
     #include "mlir/Target/LLVMIR.h"  
     #include "mlir/Transforms/DialectConversion.h"  
     #include "mlir/Transforms/Passes.h"  
     
     namespace qllvm {  
     using namespace std::complex_literals;  
     
     void new::getDependentDialects(DialectRegistry &registry) const {  
       registry.insert<LLVM::LLVMDialect>();  
     }  
         
     void new::runOnOperation() {  
         
     }  
     }

**2. Mount to PassManager**

In ``qllvm/mlir/transforms/pass_manager.hpp``, mount the new Pass to ``mlir::PassManager`` in the ``configureOptimizationPasses`` function.

The compiler supports two configuration methods:

- **Default order**: Custom sequence based on ``PassManagerOptions`` (e.g., ``customPassSequence``)
- **Default enabled**: Directly call ``addPass`` in the default branch
- **Optional enabled**: Extend according to existing macros and ``switch`` patterns

**Method 1: Default Enabled**

Add in ``configureOptimizationPasses``:

.. code-block:: cpp

   passManager.addPass(std::make_unique<new>());

.. image:: image/010.png
   :align: center
   :width: 80%

**Method 2: Optional Enabled (via macros and switch)**

- Define macro: Add ``#define NEW 12`` in ``pass_manager.hpp``

.. image:: image/011.png
   :align: center
   :width: 80%

- Add ``"NEW"`` to ``passNames``

- Add corresponding ``case`` branch in the ``for`` loop

.. image:: image/012.png
   :align: center
   :width: 80%

.. _add-new-language:

Adding Input Language Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1. Implement Parser**

Create language subdirectory under ``qllvm/mlir/parsers/``:

- Write ANTLR grammar file (``.g4``) and generate lexer/parser code
- Implement Visitor and ``*_mlir_generator`` to gradually lower AST to MLIR
- Refer to existing implementations: ``qasm3/``, ``qiskit/``, ``qcis/``

.. image:: image/013.png
   :align: center
   :width: 80%

|

.. warning::
   QASM programs currently only support **OPENQASM 2.0** format specification, and do not support compiling QASM programs with multiple quantum registers.

**2. Add Routing**

Add routing in ``loadMLIR`` in ``qllvm/mlir/tools/qllvm-mlir-helper.hpp``:

- Extend ``SourceLanguage`` enum
- Select corresponding generation function by file content, extension, or invocation parameters
- Return ``OwningModuleRef`` and unified ``MlirGenerationResult`` semantics

.. image:: image/014.png
   :align: center
   :width: 80%

.. _add-new-backend:

Adding Backend Type
^^^^^^^^^^^^^^^^^^^

**1. Implement Backend Logic**

Implement the backend's ``emit`` method (QIR to target representation conversion) in ``qllvm/backend/backends/``, alongside existing backends like ``QasmBackend``, ``TianyanBackend``, etc.

.. image:: image/015.png
   :align: center
   :width: 80%

**2. Declare Backend Class**

Declare the corresponding backend class in ``qllvm/backend/include/qllvm/backends/``.

.. image:: image/016.png
   :align: center
   :width: 80%

**3. Register Backend**

Register in ``registerBuiltinBackends()`` in ``qllvm/backend/BackendRegistry.cpp``:

.. code-block:: cpp

   BackendRegistry::instance().registerBackend(
       std::make_unique<YourBackend>());

.. image:: image/017.png
   :align: center
   :width: 80%

After registration, the implementation can be resolved by name at runtime.

.. note::
   New files typically need to add compilation targets and link dependencies in relevant ``CMakeLists.txt``.


.. _submitting-pull-request:

Submitting Pull Request
^^^^^^^^^^^^^^^^^^^^^^^

After completing code modifications, follow these steps to submit your contribution.

- **Fork repository**: Fork the QLLVM repository to your personal account on GitHub

- **Clone and create branch**

   .. code-block:: bash

      git clone https://github.com/your-username/QLLVM.git
      cd qllvm
      git checkout -b feature/your-feature-name

- **Install development dependencies**

   .. code-block:: bash

      pip install -e .[dev]

- **Make modifications and test**

   .. code-block:: bash

      pytest

- **Commit and push**

   .. code-block:: bash

      git add .
      git commit -m "Add feature: brief description"
      git push origin feature/your-feature-name

- **Create Pull Request**: Create a PR on GitHub, clearly describing your changes, and wait for maintainers to review

.. tip::
   - Maintain consistent code style with the project
   - Add appropriate test cases
   - Use clear, standardized commit messages

Contributing Documentation
-------------------------------

If you want to contribute documentation, please follow these steps:

1. Fork and clone the repository (same as code contribution steps 1-2)

2. Create a branch (same as code contribution step 3)

3. **Install documentation dependencies**

   * Install documentation building dependencies

.. code-block:: bash

    pip install -e .[docs]

4. **Modify documentation**

   * Modify or add documentation content
   * Ensure consistent documentation style
   * Check if links are valid

5. **Build documentation**

   * Build documentation to ensure no errors

.. code-block:: bash

    cd docs
    make html

6. Commit changes (same as code contribution steps 7-9)

Contributing Tests
-------------------------------





If you want to contribute tests, please follow these steps:

1. Fork and clone the repository (same as code contribution steps 1-2)

2. Create a branch (same as code contribution step 3)

3. **Install test dependencies**

   * Install test dependencies

4. **Add tests**

   * Add new test cases
   * Ensure tests cover new features or fixed bugs

5. **Run tests**

   * Run tests to ensure they pass

6. Commit changes (same as code contribution steps 7-9)

Code Style
------------------

The QLLVM project follows the following code style:

- **Python code**: Follow PEP 8 guidelines
  - Use 4 spaces for indentation
  - Line length does not exceed 79 characters
  - Import order: standard library, third-party libraries, local modules
  - Use docstrings to document functions and classes

- **Documentation**: Follow reStructuredText format
  - Use clear heading hierarchy
  - Code examples use correct syntax highlighting
  - Links use relative paths

- **Commit messages**: Use clear commit messages
  - First line: short description (no more than 50 characters)
  - Empty line
  - Detailed description (if needed)
  - Reference related Issues (if any)


Communication Channels
------------------------------

- **GitHub Issues**: For reporting issues and discussing features
- **GitHub Discussions**: For discussing project-related topics
- **Mailing list**: If there is a mailing list, please provide it here

Contributor Guide
---------------------------

First Contribution
~~~~~~~~~~~~~~~~~~~~~~~~~

If you are contributing to an open source project for the first time, the following resources may be helpful:

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [First Contributions](https://firstcontributions.github.io/)
- [GitHub Docs: Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

Code Review
~~~~~~~~~~~~~~~~~

All Pull Requests will go through code review. During the review process, you may need to make modifications based on review comments. Please be patient and open-minded, as code review is an important part of improving code quality.

License
~~~~~~~~~~~~~

By contributing code to the QLLVM project, you agree that your contributions will be released under the project's license.

Acknowledgements
------------------------

Thank you to all who have contributed to the QLLVM project! Your contributions are key to the project's success.