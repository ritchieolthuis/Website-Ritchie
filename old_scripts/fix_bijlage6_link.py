import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

url = "https://docs.google.com/spreadsheets/d/1XqhvW2usQ9FYD7Tye1TzObGUiBtvB9cJrIJR7dbGhWg/edit?usp=drive_link"
a_tag = f'<a href="{url}" target="_blank" class="text-accent hover:underline font-bold">Bijlage VI</a>'
a_tag_mx1 = f'<a href="{url}" target="_blank" class="text-accent hover:underline font-bold inline-block mx-1">Bijlage VI</a>'

# 1. Line 1628 / Story text
content = content.replace(
    'De CE Skills Guide (Windesheim, 2026; zie <span class="text-accent font-bold">Bijlage VI</span>)',
    f'De CE Skills Guide (Windesheim, 2026; zie {a_tag_mx1})'
)

# 2. Line 1682 / Skills Visualisation text
content = content.replace(
    'intervisie met medestudenten gedurende de opleiding (Windesheim, 2026; zie <span class="text-accent font-bold">Bijlage VI</span>)',
    f'intervisie met medestudenten gedurende de opleiding (Windesheim, 2026; zie {a_tag})'
)

# 3. Line 1703 / Chart footnote
content = content.replace(
    '* Windesheim. (2026). Ingevulde CE Skillsguide door medestudenten (Bijlage VI).',
    f'* Windesheim. (2026). Ingevulde CE Skillsguide door medestudenten (Bijlage VI). Raadpleeg via: <a href="{url}" target="_blank" class="text-accent hover:underline">Google Sheets</a>'
)

# 4. Line 2172 / Bronnenlijst
content = content.replace(
    'Windesheim. (2026). <span class="italic">Ingevulde CE Skillsguide door medestudenten</span> [Bijlage VI]. Ongepubliceerd manuscript, Windesheim.',
    f'Windesheim. (2026). <span class="italic">Ingevulde CE Skillsguide door medestudenten</span> [Bijlage VI]. Ongepubliceerd manuscript, Windesheim.<br><a href="{url}" target="_blank" class="text-accent hover:underline break-words">{url}</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

