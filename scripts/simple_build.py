#!/usr/bin/env python3
"""
Simple Resume Builder

This script generates resumes using basic string substitution.
No external dependencies required.
"""

import os
import re
import json
from pathlib import Path

class SimpleResumeBuilder:
    def __init__(self, data_file='data/resume.yml'):
        self.base_dir = Path(__file__).parent.parent
        self.data_dir = self.base_dir / 'data'
        self.templates_dir = self.base_dir / 'templates'
        self.output_dir = self.base_dir / 'output'
        
        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)
        
        # Load data from YAML file
        self.data = self.load_yaml_data()
    
    def load_yaml_data(self):
        """Simple YAML parser for basic key-value pairs"""
        data = {}
        current_section = None
        current_list = None
        
        try:
            with open(self.data_dir / 'resume.yml', 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("❌ Error: resume.yml not found. Please create it first.")
            return {}
        
        for line in lines:
            line = line.rstrip()
            
            # Skip comments and empty lines
            if line.startswith('#') or not line.strip():
                continue
            
            # Top-level sections
            if line and not line.startswith(' '):
                section_name = line.rstrip(':')
                data[section_name] = {}
                current_section = section_name
                current_list = None
            
            # Subsections or values
            elif line.startswith('  ') and not line.startswith('    '):
                if current_section:
                    if line.strip().startswith('- '):
                        # List item
                        if current_list is None:
                            current_list = []
                            # Find the parent key
                            parent_key = list(data[current_section].keys())[-1] if data[current_section] else 'items'
                            data[current_section][parent_key] = current_list
                        current_list.append(line.strip()[2:].strip('"'))
                    else:
                        # Key-value pair
                        if ':' in line:
                            key, value = line.strip().split(':', 1)
                            data[current_section][key.strip()] = value.strip().strip('"')
                            current_list = None
        
        return data
    
    def simple_template_render(self, template_content, data):
        """Simple template rendering using string replacement"""
        content = template_content
        
        # Replace simple variables like {{personal.name}}
        def replace_var(match):
            var_path = match.group(1)
            parts = var_path.split('.')
            
            try:
                value = data
                for part in parts:
                    if isinstance(value, dict):
                        value = value.get(part, '')
                    else:
                        return f"{{{{ {var_path} }}}}"
                return str(value) if value else ''
            except:
                return f"{{{{ {var_path} }}}}"
        
        # Replace variables
        content = re.sub(r'\{\{\s*([^}]+)\s*\}\}', replace_var, content)
        
        return content
    
    def build_simple_markdown(self):
        """Build markdown resume using simple template"""
        try:
            with open(self.templates_dir / 'markdown' / 'simple_resume.md', 'r') as f:
                template = f.read()
        except FileNotFoundError:
            print("❌ Error: simple_resume.md template not found.")
            return None
        
        # Manual replacement for simple template
        content = template
        
        # Replace basic info if available
        if 'personal' in self.data:
            personal = self.data['personal']
            content = content.replace('Your Name', personal.get('name', 'Your Name'))
            content = content.replace('Your Job Title', personal.get('title', 'Your Job Title'))
            content = content.replace('your.email@example.com', personal.get('email', 'your.email@example.com'))
            # Add more replacements as needed
        
        # Write output
        output_file = self.output_dir / 'simple_resume.md'
        with open(output_file, 'w') as f:
            f.write(content)
        
        print(f"✅ Simple markdown resume generated: {output_file}")
        return output_file
    
    def create_sample_resume(self):
        """Create a sample resume with placeholder data"""
        output_file = self.output_dir / 'sample_resume.md'
        
        sample_content = """# John Doe

**Senior Software Engineer**

📧 john.doe@email.com | 📱 +1 (555) 123-4567 | 📍 San Francisco, CA  
🌐 [johndoe.dev](https://johndoe.dev) | 💼 [LinkedIn](https://linkedin.com/in/johndoe) | 👨‍💻 [GitHub](https://github.com/johndoe)

---

## Summary

Experienced software engineer with 5+ years of experience in full-stack development, cloud technologies, and team leadership. Passionate about creating scalable solutions and mentoring junior developers.

---

## Experience

### Senior Software Engineer | Tech Innovations Inc.
*San Francisco, CA | Jan 2021 - Present*

- Led development of microservices architecture serving 1M+ users
- Reduced system latency by 40% through optimization initiatives
- Mentored 3 junior developers and conducted code reviews
- Implemented CI/CD pipelines reducing deployment time by 60%

### Software Engineer | Digital Solutions Ltd.
*San Francisco, CA | Jun 2019 - Jan 2021*

- Developed RESTful APIs using Node.js and Express
- Built responsive web applications with React and TypeScript
- Collaborated with cross-functional teams in Agile environment
- Maintained 95%+ code coverage through comprehensive testing

---

## Education

### Bachelor of Science in Computer Science
**Stanford University** | Stanford, CA | May 2019  
*GPA: 3.8/4.0*

**Relevant Coursework:** Data Structures and Algorithms, Software Engineering, Database Systems, Computer Networks

---

## Technical Skills

**Programming Languages:** Python, JavaScript/TypeScript, Java, Go, SQL

**Frameworks & Libraries:** React, Node.js, Express, Django, Flask, Spring Boot

**Tools & Technologies:** Docker, Kubernetes, AWS, Git, Jenkins, PostgreSQL, MongoDB, Redis

---

## Projects

### E-commerce Platform
Full-stack web application with payment processing

**Technologies:** React, Node.js, PostgreSQL, Stripe API  
**GitHub:** [github.com/johndoe/ecommerce-platform](https://github.com/johndoe/ecommerce-platform)

- Implemented secure payment processing
- Built admin dashboard for inventory management
- Achieved 99.9% uptime with proper error handling

### Data Analytics Dashboard
Real-time dashboard for business metrics visualization

**Technologies:** Python, Django, Chart.js, PostgreSQL  
**GitHub:** [github.com/johndoe/analytics-dashboard](https://github.com/johndoe/analytics-dashboard)

- Processed and visualized 100K+ data points daily
- Created interactive charts and reports
- Implemented role-based access control

---

## Certifications

- **AWS Certified Solutions Architect** - Amazon Web Services (Mar 2022)
- **Certified Kubernetes Application Developer** - Cloud Native Computing Foundation (Nov 2021)
"""
        
        with open(output_file, 'w') as f:
            f.write(sample_content)
        
        print(f"✅ Sample resume created: {output_file}")
        return output_file

def main():
    print("🚀 Simple Resume Builder")
    
    builder = SimpleResumeBuilder()
    
    # Always create a sample resume
    builder.create_sample_resume()
    
    # Try to build from data if available
    if builder.data:
        builder.build_simple_markdown()
    else:
        print("\n💡 Tip: Edit data/resume.yml to customize your resume")
    
    print("\n✨ Build complete! Check the output/ directory.")

if __name__ == '__main__':
    main()