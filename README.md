# LaTeX Resume Template

A professional, ATS-friendly LaTeX resume template with modern styling and comprehensive sections.

## Features

- **ATS-Friendly**: Uses machine-readable fonts and formatting
- **Modern Design**: Clean, professional layout with Font Awesome icons
- **Comprehensive Sections**: Education, Experience, Projects, Skills, Certifications, Leadership
- **Easy Customization**: Well-commented LaTeX code with custom commands
- **Professional Typography**: Uses Fira Sans font for modern appearance

## Prerequisites

To compile this resume, you'll need:

- A LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- The following LaTeX packages (usually included in full distributions):
  - `fontawesome5`
  - `FiraSans`
  - `titlesec`
  - `enumitem`
  - `hyperref`
  - `tabularx`

## Quick Start

1. **Install LaTeX** (if not already installed):
   - Ubuntu/Debian: `sudo apt-get install texlive-full`
   - macOS: Install MacTeX from https://www.tug.org/mactex/
   - Windows: Install MiKTeX from https://miktex.org/

2. **Compile the resume**:
   ```bash
   make
   ```
   
   Or manually:
   ```bash
   pdflatex resume.tex
   pdflatex resume.tex  # Run twice for proper formatting
   ```

3. **View the result**:
   ```bash
   make view
   ```

## Customization Guide

### 1. Personal Information (Header)
Replace the placeholder information in the header section:

```latex
{\Huge \scshape Your Name} \\ \vspace{1pt}
City, State, ZIP Code \\ \vspace{1pt}
\small \raisebox{-0.1\height}\faPhone\ 123-456-7890 ~ 
\href{mailto:your.email@example.com}{\raisebox{-0.2\height}\faEnvelope\  your.email@example.com} ~ 
\href{https://linkedin.com/in/yourprofile}{\raisebox{-0.2\height}\faLinkedin\ linkedin.com/in/yourprofile} ~
\href{https://github.com/yourusername}{\raisebox{-0.2\height}\faGithub\ github.com/yourusername} ~
\href{https://yourwebsite.com}{\raisebox{-0.2\height}\faGlobe\ yourwebsite.com}
```

### 2. Education
Update the education section with your academic background:

```latex
\resumeSubheading
  {University Name}{Month Year -- Month Year}
  {Degree in Major, Minor (if applicable)}{City, State}
  \resumeItemListStart
    \resumeItem{GPA: X.XX/4.0 (if impressive)}
    \resumeItem{Relevant Coursework: Course 1, Course 2, Course 3, Course 4}
    \resumeItem{Honors/Awards: Dean's List, Scholarship Name, etc.}
  \resumeItemListEnd
```

### 3. Experience
Add your work experience using the `\resumeSubheading` command:

```latex
\resumeSubheading
  {Job Title}{Month Year -- Present/Month Year}
  {Company Name}{City, State}
  \resumeItemListStart
    \resumeItem{Achievement with quantifiable results (e.g., increased efficiency by 25\%)}
    \resumeItem{Another achievement demonstrating impact and technical skills}
    \resumeItem{Technologies used: Technology 1, Technology 2, Technology 3}
  \resumeItemListEnd
```

### 4. Projects
Showcase your projects with technologies used:

```latex
\resumeProjectHeading
    {\textbf{Project Name} $|$ \emph{Technology 1, Technology 2, Technology 3}}{Month Year}
    \resumeItemListStart
      \resumeItem{Brief description of the project and its purpose}
      \resumeItem{Key technical challenges solved and methodologies used}
      \resumeItem{Results achieved or impact made}
    \resumeItemListEnd
```

### 5. Technical Skills
Update the skills section with your technologies:

```latex
\textbf{Programming Languages}{: Python, Java, JavaScript, C++, SQL, HTML/CSS} \\
\textbf{Frameworks \& Libraries}{: React, Node.js, Django, Flask, TensorFlow, PyTorch} \\
\textbf{Tools \& Technologies}{: Git, Docker, AWS, MongoDB, PostgreSQL, Linux, Kubernetes} \\
```

## Tips for Customization

1. **Keep it concise**: Aim for 1-2 pages maximum
2. **Use action verbs**: Start bullet points with strong action verbs
3. **Quantify achievements**: Include numbers and percentages when possible
4. **Tailor content**: Customize for each job application
5. **Proofread carefully**: Check for typos and grammatical errors

## Adding/Removing Sections

- To add a new section, use the `\section{Section Name}` command
- To remove a section, simply delete or comment out the entire section block
- Available sections in this template: Education, Experience, Projects, Technical Skills, Certifications, Leadership & Activities

## Makefile Commands

- `make` or `make all`: Compile the resume
- `make clean`: Remove auxiliary files
- `make clean-all`: Remove all generated files including PDF
- `make view`: Open the compiled PDF
- `make help`: Show available commands

## Troubleshooting

1. **Missing packages**: If compilation fails due to missing packages, install them via your LaTeX package manager
2. **Font issues**: If Font Awesome icons don't display, ensure `fontawesome5` package is installed
3. **Unicode issues**: Make sure your LaTeX editor is set to UTF-8 encoding

## Converting from Your PDF

To transfer information from your existing PDF resume:

1. Open your PDF resume
2. Copy the text content section by section
3. Replace the placeholder text in the corresponding LaTeX sections
4. Maintain the same structure and formatting style
5. Adjust bullet points to match the template's style
6. Update contact information and links

This template provides a solid foundation for a professional resume that you can easily customize with your specific information and experiences.