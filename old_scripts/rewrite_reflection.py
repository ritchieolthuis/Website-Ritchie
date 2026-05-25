import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the entire #pdb-story-container inner content up to SKILLS VISUALIZATION
old_story_pattern = re.compile(r'<!-- STORY CHAPTER: FOUNDATION -->.*?<!-- SECTION: SKILLS VISUALIZATION -->', re.DOTALL)

new_story = """<!-- STORY CHAPTER: INSTITUTIONEEL FRAME -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-accent text-black flex items-center justify-center font-bold text-xs">01</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Institutioneel Frame</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800 space-y-4">
                        <p class="text-zinc-400 text-sm md:text-base leading-relaxed">
                            Binnen de opleiding Commerciële Economie aan Windesheim leer ik waarde te creëren in een omgeving die voortdurend verandert. Mijn reis begon met de overtuiging dat ik de overstap van mbo naar hbo succesvol wilde afronden (Olthuis, 2023; zie <button onclick="window.showSemesterPage('jaar1')" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>). De CE Skills Guide (Windesheim, 2026; zie <button onclick="window.scrollTo({top: document.getElementById('pdb-bronnen').offsetTop, behavior: 'smooth'})" class="text-accent hover:underline inline-block mx-1">Bijlage VI</button>) vormt hierbij een belangrijk kompas om te reflecteren op mijn vaardigheden. Van de zestien vaardigheden focus ik mij met name op Initiatief, Samenwerken, Verantwoordelijkheid en het durven handelen in onzekerheid.
                        </p>
                        <div class="text-xs p-4 bg-zinc-900/50 rounded-lg text-zinc-300 font-medium border border-zinc-800">
                             "Mijn ontwikkeling binnen dit frame draait om de transitie van een uitvoerende student naar een strategische denker die theorie koppelt aan praktijkwaarde."
                        </div>
                    </div>
                </div>

                <!-- STORY CHAPTER: PROFESSIONEEL FRAME -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">02</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Professioneel Frame</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800 space-y-4">
                        <p class="text-zinc-400 text-sm md:text-base leading-relaxed">
                            Mijn professionele frame richt zich op het snijvlak van commerciële strategie en innovatie. Tijdens projecten zoals <strong class="text-white">Unica</strong> (Olthuis, 2024; zie <button onclick="window.showSemesterPage('jaar2')" class="text-accent hover:underline mx-1">Bijlage II</button>) en <strong class="text-white">Vitens / Perron038</strong> (Olthuis, 2026a; zie <button onclick="window.showSemesterPage('jaar4')" class="text-accent hover:underline mx-1">Bijlage IV</button>) heb ik ervaren hoe cruciaal het is om analytisch denken om te zetten in concrete business impact. Hierbij hanteer ik principes uit <em>Design Thinking</em> (Brown, 2009): sneller testen, valideren en bijsturen in plaats van te blijven hangen in de ontwerpfase.
                        </p>
                        <div class="text-zinc-300 text-sm p-4 bg-zinc-900/50 rounded-lg border border-zinc-800 font-medium mt-4">
                            <strong>Mijn belangrijkste inzicht:</strong> Perfectie is de vijand van vooruitgang. Ik creëer de meeste waarde wanneer ik mijn drang naar controle loslaat en iteratief durf te werken.
                        </div>
                    </div>
                </div>

                <!-- STORY CHAPTER: PROFESSIONELE ZELF -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">03</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Professionele Zelf</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800 space-y-4">
                        <p class="text-zinc-400 text-sm md:text-base leading-relaxed">
                            In de praktijk ben ik een initiatiefrijke, analytische en gestructureerde professional. Omdat ik hoog scoor op controle, had ik in het verleden de neiging om verantwoordelijkheid volledig naar me toe te trekken. Door intervisie en reflectie heb ik geleerd om proactiever binnen mijn cirkel van invloed te handelen (Covey, 1989) en meer ruimte te geven aan anderen in samenwerking. Tijdens de pre-master aan de Universiteit Twente (Olthuis, 2025; zie <button onclick="window.showSemesterPage('jaar3')" class="text-accent hover:underline mx-1">Bijlage III</button>) heb ik mijn besluitvaardigheid aanzienlijk versterkt door complexe data sneller te vertalen naar gefundeerde keuzes.
                        </p>
                    </div>
                </div>

                <!-- STORY CHAPTER: PERSOONLIJKE ZELF -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">04</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Persoonlijke Zelf</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800 space-y-4">
                        <p class="text-zinc-300 text-sm md:text-base leading-relaxed">
                            Wie ik ben als professional, is diep geworteld in mijn persoonlijke drijfveren: de wil om te ontwikkelen, impact te maken en verantwoordelijkheid te dragen. Volgens het model <em>Mijn Binnenste Buiten</em> (Ruijters, 2015) is er pas sprake van flow wanneer deze innerlijke waarden in balans zijn met de externe context. Deze balans komt voor mij momenteel het sterkst naar voren in mijn afstudeeronderzoek voor Axelio (Olthuis, 2026b; zie <button onclick="window.showSemesterPage('afstuderen')" class="text-accent hover:underline mx-1">Bijlage V</button>), waar ik eigenaarschap combineer met strategische marktontwikkeling.
                        </p>
                    </div>
                </div>

                <!-- SECTION: SKILLS VISUALIZATION -->"""

content = re.sub(old_story_pattern, new_story, content)

# Also update the title of the PDB section to reflect this structured reflection
content = content.replace(
    '<!-- Personal Branding Dossier Story Chapters -->',
    '<!-- Personal Branding Dossier Story Chapters -->\n            <div class="max-w-6xl mx-auto mb-4">\n                <p class="text-zinc-300 text-lg leading-relaxed">\n                    Om mijn professionele identiteit als student Commerciële Economie inzichtelijk te maken, maak ik gebruik van het model <em>Mijn Binnenste Buiten</em> van Manon Ruijters (2015). Door mijn ontwikkeling binnen de vier frames te beschrijven, geef ik een onderbouwde reflectie op mijn groei, keuzes en ambities.\n                </p>\n            </div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

