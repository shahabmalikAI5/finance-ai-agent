#!/bin/bash

# Finance Agent Web Interface - Startup Script
# This script launches the Streamlit web interface

echo "🚀 Starting Finance Agent Web Interface..."
echo ""

# Check if streamlit is installed
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing Streamlit..."
    pip install streamlit
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "   Please create .env with your OpenRouter API key."
    echo ""
    echo "   Example:"
    echo "   OPENAI_API_KEY=sk-or-v1-your-key-here"
    echo "   OPENAI_BASE_URL=https://openrouter.ai/api/v1"
    echo ""
    read -p "Press Enter to continue anyway..."
fi

# Start the web interface
echo "✅ Launching web interface..."
echo "📱 Open your browser to: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
