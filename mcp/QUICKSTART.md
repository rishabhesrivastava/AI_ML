# Gmail MCP Server - Quick Start Guide

## 🚀 5-Minute Setup

### Step 1: Get Google Credentials (5 min)

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable Gmail API:
   - Click "APIs & Services" → "Library"
   - Search "Gmail API" and click "Enable"
4. Create OAuth credentials:
   - Click "Credentials" → "Create Credentials" → "OAuth 2.0 Client ID"
   - Choose "Desktop application"
   - Download as JSON
5. Save the file as `credentials.json` in the project root

### Step 2: Set Up the Project (2 min)

```bash
# Navigate to the project directory
cd /Users/krishna/Desktop/Workspace/BITS_PILANI/Code_workspace/mcp

# Create virtual environment (if using uv)
uv venv
source .venv/bin/activate

# Install dependencies
uv sync
# OR with pip:
pip install -r requirements.txt
```

### Step 3: Test the Server (1 min)

```bash
# Run with MCP Inspector (best for testing)
uv run mcp dev gmail_mcp_server/server.py

# Opens at http://localhost:5173 - you can test all tools here!
```

That's it! 🎉

## 📋 Common Tasks

### Send an Email
```
Use the send_email tool with:
- to: recipient@example.com
- subject: Hello World
- body: <p>This is my email body</p>
```

### Search for Emails
```
Use search_emails tool with queries like:
- from:sender@example.com
- has:attachment
- is:unread
- subject:important
```

### Get Recent Emails
```
Use list_emails with max_results: 20
```

## 🔗 Integration Options

### With Claude Desktop
```bash
uv run mcp install gmail_mcp_server/server.py --name "Gmail"
```

### With VS Code
- Use the provided `.vscode/mcp.json` configuration
- Press Cmd+Shift+P and search for "MCP"

## 📚 Need Help?

See full documentation in `README.md`

Common issues:
- **Can't find credentials.json?** Make sure it's in the project root
- **Import errors?** Run `uv sync` to reinstall dependencies
- **Authentication fails?** Delete `token.json` and try again
