import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to insert a closing </div> right before <!-- Semester Pages Container -->
content = content.replace(
    '               </div>\n            <!-- Semester Pages Container -->',
    '               </div>\n            </div>\n            <!-- Semester Pages Container -->'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

