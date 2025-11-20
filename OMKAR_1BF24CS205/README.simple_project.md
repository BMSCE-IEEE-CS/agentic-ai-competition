# Simple Project

This is a minimal Python project scaffold. Files live inside the
`OMKAR_1BF24CS205` folder.

Project layout (important files):

- `simple_project/__init__.py` — package init and `__version__`.
- `simple_project/cli.py` — `greet(name)` and CLI entry (`main`).
- `run.py` — tiny runner that calls `greet` (example runner).
- `requirements.txt` — runtime/test deps (e.g. `pytest`).
- `tests/test_cli.py` — a single `pytest` test for `greet`.

How to run (PowerShell) — minimal steps

1) (Optional but recommended) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies (if you want to run tests):

```powershell
pip install -r requirements.txt
```

3) Run the small app / CLI examples:

```powershell
# run the runner script (passes first arg as name)
python run.py
python run.py Alice

# run CLI as a module
python -m simple_project.cli --name Bob
```

Expected output:

- `python run.py Alice` prints:

```
Hello, Alice!
```

- `python -m simple_project.cli --name Bob` prints:

```
Hello, Bob!
```

4) Run tests with `pytest` (if installed):

```powershell
pytest -q
```

Expected test output (one passing test):

```
1 passed
```

Notes
- Make sure you run commands from inside the `OMKAR_1BF24CS205` folder so
  that Python can import the local `simple_project` package (or set `PYTHONPATH`).
- If you prefer not to create a virtualenv, you can run `python run.py Alice` directly,
  but installing `pytest` system-wide is not recommended.
# Simple Project

This is a minimal Python project scaffold added for demonstration.

Quick start (PowerShell):

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the CLI (examples):

```powershell
python run.py
python run.py Alice
python -m simple_project.cli --name Bob
```

4. Run tests:

```powershell
pytest -q
```
