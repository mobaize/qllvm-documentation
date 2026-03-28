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

If you want to contribute code, please follow these steps:

1. **Fork the repository**
   - Fork the QLLVM repository to your own account on GitHub

2. **Clone the repository**
   - Clone your forked repository to your local machine

.. code-block:: bash

    git clone https://github.com/QCFlow/QLLVM.git
    cd qllvm

3. **Create a branch**
   - Create a new branch for your modifications

.. code-block:: bash
   
    git checkout -b feature/your-feature-name

4. **Install development dependencies**
   - Install development dependencies

.. code-block:: bash

    pip install -e .[dev]

5. **Make modifications**
   - Make your code modifications
   - Ensure code style meets project requirements
   - Add appropriate tests

6. **Run tests**
   - Run tests to ensure your modifications do not break existing functionality

.. code-block:: bash

    pytest

7. **Commit changes**
   - Commit your changes with a clear commit message

.. code-block:: bash

    git add .
    git commit -m "Add feature: your feature description"

8. **Push branch**
   - Push your branch to GitHub

.. code-block:: bash

    git push origin feature/your-feature-name   

9. **Create Pull Request**
   - Create a Pull Request on GitHub, describing your changes
   - Wait for project maintainers to review

Contributing Documentation
-------------------------------

If you want to contribute documentation, please follow these steps:

1. Fork and clone the repository (same as code contribution steps 1-2)

2. Create a branch (same as code contribution step 3)

3. **Install documentation dependencies**
   - Install documentation building dependencies

.. code-block:: bash

    pip install -e .[docs]

4. **Modify documentation**
   - Modify or add documentation content
   - Ensure consistent documentation style
   - Check if links are valid

5. **Build documentation**
   - Build documentation to ensure no errors

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
   - Install test dependencies

4. **Add tests**
   - Add new test cases
   - Ensure tests cover new features or fixed bugs

5. **Run tests**
   - Run tests to ensure they pass

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