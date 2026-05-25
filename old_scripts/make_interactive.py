import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Covey - Professionele Zelf
old_covey = """<div class="pl-12 border-l border-zinc-800/60 space-y-4">
                        <p class="text-zinc-400 text-sm md:text-base md:text-[17px] leading-[1.8] font-light tracking-wide">
                            In de praktijk ben ik een initiatiefrijke, analytische en gestructureerde professional. Omdat ik hoog scoor op controle, had ik in het verleden de neiging om verantwoordelijkheid volledig naar me toe te trekken. Door intervisie en reflectie heb ik geleerd om proactiever binnen mijn cirkel van invloed te handelen (Covey, 1989) en meer ruimte te geven aan anderen in samenwerking. Tijdens de pre-master aan de Universiteit Twente (Olthuis, 2025; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar3'); setTimeout(() => document.getElementById('jaar3-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage III</button>) heb ik mijn besluitvaardigheid aanzienlijk versterkt door complexe data sneller te vertalen naar gefundeerde keuzes. Daarbij ben ik mij veel bewuster geworden van de waarde van constructief samenwerken: door actief te luisteren, waardering uit te spreken en open te staan voor kritische peer-feedback, lukt het me om diverse perspectieven beter te benutten en de gezamenlijke output in teamsessies (zoals tijdens de intervisies) naar een hoger niveau te tillen.
                        </p>
                    </div>"""

new_covey = """<div class="pl-12 border-l border-zinc-800/60 space-y-4">
                        <!-- Interactief Model: Covey -->
                        <div class="bg-zinc-900/40 border border-zinc-800 rounded-xl p-5 group cursor-pointer hover:border-zinc-700 transition-all" onclick="this.classList.toggle('expanded')">
                            <style>
                                .expanded .covey-details { display: block; }
                                .covey-details { display: none; }
                                .covey-circle { transition: all 0.5s ease; }
                                .expanded .covey-circle { transform: scale(1.05); border-color: #f97316; }
                            </style>
                            <div class="flex items-center gap-4 mb-2">
                                <div class="relative w-12 h-12 flex items-center justify-center">
                                    <div class="absolute inset-0 border border-zinc-600 rounded-full"></div>
                                    <div class="absolute inset-2 border-2 border-accent/50 rounded-full covey-circle group-hover:border-accent"></div>
                                </div>
                                <div>
                                    <h4 class="text-white font-bold font-display text-sm flex items-center gap-2">Cirkel van Invloed (Covey, 1989) <i data-lucide="chevron-down" class="w-4 h-4 text-zinc-500"></i></h4>
                                    <p class="text-xs text-zinc-500 font-mono uppercase tracking-wider">Klik om reflectie te lezen</p>
                                </div>
                            </div>
                            <div class="covey-details mt-4 pt-4 border-t border-zinc-800 text-zinc-400 text-sm leading-relaxed">
                                <p>In de praktijk ben ik een initiatiefrijke, analytische en gestructureerde professional. Omdat ik hoog scoor op controle, had ik in het verleden de neiging om verantwoordelijkheid volledig naar me toe te trekken. Door intervisie heb ik geleerd om proactiever binnen mijn <strong class="text-accent">cirkel van invloed</strong> te handelen en meer ruimte te geven aan anderen.</p>
                                <p class="mt-2">Tijdens de pre-master (Olthuis, 2025; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar3'); setTimeout(() => document.getElementById('jaar3-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage III</button>) heb ik mijn besluitvaardigheid versterkt door complexe data sneller te vertalen naar keuzes. Ik ben me bewuster geworden van constructief samenwerken: actief luisteren en kritische peer-feedback benutten om gezamenlijke output in teamsessies naar een hoger niveau te tillen.</p>
                            </div>
                        </div>
                    </div>"""

# 2. Ruijters - Persoonlijke Zelf
old_ruijters = """<div class="pl-12 border-l border-zinc-800/60 space-y-4">
                        <p class="text-zinc-300 text-sm md:text-base md:text-[17px] leading-[1.8] font-light tracking-wide">
                            Wie ik ben als professional, is diep geworteld in mijn persoonlijke drijfveren: de wil om te ontwikkelen, impact te maken en verantwoordelijkheid te dragen. Volgens het model <em>Mijn Binnenste Buiten</em> (Ruijters, 2015) is er pas sprake van flow wanneer deze innerlijke waarden in balans zijn met de externe context. Deze balans komt voor mij momenteel het sterkst naar voren in mijn afstudeeronderzoek voor Axelio (Olthuis, 2026b; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('afstuderen-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage V</button>), waar ik eigenaarschap combineer met strategische marktontwikkeling.
                        </p>
                    </div>"""

new_ruijters = """<div class="pl-12 border-l border-zinc-800/60 space-y-4">
                        <!-- Interactief Model: Ruijters -->
                        <div class="bg-zinc-900/40 border border-zinc-800 rounded-xl p-5 group cursor-pointer hover:border-zinc-700 transition-all" onclick="this.classList.toggle('expanded')">
                            <style>
                                .expanded .ruijters-details { display: block; }
                                .ruijters-details { display: none; }
                                .expanded .ruijters-balance { width: 100%; opacity: 1; }
                                .ruijters-balance { width: 0%; opacity: 0; transition: all 1s ease; }
                            </style>
                            <div class="flex items-center gap-4 mb-2">
                                <div class="w-12 h-12 flex flex-col items-center justify-center border-l-2 border-r-2 border-accent/30 gap-1 overflow-hidden">
                                    <div class="w-full h-1 bg-accent/20 rounded">
                                        <div class="h-full bg-accent ruijters-balance rounded"></div>
                                    </div>
                                    <div class="w-full h-1 bg-accent/20 rounded">
                                        <div class="h-full bg-accent ruijters-balance rounded" style="transition-delay: 0.2s;"></div>
                                    </div>
                                </div>
                                <div>
                                    <h4 class="text-white font-bold font-display text-sm flex items-center gap-2">Mijn Binnenste Buiten (Ruijters, 2015) <i data-lucide="chevron-down" class="w-4 h-4 text-zinc-500"></i></h4>
                                    <p class="text-xs text-zinc-500 font-mono uppercase tracking-wider">Klik om balans / flow te zien</p>
                                </div>
                            </div>
                            <div class="ruijters-details mt-4 pt-4 border-t border-zinc-800 text-zinc-300 text-sm leading-relaxed">
                                <p>Wie ik ben als professional, is diep geworteld in mijn persoonlijke drijfveren: de wil om te ontwikkelen, impact te maken en verantwoordelijkheid te dragen. Er is pas sprake van <strong>flow</strong> wanneer deze innerlijke waarden in balans zijn met de externe context.</p>
                                <p class="mt-2">Deze balans (flow) komt voor mij momenteel het sterkst naar voren in mijn afstudeeronderzoek voor Axelio (Olthuis, 2026b; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('afstuderen-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage V</button>), waar ik eigenaarschap combineer met strategische marktontwikkeling.</p>
                            </div>
                        </div>
                    </div>"""


content = content.replace(old_covey, new_covey)
content = content.replace(old_ruijters, new_ruijters)

# 3. Ikigai and Design Thinking
# These are in the javascript translation dictionary. Let's find it.
# Wait, replacing complex HTML in JS is hard. Let's just do it directly in HTML and remove it from translation.
ikigai_block_start = '<div class="text-zinc-300 text-sm leading-relaxed space-y-4 font-sans mb-4" id="ikigai-reflection" data-i18n="ikigai_reflection">'
ikigai_block_end = '                        </div>'

# We will regex replace the whole div#ikigai-reflection.
ikigai_pattern = r'<div class="text-zinc-300 text-sm leading-relaxed space-y-4 font-sans mb-4" id="ikigai-reflection" data-i18n="ikigai_reflection">.*?</div>'

new_ikigai = """<!-- Interactief Ikigai & Design Thinking Model -->
                        <div class="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5 mt-4 space-y-4" id="ikigai-interactive">
                            <!-- Design Thinking Flow -->
                            <div class="group cursor-pointer p-4 bg-zinc-950 rounded-lg border border-zinc-850 hover:border-zinc-700 transition-all" onclick="this.classList.toggle('expanded')">
                                <style>
                                    .expanded .dt-details { display: block; }
                                    .dt-details { display: none; }
                                    .dt-dot { transition: transform 0.3s; }
                                    .expanded .dt-dot { transform: scale(1.5); background-color: #f97316; }
                                </style>
                                <div class="flex items-center gap-3">
                                    <div class="flex items-center gap-1">
                                        <div class="w-2 h-2 rounded-full bg-zinc-700 dt-dot"></div>
                                        <div class="w-4 h-px bg-zinc-700"></div>
                                        <div class="w-2 h-2 rounded-full bg-zinc-700 dt-dot" style="transition-delay: 0.1s"></div>
                                        <div class="w-4 h-px bg-zinc-700"></div>
                                        <div class="w-2 h-2 rounded-full bg-zinc-700 dt-dot" style="transition-delay: 0.2s"></div>
                                    </div>
                                    <div>
                                        <h4 class="text-white font-bold text-sm">Design Thinking (Brown, 2009)</h4>
                                        <p class="text-[10px] text-zinc-500 uppercase font-mono">Van analyse-paralyse naar iteratieve actie (Klik)</p>
                                    </div>
                                </div>
                                <div class="dt-details mt-4 pt-4 border-t border-zinc-800 text-zinc-300 text-sm leading-relaxed">
                                    <p>Waar ik in de eerste jaren de neiging had om alles kapot te analyseren, heb ik tijdens mijn projecten bij Vitens en Perron038 ervaren dat wachten op 100% zekerheid je simpelweg stilzet (<button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar4'); setTimeout(() => document.getElementById('jaar4-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline inline-block">Bijlage IV</button>).</p>
                                    <p class="mt-2">In lijn met <em>Design Thinking</em> ben ik steeds iteratiever gaan werken. Dit gaf me de ruimte om daadwerkelijk verantwoordelijkheid te pakken en eigenaarschap te tonen in complexe uitdagingen (zie afstudeeronderzoek <button onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('afstuderen-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline inline-block">Bijlage V</button>).</p>
                                </div>
                            </div>
                            
                            <!-- Ikigai Venn -->
                            <div class="group cursor-pointer p-4 bg-zinc-950 rounded-lg border border-zinc-850 hover:border-zinc-700 transition-all" onclick="this.classList.toggle('expanded')">
                                <style>
                                    .expanded .iki-details { display: block; }
                                    .iki-details { display: none; }
                                    .iki-circle { transition: opacity 0.5s, transform 0.5s; opacity: 0.3; }
                                    .expanded .iki-circle { opacity: 0.8; transform: scale(1.1); }
                                </style>
                                <div class="flex items-center gap-4">
                                    <div class="relative w-12 h-12">
                                        <div class="absolute top-0 left-2 w-6 h-6 rounded-full bg-accent iki-circle mix-blend-screen"></div>
                                        <div class="absolute bottom-1 left-0 w-6 h-6 rounded-full bg-blue-500 iki-circle mix-blend-screen" style="transition-delay: 0.1s"></div>
                                        <div class="absolute bottom-1 right-1 w-6 h-6 rounded-full bg-purple-500 iki-circle mix-blend-screen" style="transition-delay: 0.2s"></div>
                                    </div>
                                    <div>
                                        <h4 class="text-white font-bold text-sm">Ikigai Balans</h4>
                                        <p class="text-[10px] text-zinc-500 uppercase font-mono">De perfecte overlap vinden (Klik)</p>
                                    </div>
                                </div>
                                <div class="iki-details mt-4 pt-4 border-t border-zinc-800 text-zinc-300 text-sm leading-relaxed">
                                    <p>Mijn grootste les uit de afgelopen jaren is dat ik mijn natuurlijke analytische kracht niet overboord hoef te gooien. Het gaat om de <strong>Ikigai balans</strong>: de analyse gebruiken als fundament, om van daaruit durf te tonen, keuzes te maken en daadkrachtig te handelen in een omgeving die continu verandert.</p>
                                </div>
                            </div>
                        </div>"""

content = re.sub(ikigai_pattern, new_ikigai, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
