# {{personal.name}}

**{{personal.title}}**

📧 {{personal.email}} | 📱 {{personal.phone}} | 📍 {{personal.location}}  
🌐 [{{personal.website}}]({{personal.website}}) | 💼 [LinkedIn]({{personal.linkedin}}) | 👨‍💻 [GitHub]({{personal.github}})

---

## Summary

{{summary}}

---

## Experience

{{#each experience}}
### {{position}} | {{company}}
*{{location}} | {{start_date}} - {{end_date}}*

{{#each achievements}}
- {{this}}
{{/each}}

{{/each}}

---

## Education

{{#each education}}
### {{degree}}
**{{institution}}** | {{location}} | {{graduation_date}}
{{#if gpa}}
*GPA: {{gpa}}*
{{/if}}

{{#if relevant_coursework}}
**Relevant Coursework:** {{#each relevant_coursework}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}
{{/if}}

{{/each}}

---

## Technical Skills

**Programming Languages:** {{#each skills.programming_languages}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}

**Frameworks & Libraries:** {{#each skills.frameworks_libraries}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}

**Tools & Technologies:** {{#each skills.tools_technologies}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}

---

## Projects

{{#each projects}}
### {{name}}
{{description}}

**Technologies:** {{#each technologies}}{{this}}{{#unless @last}}, {{/unless}}{{/each}}  
**GitHub:** [{{github}}]({{github}})

{{#each achievements}}
- {{this}}
{{/each}}

{{/each}}

---

## Certifications

{{#each certifications}}
- **{{name}}** - {{issuer}} ({{date}})
{{/each}}