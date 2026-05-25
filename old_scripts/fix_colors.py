import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix ikigai colors
content = content.replace('bg-blue-500', 'bg-zinc-300')
content = content.replace('bg-purple-500', 'bg-white')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
