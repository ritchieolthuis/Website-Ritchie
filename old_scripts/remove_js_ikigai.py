import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the translation keys for ikigai_reflection
content = re.sub(r"ikigai_reflection:\s*'.*?',\n", "", content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
