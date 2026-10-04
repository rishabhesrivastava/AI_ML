#!/usr/bin/env zsh
# Start the local Streamlit demo and FastAPI service on macOS.
set -euo pipefail

PROJECT_DIR="${0:A:h}"
REPO_DIR="${PROJECT_DIR:h}"
# Override this when the virtual environment lives somewhere else:
#   PROJECT_FINAL_PYTHON=/absolute/path/to/venv/bin/python ./run_services_macos.sh
DEFAULT_PYTHON="$REPO_DIR/.venv/bin/python"
PYTHON_BIN="${PROJECT_FINAL_PYTHON:-$DEFAULT_PYTHON}"

if [[ ! -x "$PYTHON_BIN" ]]; then
  print -u2 "Python interpreter not found: $PYTHON_BIN"
  exit 1
fi

if [[ ! -f "$PROJECT_DIR/loan_model_artifacts.joblib" ]]; then
  print -u2 "Missing trained model: $PROJECT_DIR/loan_model_artifacts.joblib"
  exit 1
fi

for port in 8000 8501; do
  if lsof -nP -iTCP:"$port" -sTCP:LISTEN >/dev/null 2>&1; then
    print -u2 "Port $port is already in use. Stop the existing service first."
    exit 1
  fi
done

cd "$PROJECT_DIR"
"$PYTHON_BIN" -m uvicorn risk_api:app --host 127.0.0.1 --port 8000 &
API_PID=$!

cleanup() {
  kill "$API_PID" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

print "API docs:  http://127.0.0.1:8000/docs"
print "Streamlit: http://127.0.0.1:8501"
print "Press Ctrl+C to stop both services."
"$PYTHON_BIN" -m streamlit run streamlit_app.py --server.address 127.0.0.1 --server.port 8501
