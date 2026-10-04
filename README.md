# AI/ML Coursework Repository

This repository contains coursework, notebooks, datasets, and project work for the
AI/ML program. Major areas include ANN, classification, regression, feature
engineering, text mining, unsupervised learning, the MCP project, and the final
loan-risk assessment project.

## Local development

Use the root virtual environment for general Python and Jupyter work:

```zsh
source .venv/bin/activate
python -m pip install -r Project_Final/requirements.txt
```

The selected VS Code interpreter is `.venv/bin/python`. Choose it as the notebook
kernel when opening a notebook for the first time.

Useful VS Code tasks are included:

- `Start Project_Final demo`: starts the FastAPI and Streamlit demo.
- `Start JupyterLab`: starts JupyterLab from the repository root.

Project-specific dependencies remain in their own `requirements.txt` or
`pyproject.toml` files. Install only the dependencies for the project you are
working on instead of combining every project's packages into one requirements file.

## Git workflow

Use the VS Code Source Control panel, or run:

```zsh
git status
git add <files>
git commit -m "Describe the change"
git push
```

The workspace is configured to use the working Apple Git binary on this Mac.

## Repository policy

Commit source code, notebooks, documentation, small sample data, dependency files,
and reproducible configuration. Keep virtual environments, notebook checkpoints,
bytecode, credentials, operating-system files, and generated model artifacts local.

Keep files at or below 10 MB in Git. Put larger local-only inputs under
`data/local/` or the relevant ignored project directory, and document how to
obtain them when a notebook or app needs them.
