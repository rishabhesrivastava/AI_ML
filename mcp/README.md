# Gmail MCP Server

A Model Context Protocol (MCP) server for seamless Gmail integration. This server provides tools to read, compose, search, and manage emails through the Gmail API.

## Features

- **List Emails**: Retrieve emails from your inbox with optional search filters
- **Get Email Details**: View full email content including subject, sender, body, and attachments
- **Send Emails**: Compose and send emails with HTML support
- **Search Emails**: Advanced search using Gmail search syntax
- **Manage Emails**: Mark as read, delete, and organize with labels
- **Get Labels**: Retrieve all your Gmail labels

## Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`
- Google Cloud Project with Gmail API enabled
- Gmail API credentials (OAuth 2.0)

## Installation

### 1. Clone or Download the Project

```bash
cd /Users/krishna/Desktop/Workspace/BITS_PILANI/Code_workspace/mcp
```

### 2. Set Up Python Environment

Using `uv` (recommended):

```bash
uv venv
source .venv/bin/activate
```

Or using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

### 3. Install Dependencies

Using `uv`:

```bash
uv add "mcp[cli]" google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
```

Or using pip:

```bash
pip install -r requirements.txt
```

## Google Cloud Setup

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable the Gmail API:
   - Go to "APIs & Services" > "Library"
   - Search for "Gmail API"
   - Click "Enable"

### 2. Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. Select "Desktop application"
4. Download the credentials as JSON
5. Save it as `credentials.json` in the project root

### 3. Configure Environment Variables

Copy `.env.example` to `.env` and update if needed:

```bash
cp .env.example .env
```

The `.env` file will contain:
```
GMAIL_CLIENT_ID=your-client-id.apps.googleusercontent.com
GMAIL_CLIENT_SECRET=your-client-secret
GMAIL_REDIRECT_URI=http://localhost:8000/callback
```

## Running the Server

### Development Mode with MCP Inspector

The fastest way to test the server:

```bash
uv run mcp dev gmail_mcp_server/server.py
```

This opens the MCP Inspector at `http://localhost:5173` where you can:
- Test all available tools
- View tool parameters and descriptions
- See responses in real-time

### Direct Execution

```bash
uv run gmail_mcp_server/server.py
```

### As a Script Entry Point

After installation, you can run:

```bash
gmail-mcp-server
```

## Using with Claude Desktop

To use the Gmail MCP server with Claude Desktop:

### 1. Install to Claude Desktop

```bash
uv run mcp install gmail_mcp_server/server.py --name "Gmail"
```

### 2. Manual Configuration

Or manually add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "servers": {
    "gmail-mcp-server": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "gmail-mcp-server"],
      "env": {
        "PYTHONPATH": "/path/to/mcp"
      }
    }
  }
}
```

## Using with VS Code

The project includes an `mcp.json` configuration file in the `.vscode` folder for VS Code's MCP support:

1. Open VS Code
2. Press `Cmd+Shift+P` and select "MCP: Add server..."
3. The gmail-mcp-server should appear as an available option

Or manually configure in your VS Code settings if needed.

## Available Tools

### 1. list_emails
List emails from your Gmail inbox.

**Parameters:**
- `query` (string, optional): Gmail search query (default: "")
- `max_results` (integer, optional): Maximum emails to return (default: 10)

**Returns:** List of emails with subject, sender, and snippet

### 2. get_email_details
Get complete details of a specific email.

**Parameters:**
- `message_id` (string, required): The Gmail message ID

**Returns:** Full email including subject, sender, recipient, date, and body

### 3. send_email
Send an email message.

**Parameters:**
- `to` (string, required): Recipient email address
- `subject` (string, required): Email subject line
- `body` (string, required): Email body (HTML supported)

**Returns:** Message ID if successful

### 4. mark_email_as_read
Mark an email as read.

**Parameters:**
- `message_id` (string, required): The Gmail message ID

**Returns:** Success status

### 5. delete_email
Delete an email message.

**Parameters:**
- `message_id` (string, required): The Gmail message ID

**Returns:** Success status

### 6. search_emails
Search emails using Gmail search syntax.

**Parameters:**
- `query` (string, required): Gmail search query
- `max_results` (integer, optional): Maximum results to return (default: 20)

**Returns:** List of matching emails

### 7. get_labels
Get all Gmail labels.

**Parameters:** None

**Returns:** List of all labels in your Gmail account

## Gmail Search Syntax Examples

```
from:user@example.com          # Emails from specific sender
to:user@example.com            # Emails to specific recipient
subject:important              # Search in subject line
has:attachment                 # Emails with attachments
filename:pdf                   # Attachments of specific type
is:starred                     # Starred emails
is:unread                      # Unread emails
after:2024/01/01               # Emails after date
before:2024/01/01              # Emails before date
label:label_name               # Emails with specific label
size>5M                        # Emails larger than 5MB
```

## Troubleshooting

### Authentication Issues

**Error: "credentials.json not found"**
- Ensure you've downloaded the credentials file from Google Cloud Console
- Place it in the project root as `credentials.json`

**Error: "Failed to authenticate with Gmail API"**
- Delete `token.json` if it exists to force re-authentication
- Ensure the Gmail API is enabled in your Google Cloud project
- Check that your credentials.json is valid

### Import Errors

If you get import errors:

```bash
# Reinstall dependencies
uv sync
# Or with pip
pip install -r requirements.txt
```

### Connection Issues

**Error: "Connection refused"**
- Ensure the server is running
- Check that the port (8000 by default) isn't in use

## Project Structure

```
mcp/
├── gmail_mcp_server/
│   ├── __init__.py           # Package initialization
│   ├── config.py             # Configuration settings
│   ├── gmail_client.py        # Gmail API wrapper
│   └── server.py             # MCP server implementation
├── .vscode/
│   └── mcp.json              # VS Code MCP configuration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

## Development

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black gmail_mcp_server/

# Lint code
ruff check gmail_mcp_server/
```

## API Documentation

For more information about the Gmail API, visit:
- [Gmail API Documentation](https://developers.google.com/gmail/api)
- [Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python)

## Model Context Protocol

For more information about MCP:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Security Note

⚠️ **Important Security Considerations:**

1. **Never commit credentials**: Always use `.env` files and add `credentials.json` and `token.json` to `.gitignore`
2. **Protect tokens**: The `token.json` file contains your Gmail access token - never share it
3. **Scope limitations**: This server requests Gmail API scopes that allow reading and modifying emails
4. **Environment variables**: Keep your `GMAIL_CLIENT_SECRET` confidential

## License

MIT

## Support

For issues or questions, please refer to:
- [MCP GitHub Issues](https://github.com/modelcontextprotocol)
- [Gmail API Support](https://support.google.com/code/contact/gmail_api_support)
