# Python Project Testing Guide

This repository contains Python modules organized into separate directories, each with its own set of tests. The tests are written using `pytest` and are located in the `tests/` directories of each module.

## Project Structure

```
python
python/
  - mathlib/
    - plotting.py
    - tests/
      - test_plotting.py
  - other_module/
    - other_file.py
    - tests/
      - test_other_file.py
```

### Prerequisites

1. Install `pytest` if you haven't already:

    ```bash
    pip install pytest
    ```

2. Ensure that your `PYTHONPATH` includes the `python/` directory, so that the modules can be correctly imported in the tests:

    On Linux/macOS:
    ```bash
    export PYTHONPATH="$PYTHONPATH:$(pwd)"
    ```

    On Windows:
    ```bash
    set PYTHONPATH=%PYTHONPATH%;%CD%
    ```

## Running All Tests

To run all tests in the `python/` directory, navigate to the `python/` directory and run:

```bash
pytest
```

This will automatically discover and run all test files in the project.

## Running Tests for a Specific Module

You can also run tests for a specific module by specifying the path to its `tests/` directory.

### Running Tests for `mathlib`

To run tests for the `mathlib` module:

```bash
pytest mathlib/tests/
```

### Running Tests for `other_module`

To run tests for the `other_module` module:

```bash
pytest other_module/tests/
```

## Running a Specific Test

You can run a specific test function inside a test file by specifying the test file and the test function:

```bash
pytest path/to/test_file.py::test_function_name
```

For example, to run the `test_plotting` function from the `test_plotting.py` file:

```bash
pytest mathlib/tests/test_plotting.py::test_plot_function
```

## Viewing Detailed Output

For more detailed output during the test run, use the `-v` (verbose) flag:

```bash
pytest -v
```

## Generating Test Coverage Reports (Optional)

To check how much of your code is covered by tests, you can use `pytest-cov`. First, install it:

```bash
pip install pytest-cov
```

Then, run it with the following command:

```bash
pytest --cov=mathlib --cov=other_module
```

This will show you the test coverage for each module.

---
