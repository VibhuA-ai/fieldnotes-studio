# Development Container Configuration

This directory contains the configuration for GitHub Codespaces and VS Code Dev Containers.

## What's Configured

- **Base Image**: Python 3.12 official dev container
- **Extensions**: 
  - Python language support
  - Pylance for IntelliSense
  - Python debugging
  - Jupyter notebooks support
  - Ruff formatter and linter
  - Code spell checker
- **Port Forwarding**: Port 8501 for Streamlit
- **Auto Setup**: Dependencies are automatically installed from `requirements.txt`

## Usage

### GitHub Codespaces

1. Navigate to the repository on GitHub
2. Click the "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main" (or your branch)

### VS Code Dev Containers

1. Install the "Dev Containers" extension in VS Code
2. Open the repository folder
3. Press F1 and select "Dev Containers: Reopen in Container"

## Running the Application

Once the container is ready:

```bash
streamlit run app.py
```

The Streamlit app will be accessible through the forwarded port 8501.
