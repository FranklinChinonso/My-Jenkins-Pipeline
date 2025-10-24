# simple-pipeline

Simple Python project demonstrating a basic Jenkins CI/CD pipeline.

## Files
- `app.py` - small Python module with `reverse_and_upper(s)` function and a `main()` entrypoint.
- `test_app.py` - pytest tests for the function.
- `requirements.txt` - project dependencies (pytest).
- `Jenkinsfile` - Declarative Jenkins pipeline.

## Pipeline stages (Jenkinsfile)
1. **Checkout** – Jenkins pulls the source code from the Git repository.
2. **Build** – Creates a Python virtual environment and installs dependencies from `requirements.txt`.
3. **Test** – Runs automated tests using `pytest`.
4. **Deploy** – Simulated deploy stage that prints “Deployment successful (simulated)”.

## How to run locally (PowerShell)
1. Create venv: `python -m venv venv`
2. Activate: `.\venv\Scripts\Activate` (Windows) or `. venv/bin/activate` (Linux/macOS)
3. Install deps: `pip install -r requirements.txt`
4. Run app: `python .\app.py`
5. Run tests: `pytest -q`

## Notes
- Replace the Jenkinsfile steps with `bat` instead of `sh` if using Windows Jenkins agents.
- This repository is intended for learning CI/CD with Jenkins.
