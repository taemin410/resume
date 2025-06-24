# Quick Start Guide

## 🚀 Get Your Resume Ready in 3 Steps

### Step 1: Customize Your Data
Edit `data/resume.yml` with your information:
```bash
nano data/resume.yml
```

### Step 2: Build Your Resume
Run the simple builder (works everywhere):
```bash
python3 scripts/simple_build.py
```

### Step 3: Get Your Files
Check the `output/` directory for:
- `sample_resume.md` - Example resume
- `simple_resume.md` - Your customized resume

## 📄 Convert to PDF

If you have pandoc installed:
```bash
pandoc output/sample_resume.md -o output/sample_resume.pdf
```

## 🎨 Available Templates

1. **Simple Template** (`templates/markdown/simple_resume.md`)
   - Direct editing, no dependencies
   - Just replace placeholder text

2. **Advanced Template** (`templates/markdown/resume.md`)
   - Uses YAML data + Jinja2 templates
   - Requires `python3 scripts/build_resume.py` with dependencies

3. **LaTeX Template** (`templates/latex/resume.tex`)
   - Professional PDF output
   - Requires LaTeX installation

## 💡 Tips

- Start with the sample resume as a template
- Copy `sample_resume.md` and edit directly for quickest results
- Use the YAML data approach for managing multiple resume versions
- Version control your resume changes with git

## 🛠️ Full Setup (Optional)

For advanced features with PDF generation:
```bash
./scripts/setup.sh
```

This will set up virtual environments and check for PDF conversion tools.

---

**Ready to impress! 🎉**