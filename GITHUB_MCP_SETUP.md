# GitHub MCP Server Setup Guide

## ✅ Installation Status
- GitHub MCP Server: Installed via npm
- Configuration file: `.mcp.json` created in Finance_agent directory

## 🔑 Step 1: Create GitHub Personal Access Token

1. Browser mein yahan jayein: **https://github.com/settings/tokens**
2. **"Generate new token (classic)"** par click karein
3. Token ka naam dein (e.g., "Claude Code MCP")
4. **Permissions** mein yeh select karein:
   - ✅ **repo** (Full control of private repositories)
   - ✅ **repo:status** (Access commit status)
   - ✅ **repo_deployment** (Access deployment status)
   - ✅ **public_repo** (Access public repositories)
   - ✅ **read:org** (Read org and team membership)
5. **"Generate token"** par click karein
6. ⚠️ **Token ko copy karein** - Yeh sirf ek baar dikhai dega!

## 🖥️ Step 2: Set Environment Variable

Terminal mein yeh command run karein (token ko paste karke):

```bash
export GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

**Permanent ke liye** (`~/.bashrc` mein add karein):
```bash
echo 'export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc
```

## 🔄 Step 3: Restart Claude Code

Claude Code ko close karke dobara start karein taake GitHub MCP load ho jaye.

## 🧪 Step 4: Verify Installation

Claude Code mein check karein ki GitHub MCP available hai ya nahi.

## 📝 Features Available

GitHub MCP server ke through yeh features available hain:
- 📂 Repository browsing
- 📄 File reading
- 📝 File editing
- 🌿 Branch operations
- 🔄 Commit operations
- ⚠️ Issues aur Pull Requests

## 🔍 File Locations

- **MCP Config**: `/mnt/d/Data all/claude-code-router-setup/Finance_agent/.mcp.json`
- **Installation Script**: `/mnt/d/Data all/claude-code-router-setup/Finance_agent/install_github_mcp.sh`

---
**Created by:** SHAHAB MALIK
