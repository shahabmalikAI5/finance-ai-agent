#!/bin/bash

echo "🚀 Installing GitHub MCP Server..."

# Install GitHub MCP server globally via npm
npm install -g @modelcontextprotocol/server-github

echo "✅ GitHub MCP Server installed successfully!"
echo ""
echo "📋 Configuration Complete!"
echo "   - .mcp.json file created in Finance_agent directory"
echo ""
echo "🔑 IMPORTANT: Set your GitHub Token"
echo "   Run this command in your terminal:"
echo "   export GITHUB_TOKEN='your_github_personal_access_token'"
echo ""
echo "   To get GitHub Token:"
echo "   1. Go to https://github.com/settings/tokens"
echo "   2. Click 'Generate new token (classic)'"
echo "   3. Select 'repo' permissions"
echo "   4. Copy the token and paste it above"
echo ""
echo "📌 After setting token, restart Claude Code to activate GitHub MCP"
