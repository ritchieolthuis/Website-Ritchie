import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Bronnenlijst (Reference List)
old_ref_1 = 'Windesheim. (2026). <span class="italic">Skills Guide</span>. Data ingevuld door Hugo, Thijmen en Ritchie.'

new_refs = """Windesheim. (2026). <span class="italic">Ingevulde CE Skillsguide door medestudenten</span> [Bijlage VI]. Ongepubliceerd manuscript, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2023). <span class="italic">Portfolio Jaar 1: Fundament & Professionele Ontwikkeling</span> [Bijlage I]. Ongepubliceerd portfolio, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2024). <span class="italic">Portfolio Jaar 2: Business Development | Unica Building Services</span> [Bijlage II]. Ongepubliceerd portfolio, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2025). <span class="italic">Portfolio Jaar 3: Minor Financiële Besluitvorming & Pre-master Business Administration</span> [Bijlage III]. Ongepubliceerd portfolio, Universiteit Twente.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2026a). <span class="italic">Portfolio Jaar 4: Young Professional Commerce Programme</span> [Bijlage IV]. Ongepubliceerd portfolio, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2026b). <span class="italic">Afstudeerportfolio: Axelio / Agrio UK Market Entry</span> [Bijlage V]. Ongepubliceerd portfolio, Windesheim."""
content = content.replace(old_ref_1, new_refs)

# 2. Add APA to text and link to evidence
# De Fundering (Jaar 1)
content = content.replace(
    'Mijn reis begon met een sterke drive om de overstap van mbo naar hbo te bewijzen.',
    'Mijn reis begon met een sterke drive om de overstap van mbo naar hbo te bewijzen (Olthuis, 2023; zie <button onclick="window.showSemesterPage(\'jaar1\')" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>).'
)

# De Praktijk (Jaar 2 & 4)
content = content.replace(
    'Door projecten zoals <strong class="text-white">Vitens</strong>, <strong class="text-white">Perron038</strong> en <strong class="text-white">Unica</strong> heb ik geleerd dat perfectie niet bestaat in innovatie.',
    'Door projecten zoals <strong class="text-white">Unica</strong> (Olthuis, 2024; zie <button onclick="window.showSemesterPage(\'jaar2\')" class="text-accent hover:underline mx-1">Bijlage II</button>), en <strong class="text-white">Vitens</strong> en <strong class="text-white">Perron038</strong> (Olthuis, 2026a; zie <button onclick="window.showSemesterPage(\'jaar4\')" class="text-accent hover:underline mx-1">Bijlage IV</button>) heb ik geleerd dat perfectie niet bestaat in innovatie.'
)

# Update the evidence buttons in De Praktijk
content = content.replace(
    '<i data-lucide="arrow-right" class="w-3.5 h-3.5"></i> Bewijs: Unica (Jaar 2)',
    '<i data-lucide="paperclip" class="w-3.5 h-3.5"></i> Bijlage II - Unica (Jaar 2)'
)
content = content.replace(
    '<i data-lucide="arrow-right" class="w-3.5 h-3.5"></i> Bewijs: Vitens & Perron038 (Jaar 4)',
    '<i data-lucide="paperclip" class="w-3.5 h-3.5"></i> Bijlage IV - Vitens & Perron038 (Jaar 4)'
)

# Wie Ik Nu Ben (Afstuderen & Minor)
content = content.replace(
    'Ik balanceer mijn natuurlijke behoefte aan structuur met de noodzaak om in complexe omgevingen iteratief te blijven werken en verantwoordelijkheid te dragen voor het resultaat.',
    'Ik balanceer mijn natuurlijke behoefte aan structuur met de noodzaak om in complexe omgevingen iteratief te blijven werken en verantwoordelijkheid te dragen voor het resultaat. Deze balans is sterk ontwikkeld tijdens de pre-master (Olthuis, 2025; zie <button onclick="window.showSemesterPage(\'jaar3\')" class="text-accent hover:underline mx-1">Bijlage III</button>) en komt volledig samen in mijn afstudeeronderzoek voor Axelio (Olthuis, 2026b; zie <button onclick="window.showSemesterPage(\'afstuderen\')" class="text-accent hover:underline mx-1">Bijlage V</button>).'
)

# 3. Skills Visualization Text Update
old_skills_title = '<h3 class="text-2xl font-bold text-white mb-4" data-i18n="skills_viz_title">Skills Visualization</h3>'
new_skills_title = '''<h3 class="text-2xl font-bold text-white mb-2" data-i18n="skills_viz_title">Skills Visualization</h3>
                    <p class="text-zinc-300 text-sm mb-6 leading-relaxed">
                        Onderstaande visualisatie toont de ontwikkeling van mijn competenties. Deze data is gebaseerd op de officiële CE Skillsguide en is gevalideerd door actieve feedbackrondes en intervisie met medestudenten gedurende de opleiding (Windesheim, 2026; zie <button onclick="window.scrollTo({top: document.getElementById('pdb-bronnen').offsetTop, behavior: 'smooth'})" class="text-accent hover:underline font-bold">Bijlage VI</button>).
                    </p>'''
content = content.replace(old_skills_title, new_skills_title)

# Update the little text under the table
content = content.replace(
    '* Windesheim. (2026). Skills Guide. Data ingevuld door Hugo, Thijmen en Ritchie.',
    '* Windesheim. (2026). Ingevulde CE Skillsguide door medestudenten (Bijlage VI).'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

