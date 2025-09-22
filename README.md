# Setup Instructions

## Step 0
Install the uv package manager:

```
pip install uv
```

## Step 1
Run `uv init` to initialize the project.

## Step 2
Run `uv venv` to create a virtual environment.

## Step 3
Create or update `requirements.txt` with your dependencies.

## Step 4
Install dependencies:

```
uv pip install -r requirements.txt
```

## Step 5
Activate the virtual environment (if not already activated):

- On Windows (PowerShell):
  ```
  .\.venv\Scripts\Activate.ps1
  ```
- On macOS/Linux:
  ```
  source .venv/bin/activate
  ```

## Step 6
Run the MCP server:

```
python calcserver.py
```

## Step 7
Run the client to test math operations:

```
python client.py
```

---

You may need to update the server/client ports in the code to match your setup. Ensure the MCP server is running before starting the client.

