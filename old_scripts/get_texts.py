import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def print_match(pattern, name):
    match = re.search(pattern, content, re.DOTALL)
    if match:
        print(f"--- {name} FOUND ---")
    else:
        print(f"--- {name} NOT FOUND ---")

# 1. about_text (Dutch)
print_match(r'about_text:\s*"Ik ben een ambitieuze.*?heen\.",', 'about_text_nl')

# 2. PDB Intro
print_match(r'Om mijn professionele identiteit.*?ambities\.', 'pdb_intro')

# 3. PDB Inst Frame
print_match(r'Binnen de opleiding Commerciële Economie aan Windesheim leer ik.*?handelen in onzekerheid\.', 'pdb_inst')
print_match(r'"Mijn ontwikkeling binnen dit frame draait om de transitie.*?"', 'pdb_inst_quote')

# 4. PDB Prof Frame
print_match(r'Mijn professionele frame richt zich op het snijvlak.*?blijven hangen in de ontwerpfase\.', 'pdb_prof')
print_match(r'<strong>Mijn belangrijkste inzicht:</strong> Perfectie is de vijand van vooruitgang.*?durf te werken\.', 'pdb_prof_quote')

# 5. Covey (Professionele Zelf)
print_match(r'<p>In de praktijk ben ik een initiatiefrijke.*?ruimte te geven aan anderen\.</p>\s*<p class="mt-2">Tijdens de pre-master.*?naar een hoger niveau te tillen\.</p>', 'covey_text')

# 6. Ruijters (Persoonlijke Zelf)
print_match(r'<p>Wie ik ben als professional, is diep geworteld in mijn persoonlijke drijfveren.*?met de externe context\.</p>\s*<p class="mt-2">Deze balans \(flow\) komt voor mij momenteel het sterkst naar voren.*?strategische marktontwikkeling\.</p>', 'ruijters_text')

# 7. Design Thinking
print_match(r'<p>Waar ik in de eerste jaren de neiging had om alles kapot te analyseren.*?simpelweg stilzet.*?</p>\s*<p class="mt-2">In lijn met <em>Design Thinking</em> ben ik steeds iteratiever gaan werken.*?complexe uitdagingen.*?</p>', 'dt_text')

# 8. Ikigai
print_match(r'<p>Mijn grootste les uit de afgelopen jaren is dat ik mijn natuurlijke analytische kracht niet overboord hoef te gooien.*?continu verandert\.</p>', 'ikigai_text')

# 9. VPMC Reflectie
print_match(r'De keuze voor de universitaire pre-master ontstond vanuit een sterke drive.*?aan de Universiteit Twente bij mij zou passen\.', 'vpmc_ref1')
print_match(r'"Mijn doel is om hierna door te stromen.*?waar ik naar op zoek ben\."', 'vpmc_quote')
print_match(r'De overstap van het hbo naar het wetenschappelijk onderwijs \(wo\) vereiste wel aanpassingsvermogen.*?persoonlijke en professionele ontwikkeling\.', 'vpmc_ref2')

