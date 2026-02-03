#!/bin/bash

# Quick start script for GitHub Codespaces and Dev Containers
# This script helps new users get started quickly

echo "🚀 Python Streamlit Starter - Quick Start"
echo "=========================================="
echo ""

# Check if dependencies are installed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install --user -r requirements.txt
    echo "✅ Dependencies installed!"
    echo ""
fi

echo "🎯 Starting Streamlit application..."
echo ""
echo "The app will be available at:"
echo "  - Local: http://localhost:8501"
echo "  - Codespaces: Click the notification to open"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run Streamlit
streamlit run app.py
