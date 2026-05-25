import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'id="portfolio-grid".*?<!-- Jaar 3 Card -->', content, re.DOTALL)
if match:
    print(match.group(0))

