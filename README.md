If you use cursor make sure to Disable Cursor Tab to avoid autocorrection
If you use VS Code make sure to disable Copilot


Make sure your Python is at least 3.10
```
python --version
```

run

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

run and make sure that mypy shows errors
```
mypy exercises/1_broken_greetings.py
```
