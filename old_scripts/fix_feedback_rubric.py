import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a sentence about feedback, listening, and perspectives to "Professionele Zelf"
old_text = 'Tijdens de pre-master aan de Universiteit Twente (Olthuis, 2025; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar3\'); setTimeout(() => document.getElementById(\'jaar3-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline mx-1">Bijlage III</button>) heb ik mijn besluitvaardigheid aanzienlijk versterkt door complexe data sneller te vertalen naar gefundeerde keuzes.'

new_text = old_text + ' Daarbij ben ik mij veel bewuster geworden van de waarde van constructief samenwerken: door actief te luisteren, waardering uit te spreken en open te staan voor kritische peer-feedback, lukt het me om diverse perspectieven beter te benutten en de gezamenlijke output in teamsessies (zoals tijdens de intervisies) naar een hoger niveau te tillen.'

content = content.replace(old_text, new_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

