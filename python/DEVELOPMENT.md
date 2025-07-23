# Pixel-Canon: Python Development Guide

This directory contains the Python implementation of the Pixel-Canon specification and its packaging configuration (`pyproject.toml`).

## Development Setup

To work on this package locally, it is recommended to install it in "editable" mode inside a virtual environment.

1.  **Navigate to this directory:**
    ```bash
    cd path/to/pixel-canon/python
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # ... (инструкции для разных ОС) ...
    ```

3.  **Install the package in editable mode:**
    ```bash
    pip install -e .
    ```
    To install extras:
    ```bash
    pip install -e ".[numpy]"
    ```

## Running Tests

From this directory (`pixel-canon/python`), run the following command:

```bash
python -m unittest discover -s tests
```

## Publishing to PyPI

From this directory (`pixel-canon/python`):

1.  **Install build tools:** `pip install build twine`
2.  **Build:** `python -m build`
3.  **Upload:** `python -m twine upload dist/*`

