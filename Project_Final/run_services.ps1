$ErrorActionPreference = "Stop"
$ProjectDir = $PSScriptRoot
$PythonPath = Join-Path $ProjectDir ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $PythonPath -PathType Leaf)) {
    throw "Project virtual environment not found. Follow INSTALLATION_DEPLOYMENT.md to create it and install dependencies."
}

foreach ($requiredFile in @(
    (Join-Path $ProjectDir "risk_api.py"),
    (Join-Path $ProjectDir "streamlit_app.py"),
    (Join-Path $ProjectDir "loan_model_artifacts.joblib")
)) {
    if (-not (Test-Path -LiteralPath $requiredFile -PathType Leaf)) {
        throw "Required file not found: $requiredFile"
    }
}

foreach ($port in @(8000, 8501)) {
    $listener = Get-NetTCPConnection -State Listen -LocalPort $port -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($listener) {
        throw "Port $port is already in use by PID $($listener.OwningProcess). Stop that process before starting these services."
    }
}

$apiProcess = Start-Process -FilePath $PythonPath `
    -ArgumentList @("-m", "uvicorn", "risk_api:app", "--host", "127.0.0.1", "--port", "8000") `
    -WorkingDirectory $ProjectDir -PassThru

$streamlitProcess = Start-Process -FilePath $PythonPath `
    -ArgumentList @("-m", "streamlit", "run", "streamlit_app.py", "--server.address", "127.0.0.1", "--server.port", "8501") `
    -WorkingDirectory $ProjectDir -PassThru

Write-Host "Streamlit PID: $($streamlitProcess.Id)"
Write-Host "Risk API PID: $($apiProcess.Id)"
Write-Host "Streamlit: http://localhost:8501/"
Write-Host "API docs:  http://localhost:8000/docs"