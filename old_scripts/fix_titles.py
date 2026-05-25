import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Jaar 2 title
content = content.replace(
    '<p class="text-white font-bold text-lg md:text-xl mb-3">Business Development | Unica</p>',
    '<p class="text-white font-bold text-lg md:text-xl mb-3">Business Development | Unica Building Services</p>'
)

# Update Jaar 3 title
content = content.replace(
    '<p class="text-white font-bold text-lg md:text-xl mb-3">Minor Financiële & Pre-master UT</p>',
    '<p class="text-white font-bold text-lg md:text-xl mb-3">Minor Financiële Besluitvorming & Pre-master Business Administration | Universiteit Twente</p>'
)

# Update Jaar 4 title
old_jaar4_p = '<p class="text-white font-bold text-lg md:text-xl mb-3">Young Professional Commerce</p>'
new_jaar4_p = '''<p class="text-white font-bold text-lg md:text-xl mb-3">Young Professional Commerce Programme</p>
                            <p class="text-zinc-400 text-sm font-medium mb-1">Perron038 | Factory NEXT Positionering</p>
                            <p class="text-zinc-400 text-sm font-medium mb-3">Vitens | Water as a Service Positionering</p>'''
content = content.replace(old_jaar4_p, new_jaar4_p)

# Update Afstuderen title
old_afstuderen_h = '<h3 class="text-3xl md:text-4xl font-display text-white group-hover:text-accent font-bold transition-colors">Afstuderen</h3>'
new_afstuderen_h = '<h3 class="text-3xl md:text-4xl font-display text-white group-hover:text-accent font-bold transition-colors">Jaar 4 – Afstuderen</h3>'
content = content.replace(old_afstuderen_h, new_afstuderen_h)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

