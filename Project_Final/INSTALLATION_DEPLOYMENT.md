# Loan Risk Assessment

## System Requirements

- Windows 10/11, 64-bit
- Python 3.11, 64-bit, and PowerShell
- Internet access to install Python packages
- Ports 8000 and 8501 available

## Install (Windows)

Open PowerShell in this folder:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

```powershell
.\run_services.ps1
```

Streamlit: http://localhost:8501
API docs: http://localhost:8000/docs

Stop each service with `Ctrl+C` in its terminal.

## Run (macOS)

This workspace includes a macOS launcher. It starts both services and stops the API
when you press `Ctrl+C`.

```zsh
chmod +x run_services_macos.sh
./run_services_macos.sh
```

The launcher uses the repository-level Python environment at `../.venv`. This
keeps notebooks and the demo on the same default VS Code interpreter. To use
another environment, set `PROJECT_FINAL_PYTHON` to its `bin/python` path:

```zsh
PROJECT_FINAL_PYTHON=/absolute/path/to/venv/bin/python ./run_services_macos.sh
```

## Generate the Model (On Demand)

The trained `loan_model_artifacts.joblib` is included. Training is not part of install or startup. To generate or retrain it, from this folder run:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-training.txt
.\.venv\Scripts\python.exe -m nbconvert --to notebook --execute train_model.ipynb --output train_model.executed
```

This writes `loan_model_artifacts.joblib` in this folder. Restart the services after retraining.

## Production

The launcher binds to `127.0.0.1` for local use. For hosted deployment, use a process manager and secured HTTPS reverse proxy; protect the API with authentication. Recreate `.venv` on the deployment machine instead of copying it.

## Key Files

- `streamlit_app.py`: Streamlit interface.
- `risk_api.py`: FastAPI risk-assessment endpoint.
- `run_services.ps1`: Starts both local services.
- `train_model.ipynb`: On-demand model training.
- `loan_model_artifacts.joblib`: Trained model and preprocessing data.
- `Loan_default.csv`: Training dataset.
- `requirements.txt` / `requirements-training.txt`: App and training dependencies.
