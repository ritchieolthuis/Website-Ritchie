import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Expert Enquête United Kingdom
content = content.replace(
    'Olthuis, R. (2026). <span class="italic">Expert Enquête United Kingdom</span> [Online Formulier].',
    'Olthuis, R. (2026). <span class="italic">Expert Enquête United Kingdom</span> [Online Formulier].<br><a href="#" onclick="window.showSemesterPage(\'afstuderen\'); document.getElementById(\'portfolio-semester-evidence\').scrollIntoView({behavior: \'smooth\'}); return false;" class="text-accent hover:underline break-words">Bekijk bewijsstuk in portfolio (Afstuderen)</a>'
)

# Diepte-interviews & Marktvalidatie Agrio
content = content.replace(
    'Olthuis, R. (2026). <span class="italic">Diepte-interviews & Marktvalidatie Agrio</span> [Online Formulier].',
    'Olthuis, R. (2026). <span class="italic">Diepte-interviews & Marktvalidatie Agrio</span> [Online Formulier].<br><a href="#" onclick="window.showSemesterPage(\'afstuderen\'); document.getElementById(\'portfolio-semester-evidence\').scrollIntoView({behavior: \'smooth\'}); return false;" class="text-accent hover:underline break-words">Bekijk bewijsstuk in portfolio (Afstuderen)</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

