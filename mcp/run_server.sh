#!/bin/bash
# Gmail MCP Server Runner

# Navigate to project directory
cd /Users/krishna/Desktop/Workspace/BITS_PILANI/Code_workspace/mcp

# Activate virtual environment
source .venv/bin/activate

# Run the server
echo "🚀 Starting Gmail MCP Server..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Server is running and waiting for connections..."
echo "✅ Ready to accept MCP client connections"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

python -m gmail_mcp_server.server
