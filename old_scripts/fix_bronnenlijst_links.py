import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace each specific string in the Bronnenlijst with the string + the URL.

# 1. Waardecreatie Plan
content = content.replace(
    'Olthuis, R. (2023). <span class="italic">Waardecreatie Plan</span> [PDF]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. (2023). <span class="italic">Waardecreatie Plan</span> [PDF]. Ongepubliceerd, Windesheim.<br><a href="https://drive.google.com/file/d/1qKTB8Ahpum2alkXtpLowEHSODjh9OM9P/view" target="_blank" class="text-accent hover:underline break-words">https://drive.google.com/file/d/1qKTB8Ahpum2alkXtpLowEHSODjh9OM9P/view</a>'
)

# 2. Pitch & Presentatie
content = content.replace(
    'Olthuis, R. (2023). <span class="italic">Pitch & Presentatie</span> [PDF]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. (2023). <span class="italic">Pitch & Presentatie</span> [PDF]. Ongepubliceerd, Windesheim.<br><a href="https://drive.google.com/file/d/1VEw7VoXK8y2NgFWvxIao0CCdtkdQwB4R/view" target="_blank" class="text-accent hover:underline break-words">https://drive.google.com/file/d/1VEw7VoXK8y2NgFWvxIao0CCdtkdQwB4R/view</a>'
)

# 3. Salesplan Unica Building Services
content = content.replace(
    'Olthuis, R. e.a. (2024). <span class="italic">Salesplan Unica Building Services</span> [PDF]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. e.a. (2024). <span class="italic">Salesplan Unica Building Services</span> [PDF]. Ongepubliceerd, Windesheim.<br><a href="https://drive.google.com/file/d/1es7Vk1lV_21IisBqw2iKkiHNbB0h9W1P/view" target="_blank" class="text-accent hover:underline break-words">https://drive.google.com/file/d/1es7Vk1lV_21IisBqw2iKkiHNbB0h9W1P/view</a>'
)

# 4. Prototype Workflow Harmony Groep 4
content = content.replace(
    'Olthuis, R. e.a. (2024). <span class="italic">Prototype Workflow Harmony Groep 4</span> [Presentatie]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. e.a. (2024). <span class="italic">Prototype Workflow Harmony Groep 4</span> [Presentatie]. Ongepubliceerd, Windesheim.<br><a href="https://docs.google.com/presentation/d/1eesuZoJtQzAdtX_vmaYCLW7OvogD6mgQ/view" target="_blank" class="text-accent hover:underline break-words">https://docs.google.com/presentation/d/1eesuZoJtQzAdtX_vmaYCLW7OvogD6mgQ/view</a>'
)

# 5. Adviesrapport Business Analyse en Advies
content = content.replace(
    'Olthuis, R. (2025). <span class="italic">Adviesrapport Business Analyse en Advies</span> [PDF]. Ongepubliceerd, Universiteit Twente.',
    'Olthuis, R. (2025). <span class="italic">Adviesrapport Business Analyse en Advies</span> [PDF]. Ongepubliceerd, Universiteit Twente.<br><a href="https://docs.google.com/document/d/1bXjcOyGofwbbC1poxEf88lLKYsifM_hz/view" target="_blank" class="text-accent hover:underline break-words">https://docs.google.com/document/d/1bXjcOyGofwbbC1poxEf88lLKYsifM_hz/view</a>'
)

# 6. Businesscase Perron038 & Factory NEXT Prototype
content = content.replace(
    'Olthuis, R. e.a. (2026). <span class="italic">Businesscase Perron038 & Factory NEXT Prototype</span> [Webapplicatie].',
    'Olthuis, R. e.a. (2026). <span class="italic">Businesscase Perron038 & Factory NEXT Prototype</span> [Webapplicatie].<br><a href="https://businesscaseperron038.hugo-fransen03.workers.dev/" target="_blank" class="text-accent hover:underline break-words">https://businesscaseperron038.hugo-fransen03.workers.dev/</a>'
)

# 7. Whitepaper Vitens Water as a Service
content = content.replace(
    'Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Water as a Service</span> [PDF]. Ongepubliceerd.',
    'Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Water as a Service</span> [PDF]. Ongepubliceerd.<br><a href="https://drive.google.com/file/d/1zbaTOl800A24MG4o8scMMDTp5x3Ss1L0/view" target="_blank" class="text-accent hover:underline break-words">https://drive.google.com/file/d/1zbaTOl800A24MG4o8scMMDTp5x3Ss1L0/view</a>'
)

# 8. Whitepaper Vitens Mindset
content = content.replace(
    'Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Mindset</span> [PDF]. Ongepubliceerd.',
    'Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Mindset</span> [PDF]. Ongepubliceerd.<br><a href="https://drive.google.com/file/d/1EHu5kPJSsH389BJXJSdSb07LpDOhY7Jt/view" target="_blank" class="text-accent hover:underline break-words">https://drive.google.com/file/d/1EHu5kPJSsH389BJXJSdSb07LpDOhY7Jt/view</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

