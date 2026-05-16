# Gmail MCP Server Development Guide

This is a Model Context Protocol (MCP) server for Gmail API integration. It provides tools for reading, composing, searching, and managing emails.

## Project Overview

- **Language**: Python 3.10+
- **Framework**: MCP SDK with FastMCP
- **External API**: Google Gmail API
- **Transport**: STDIO (default), can be extended to HTTP

## Key Files

- `gmail_mcp_server/server.py` - Main MCP server with 7 tools
- `gmail_mcp_server/gmail_client.py` - Gmail API wrapper
- `gmail_mcp_server/config.py` - Configuration management
- `.vscode/mcp.json` - VS Code MCP configuration
- `pyproject.toml` - Project dependencies and configuration

## Development Guidelines

### Adding New Tools

1. Add method to `GmailClient` class in `gmail_client.py`
2. Expose as tool using `@mcp.tool()` decorator in `server.py`
3. Include docstring with parameter descriptions
4. Test with `uv run mcp dev gmail_mcp_server/server.py`

### Tool Naming Convention

- Action verbs: `list_emails`, `get_email_details`, `send_email`, `mark_email_as_read`
- Search operations: `search_emails`
- Management: `get_labels`, `delete_email`

### Error Handling

All tools return a dictionary with:
- `"success"`: bool indicating success/failure
- `"error"`: error message if failed
- Data fields if successful

### Testing

```bash
# Development with MCP Inspector
uv run mcp dev gmail_mcp_server/server.py

# Direct execution
uv run gmail_mcp_server/server.py

# Install to Claude Desktop
uv run mcp install gmail_mcp_server/server.py --name "Gmail"
```

## Dependencies

Core dependencies are in `pyproject.toml`:
- `mcp>=1.0.0` - Model Context Protocol SDK
- `google-auth-oauthlib>=1.2.0` - Google OAuth authentication
- `google-api-python-client>=2.100.0` - Gmail API client
- `python-dotenv>=1.0.0` - Environment management

## Environment Setup

Required environment variables (see `.env.example`):
- `GMAIL_CLIENT_ID` - From Google Cloud Console
- `GMAIL_CLIENT_SECRET` - From Google Cloud Console
- `GMAIL_REDIRECT_URI` - OAuth redirect URI (default: localhost)

## Security Considerations

1. Never commit `credentials.json`, `token.json`, or `.env`
2. These are already in `.gitignore`
3. Use environment variables for sensitive data
4. Google OAuth flow is automatic on first run

## Architecture

```
User/Claude/VS Code
        ↓
    MCP Client
        ↓
   MCP Server (FastMCP)
        ↓
   Gmail MCP Server
        ↓
   GmailClient wrapper
        ↓
   Google Gmail API
```

## Common Tasks

### Run in development mode
```bash
uv run mcp dev gmail_mcp_server/server.py
```

### Install dependencies
```bash
uv sync
```

### Format code
```bash
black gmail_mcp_server/
```

### Lint code
```bash
ruff check gmail_mcp_server/
```

## First-Time Setup Instructions for Users

1. Get `credentials.json` from Google Cloud Console
2. Place in project root
3. Install dependencies: `uv sync`
4. Run: `uv run mcp dev gmail_mcp_server/server.py`
5. Test at http://localhost:5173

## Tools Available

1. **list_emails** - List emails with optional search
2. **get_email_details** - Get full email content
3. **send_email** - Send email with HTML support
4. **mark_email_as_read** - Mark email as read
5. **delete_email** - Delete email
6. **search_emails** - Advanced Gmail search
7. **get_labels** - List all Gmail labels

## Future Enhancement Ideas

- [ ] Draft management (create, update, send drafts)
- [ ] Thread handling
- [ ] Attachment handling (download, upload)
- [ ] Archive/unarchive operations
- [ ] Custom label management
- [ ] Email template support
- [ ] Batch operations
- [ ] Email filtering rules

## Debugging

Enable debug logs:
```bash
PYTHONPATH=/path/to/mcp uv run mcp dev gmail_mcp_server/server.py --debug
```

Check MCP Inspector at http://localhost:5173 for:
- Tool execution results
- Request/response debugging
- Error messages and traces

## Support Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Gmail API Python Docs](https://developers.google.com/gmail/api)
- [Google Auth Library](https://github.com/googleapis/google-auth-library-python)
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk)

## Version Information

- Python: 3.10+
- MCP SDK: v1.0.0+
- Google APIs: Latest stable
- Date Updated: May 10, 2026
