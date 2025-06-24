#!/bin/bash

# Resume Template Setup Script
# This script installs the necessary dependencies for the resume builder

echo "🚀 Setting up resume template environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✅ Python 3 found"

# Try to create virtual environment
echo "📦 Setting up Python environment..."

if python3 -m venv venv 2>/dev/null; then
    echo "✅ Virtual environment created"
    source venv/bin/activate
    pip install -r requirements.txt
    echo "✅ Dependencies installed in virtual environment"
    echo ""
    echo "To use the full-featured builder:"
    echo "  source venv/bin/activate"
    echo "  python scripts/build_resume.py"
else
    echo "⚠️  Virtual environment creation failed"
    echo "💡 Using system Python with simple builder"
    echo ""
    echo "To use the simple builder (no external dependencies):"
    echo "  python3 scripts/simple_build.py"
fi

# Check for optional dependencies
echo ""
echo "🔍 Checking for optional dependencies..."

# Check for pandoc (for markdown to PDF conversion)
if command -v pandoc &> /dev/null; then
    echo "✅ pandoc found"
else
    echo "⚠️  pandoc not found. Install pandoc to convert markdown to PDF:"
    echo "   Ubuntu/Debian: sudo apt-get install pandoc texlive-xetex"
    echo "   macOS: brew install pandoc basictex"
    echo "   Arch: sudo pacman -S pandoc texlive-core"
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

# Make build scripts executable
chmod +x scripts/*.py

echo ""
echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit data/resume.yml with your information"
echo "2. Run: python3 scripts/simple_build.py (simple version)"
if [ -d "venv" ]; then
    echo "   OR: source venv/bin/activate && python scripts/build_resume.py (full version)"
fi
echo "3. Check the output/ directory for your generated resume"