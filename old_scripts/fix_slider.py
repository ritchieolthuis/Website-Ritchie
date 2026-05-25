import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Show 4 cards instead of 3
content = content.replace('lg:w-1/3 flex-shrink-0', 'lg:w-1/4 flex-shrink-0')

# 2. Swap roles
role_7_en = '"Director at Axelio | Agrio Software | Microsoft-partner | Driver of digital growth and innovation"'
role_8_en = '"Business Development Manager at Vitens"'

role_7_nl = '"Directeur bij Axelio | Agrio Software | Microsoft-partner | Aanjager van digitale groei en innovatie"'
role_8_nl = '"Business Development Manager bij Vitens"'

# Find exactly where these are to avoid multiple matches, or just string replace securely
content = content.replace(f'rec_7_role: {role_7_en},', f'rec_7_role: {role_8_en},')
content = content.replace(f'rec_8_role: {role_8_en},', f'rec_8_role: {role_7_en},')

content = content.replace(f'rec_7_role: {role_7_nl},', f'rec_7_role: {role_8_nl},')
content = content.replace(f'rec_8_role: {role_8_nl},', f'rec_8_role: {role_7_nl},')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

