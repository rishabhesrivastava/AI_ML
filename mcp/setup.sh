#!/bin/bash
# Initial Setup Script for Gmail MCP Server

set -e

echo "======================================"
echo "Gmail MCP Server - Initial Setup"
echo "======================================"
echo ""

# Check if credentials.json exists
if [ ! -f "credentials.json" ]; then
    echo "❌ ERROR: credentials.json not found!"
    echo ""
    echo "You need to:"
    echo "1. Go to https://console.cloud.google.com"
    echo "2. Create a new project"
    echo "3. Enable Gmail API"
    echo "4. Create OAuth 2.0 credentials (Desktop app)"
    echo "5. Download the JSON file"
    echo "6. Save it as 'credentials.json' in this directory"
    echo ""
    exit 1
fi

echo "✅ credentials.json found"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.10+"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check if uv is available, if not suggest pip
if ! command -v uv &> /dev/null; then
    echo "⚠️  uv not found. Using pip instead."
    echo "   (Recommended: pip install uv)"
    echo ""
    echo "Installing dependencies with pip..."
    pip install -r requirements.txt
else
    echo "✅ uv found"
    echo ""
    echo "Installing dependencies..."
    uv sync
fi

echo ""
echo "======================================"
echo "✅ Setup Complete!"
echo "======================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Test the server (recommended):"
echo "   uv run mcp dev gmail_mcp_server/server.py"
echo ""
echo "2. Or run directly:"
echo "   uv run gmail_mcp_server/server.py"
echo ""
echo "3. Install to Claude Desktop:"
echo "   uv run mcp install gmail_mcp_server/server.py --name \"Gmail\""
echo ""
echo "For more info, see: QUICKSTART.md or SETUP_SUMMARY.md"
echo ""
