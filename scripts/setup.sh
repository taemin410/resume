#!/bin/bash

# Resume Template Setup Script
# This script installs the necessary dependencies for the resume builder

echo "🚀 Setting up resume template environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Check for optional dependencies
echo "🔍 Checking for optional dependencies..."

# Check for pandoc (for markdown to PDF conversion)
if command -v pandoc &> /dev/null; then
    echo "✅ pandoc found"
else
    echo "⚠️  pandoc not found. Install pandoc to convert markdown to PDF:"
    echo "   Ubuntu/Debian: sudo apt-get install pandoc"
    echo "   macOS: brew install pandoc"
    echo "   Arch: sudo pacman -S pandoc"
fi

# Check for LaTeX (for LaTeX to PDF conversion)
if command -v pdflatex &> /dev/null; then
    echo "✅ pdflatex found"
else
    echo "⚠️  pdflatex not found. Install texlive to convert LaTeX to PDF:"
    echo "   Ubuntu/Debian: sudo apt-get install texlive-full"
    echo "   macOS: brew install --cask mactex"
    echo "   Arch: sudo pacman -S texlive-most"
fi

# Make build script executable
chmod +x scripts/build_resume.py

echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit data/resume.yml with your information"
echo "2. Run: python3 scripts/build_resume.py"
echo "3. Check the output/ directory for your generated resume"