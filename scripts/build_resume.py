#!/usr/bin/env python3
"""
Resume Builder Script

This script generates resumes from templates and YAML data.
Supports both Markdown and LaTeX output formats.
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import subprocess

class ResumeBuilder:
    def __init__(self, data_file='data/resume.yml'):
        self.data_file = data_file
        self.base_dir = Path(__file__).parent.parent
        self.data_dir = self.base_dir / 'data'
        self.templates_dir = self.base_dir / 'templates'
        self.output_dir = self.base_dir / 'output'
        
        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)
        
        # Load data
        with open(self.data_dir / 'resume.yml', 'r') as f:
            self.data = yaml.safe_load(f)
    
    def build_markdown(self):
        """Build markdown resume"""
        env = Environment(loader=FileSystemLoader(self.templates_dir / 'markdown'))
        template = env.get_template('resume.md')
        
        # Render template with data
        output = template.render(**self.data)
        
        # Write output
        output_file = self.output_dir / 'resume.md'
        with open(output_file, 'w') as f:
            f.write(output)
        
        print(f"✅ Markdown resume generated: {output_file}")
        return output_file
    
    def build_latex(self):
        """Build LaTeX resume"""
        env = Environment(loader=FileSystemLoader(self.templates_dir / 'latex'))
        template = env.get_template('resume.tex')
        
        # Render template with data
        output = template.render(**self.data)
        
        # Write output
        output_file = self.output_dir / 'resume.tex'
        with open(output_file, 'w') as f:
            f.write(output)
        
        print(f"✅ LaTeX resume generated: {output_file}")
        return output_file
    
    def markdown_to_pdf(self, markdown_file):
        """Convert markdown to PDF using pandoc"""
        try:
            pdf_file = markdown_file.with_suffix('.pdf')
            subprocess.run([
                'pandoc', 
                str(markdown_file), 
                '-o', str(pdf_file),
                '--pdf-engine=xelatex',
                '--variable=geometry:margin=1in'
            ], check=True)
            print(f"✅ PDF generated from markdown: {pdf_file}")
            return pdf_file
        except subprocess.CalledProcessError:
            print("❌ Error: pandoc failed. Make sure pandoc and xelatex are installed.")
            return None
        except FileNotFoundError:
            print("❌ Error: pandoc not found. Please install pandoc.")
            return None
    
    def latex_to_pdf(self, latex_file):
        """Convert LaTeX to PDF using pdflatex"""
        try:
            # Change to output directory for compilation
            original_dir = os.getcwd()
            os.chdir(self.output_dir)
            
            # Run pdflatex
            subprocess.run([
                'pdflatex', 
                '-interaction=nonstopmode',
                latex_file.name
            ], check=True, capture_output=True)
            
            # Clean up auxiliary files
            for ext in ['.aux', '.log', '.out']:
                aux_file = latex_file.with_suffix(ext)
                if aux_file.exists():
                    aux_file.unlink()
            
            os.chdir(original_dir)
            
            pdf_file = latex_file.with_suffix('.pdf')
            print(f"✅ PDF generated from LaTeX: {pdf_file}")
            return pdf_file
        except subprocess.CalledProcessError:
            print("❌ Error: pdflatex failed. Make sure texlive is installed.")
            return None
        except FileNotFoundError:
            print("❌ Error: pdflatex not found. Please install texlive.")
            return None
        finally:
            os.chdir(original_dir)
    
    def build_all(self, pdf=False):
        """Build all resume formats"""
        print("🚀 Building resume...")
        
        # Build markdown
        md_file = self.build_markdown()
        
        # Build LaTeX
        tex_file = self.build_latex()
        
        if pdf:
            print("\n📄 Generating PDFs...")
            self.markdown_to_pdf(md_file)
            self.latex_to_pdf(tex_file)
        
        print("\n✨ Resume build complete!")

def main():
    parser = argparse.ArgumentParser(description='Build resume from templates')
    parser.add_argument('--format', choices=['markdown', 'latex', 'all'], 
                       default='all', help='Output format')
    parser.add_argument('--pdf', action='store_true', 
                       help='Generate PDF files')
    parser.add_argument('--data', default='data/resume.yml',
                       help='Path to resume data file')
    
    args = parser.parse_args()
    
    builder = ResumeBuilder(args.data)
    
    if args.format == 'markdown':
        md_file = builder.build_markdown()
        if args.pdf:
            builder.markdown_to_pdf(md_file)
    elif args.format == 'latex':
        tex_file = builder.build_latex()
        if args.pdf:
            builder.latex_to_pdf(tex_file)
    else:
        builder.build_all(args.pdf)

if __name__ == '__main__':
    main()