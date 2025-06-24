# Resume Template System

A flexible, data-driven resume template system that generates professional resumes in multiple formats from a single YAML data source.

## 🚀 Features

- **Single Source of Truth**: Maintain your resume data in one YAML file
- **Multiple Formats**: Generate Markdown and LaTeX versions
- **PDF Generation**: Convert to PDF using pandoc or pdflatex
- **Professional Templates**: Clean, modern designs optimized for ATS systems
- **Version Control**: Track changes to your resume over time
- **Easy Customization**: Modify templates without touching your data

## 📁 Project Structure

```
resume-template/
├── data/
│   └── resume.yml              # Your resume data
├── templates/
│   ├── markdown/
│   │   └── resume.md          # Markdown template
│   └── latex/
│       └── resume.tex         # LaTeX template
├── scripts/
│   ├── build_resume.py        # Main build script
│   └── setup.sh              # Setup script
├── output/                    # Generated files
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🛠️ Setup

### Quick Start

1. **Clone and setup:**
   ```bash
   ./scripts/setup.sh
   ```

2. **Edit your data:**
   ```bash
   nano data/resume.yml
   ```

3. **Build your resume:**
   ```bash
   python3 scripts/build_resume.py
   ```

### Manual Setup

1. **Install Python dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Install optional dependencies for PDF generation:**
   
   **For Markdown → PDF (pandoc):**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install pandoc texlive-xetex
   
   # macOS
   brew install pandoc basictex
   
   # Arch Linux
   sudo pacman -S pandoc texlive-core
   ```
   
   **For LaTeX → PDF (texlive):**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-full
   
   # macOS
   brew install --cask mactex
   
   # Arch Linux
   sudo pacman -S texlive-most
   ```

## 📝 Usage

### Basic Usage

Generate all formats:
```bash
python3 scripts/build_resume.py
```

Generate specific format:
```bash
python3 scripts/build_resume.py --format markdown
python3 scripts/build_resume.py --format latex
```

Generate with PDFs:
```bash
python3 scripts/build_resume.py --pdf
```

### Command Line Options

```bash
python3 scripts/build_resume.py --help
```

Options:
- `--format {markdown,latex,all}`: Choose output format (default: all)
- `--pdf`: Generate PDF files
- `--data PATH`: Specify custom data file (default: data/resume.yml)

## 📊 Customizing Your Resume

### 1. Edit Resume Data

All your resume information is stored in `data/resume.yml`. Simply edit this file with your information:

```yaml
personal:
  name: "Your Name"
  title: "Your Job Title"
  email: "your.email@example.com"
  # ... more fields
```

### 2. Customize Templates

Templates are located in `templates/`:
- `templates/markdown/resume.md` - Markdown template
- `templates/latex/resume.tex` - LaTeX template

Templates use Jinja2 syntax for variable substitution and logic.

### 3. Add New Sections

To add new sections:
1. Add the data to `data/resume.yml`
2. Update the relevant templates to display the new section
3. Rebuild your resume

## 🎨 Template Customization

### Markdown Template

The markdown template creates a clean, readable format perfect for:
- GitHub README profiles
- Online portfolios
- Quick sharing and viewing

### LaTeX Template

The LaTeX template uses the `moderncv` class for:
- Professional PDF output
- ATS-friendly formatting
- Customizable styling and colors

To change LaTeX styling, modify these lines in `templates/latex/resume.tex`:
```latex
\moderncvstyle{classic}  % Options: classic, casual, banking, oldstyle, fancy
\moderncvcolor{blue}     % Options: blue, orange, green, red, purple, grey, black
```

## 📄 Output Files

After running the build script, check the `output/` directory:

- `resume.md` - Markdown version
- `resume.tex` - LaTeX source
- `resume.pdf` - PDF version (if --pdf flag used)

## 🔧 Advanced Usage

### Multiple Resume Versions

Create different resume versions for different roles:

```bash
# Create specialized data files
cp data/resume.yml data/resume-frontend.yml
cp data/resume.yml data/resume-backend.yml

# Build specific versions
python3 scripts/build_resume.py --data data/resume-frontend.yml --pdf
python3 scripts/build_resume.py --data data/resume-backend.yml --pdf
```

### Custom Templates

Create new templates in the `templates/` directory and modify the build script to use them.

## 🐛 Troubleshooting

### Common Issues

**PDF generation fails:**
- Ensure pandoc and LaTeX are installed
- Check that all fonts are available
- Verify file permissions

**Template rendering errors:**
- Check YAML syntax in `data/resume.yml`
- Ensure all required fields are present
- Verify Jinja2 template syntax

**Import errors:**
- Run `pip3 install -r requirements.txt`
- Check Python version (3.6+ required)

### Getting Help

If you encounter issues:
1. Check the error message carefully
2. Verify all dependencies are installed
3. Ensure your YAML data is valid
4. Check file permissions

## 🤝 Contributing

Feel free to:
- Add new template styles
- Improve the build system
- Add support for new output formats
- Submit bug fixes and improvements

## 📄 License

This project is open source. Feel free to use and modify as needed.

## 🎯 Next Steps

1. **Customize your data** in `data/resume.yml`
2. **Build your resume** with `python3 scripts/build_resume.py --pdf`
3. **Share your professional resume** with confidence!

---

**Happy job hunting! 🎉**