# Pixel-Canon: Python Implementation

This directory contains the Python implementation of the Pixel-Canon specification.

## Development Setup

To work on this package locally, it is recommended to install it in "editable" mode inside a virtual environment.

1.  **Navigate to this directory:**
    ```bash
    cd path/to/pixel-canon/python
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows (Command Prompt, cmd.exe):**
        ```cmd
        .venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell):**
        ```powershell
        # Если вы получаете ошибку о политике выполнения, сначала выполните:
        # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
        .venv\Scripts\Activate.ps1
        ```
    *   **macOS / Linux (bash/zsh):**
        ```bash
        source .venv/bin/activate
        ```

4.  **Install the package in editable mode:**
    This command will install the package and its dependencies, making it available system-wide (within the virtual environment) while allowing you to edit the source code directly.
    ```bash
    pip install -e .
    ```
    If you need the dependencies for running tests or specific backends, you can install them as extras:
    ```bash
    pip install -e ".[numpy]"
    ```

## Running Tests

From the root of the python directory (`pixel-canon/python`), run the following command:

```bash
python -m unittest discover -s tests
```

This command explicitly tells `unittest` to start discovery in the `tests` subdirectory, ensuring all tests are found and executed correctly.
