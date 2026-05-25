import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Axelio logo
content = content.replace('src="assets/axelio.png" alt="Axelio" class="h-14 w-auto object-contain logo-white"', 
                          'src="assets/axelio_white_text.png" alt="Axelio" class="h-14 w-auto object-contain opacity-60 hover:opacity-100 transition-opacity duration-300 mix-blend-screen"')

# 2. Transform the grid in Semester pages to roadmap timelines
# We'll use a regex to find all <div class="grid grid-cols-1 md:grid-cols-2 ..."> inside the semester pages and replace them.
# Wait, this is tricky to do robustly with regex. Let's do it with specific replacements for each page to be safe.

# Jaar 1 Grid Replacement
jaar1_old = """                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                            <div class="p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800 hover:border-zinc-700 transition-colors">
                                <h4 class="text-sm font-mono text-white uppercase mb-3">Projectmatig Werken</h4>
                                <p class="text-zinc-400 text-sm leading-relaxed">
                                    Binnen groepsprojecten werd al vroeg verantwoordelijkheid genomen voor planning, kwaliteit en voortgang. Tegelijkertijd ontstond inzicht in de eigen werkwijze, waarbij de focus vaak sterk lag op analyse, voorbereiding en controle voordat daadwerkelijk tot uitvoering werd overgegaan. Hierdoor werd duidelijk dat verdere ontwikkeling vooral lag in het sneller vertalen van analyses naar concrete acties en besluitvorming.
                                </p>
                            </div>
                            
                            <div class="p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800 hover:border-zinc-700 transition-colors">
                                <h4 class="text-sm font-mono text-white uppercase mb-3">Vaardigheden & Groei</h4>
                                <p class="text-zinc-400 text-sm leading-relaxed">
                                    Daarnaast werd in jaar 1 aanvullende Nederlandse bijles gevolgd om academische schrijfvaardigheid, grammatica en professionele communicatie verder te versterken als ondersteuning voor tentamens, rapportages en hbo-niveau.
                                </p>
                            </div>
                        </div>"""
jaar1_new = """                        <div class="relative pl-8 border-l border-zinc-800 ml-2 my-8">
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold">Projectmatig Werken</h4>
                                <p class="text-zinc-300 text-base leading-relaxed">
                                    Binnen groepsprojecten werd al vroeg verantwoordelijkheid genomen voor planning, kwaliteit en voortgang. Tegelijkertijd ontstond inzicht in de eigen werkwijze, waarbij de focus vaak sterk lag op analyse, voorbereiding en controle voordat daadwerkelijk tot uitvoering werd overgegaan. Hierdoor werd duidelijk dat verdere ontwikkeling vooral lag in het sneller vertalen van analyses naar concrete acties en besluitvorming.
                                </p>
                            </div>
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold">Vaardigheden & Groei</h4>
                                <p class="text-zinc-300 text-base leading-relaxed">
                                    Daarnaast werd in jaar 1 aanvullende Nederlandse bijles gevolgd om academische schrijfvaardigheid, grammatica en professionele communicatie verder te versterken als ondersteuning voor tentamens, rapportages en hbo-niveau.
                                </p>
                            </div>
                        </div>"""
content = content.replace(jaar1_old, jaar1_new)

# Jaar 2 Grid Replacement
jaar2_old = """                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                            <div class="p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800">
                                <h4 class="text-sm font-mono text-white uppercase mb-4 flex items-center gap-2">
                                    <span class="w-2 h-2 bg-emerald-500 rounded-full"></span> Sterke punten (Unica)
                                </h4>
                                <ul class="space-y-2 text-zinc-400 text-sm">
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Sterke marktpositie binnen de technische dienstverlening</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Langdurige klantrelaties</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Expertise op het gebied van duurzaamheid</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Innovatieve oplossingen zoals Building Insights</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Focus op gezondheid, veiligheid en energie-efficiëntie</li>
                                </ul>
                            </div>
                            
                            <div class="p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800">
                                <h4 class="text-sm font-mono text-white uppercase mb-4 flex items-center gap-2">
                                    <span class="w-2 h-2 bg-red-500 rounded-full"></span> Belangrijke uitdagingen
                                </h4>
                                <ul class="space-y-2 text-zinc-400 text-sm">
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Personeelstekorten binnen de technische sector</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Toenemende concurrentie</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Stijgende kosten van duurzame oplossingen</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Complexiteit rondom regelgeving</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Smart Building-oplossingen toegankelijker en schaalbaarder maken</li>
                                </ul>
                            </div>
                        </div>"""

jaar2_new = """                        <div class="relative pl-8 border-l border-zinc-800 ml-2 my-8">
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold">Sterke Punten (Unica)</h4>
                                <ul class="space-y-2 text-zinc-300 text-base leading-relaxed">
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Sterke marktpositie binnen de technische dienstverlening</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Langdurige klantrelaties & expertise in duurzaamheid</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Innovatieve oplossingen zoals Building Insights</li>
                                </ul>
                            </div>
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold">Belangrijke Uitdagingen</h4>
                                <ul class="space-y-2 text-zinc-300 text-base leading-relaxed">
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Personeelstekorten & toenemende concurrentie</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Stijgende kosten & complexe regelgeving</li>
                                    <li class="flex items-start gap-2"><span class="text-accent">•</span> Smart Building-oplossingen toegankelijker maken</li>
                                </ul>
                            </div>
                        </div>"""
content = content.replace(jaar2_old, jaar2_new)

# Jaar 3 Grid Replacement
jaar3_old = """                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                            <div class="p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800 space-y-3">
                                <h4 class="text-sm font-mono text-white uppercase flex items-center gap-2">
                                    <i data-lucide="line-chart" class="w-4 h-4"></i> Financiële Besluitvorming
                                </h4>
                                <p class="text-zinc-400 text-sm leading-relaxed">
                                    Deze minor richtte zich op financiële analyses, strategische besluitvorming en bedrijfseconomische vraagstukken binnen organisaties. Hierbij werd gewerkt met praktijkgerichte casuïstiek, financiële kengetallen, jaarverslagen en bedrijfssimulaties waarin commerciële en financiële keuzes directe invloed hadden op organisatieresultaten.
                                </p>
                                <p class="text-zinc-400 text-sm leading-relaxed">
                                    Daarnaast werd gewerkt met financiële software en datagedreven analyses om beter inzicht te krijgen in de manier waarop organisaties financiële informatie gebruiken binnen strategische besluitvorming.
                                </p>
                            </div>
                            
                            <div class="p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800 space-y-3">
                                <h4 class="text-sm font-mono text-white uppercase flex items-center gap-2">
                                    <i data-lucide="graduation-cap" class="w-4 h-4"></i> Pre-master (UT)
                                </h4>
                                <p class="text-zinc-400 text-sm leading-relaxed">
                                    Parallel hieraan werd de pre-master Business Administration aan de Universiteit Twente gevolgd. Deze universitaire transfer minor richtte zich op academisch onderzoek, business management, strategische analyse en onderzoeksmethodologie op universitair niveau.
                                </p>
                                <div class="text-xs text-zinc-500 font-mono mt-2">
                                    Vakkenpakket omvatte onder andere:
                                    <div class="flex flex-wrap gap-2 mt-2">
                                        <span class="px-2 py-0.5 bg-zinc-800 rounded">Organization Theory</span>
                                        <span class="px-2 py-0.5 bg-zinc-800 rounded">Research Methodology</span>
                                        <span class="px-2 py-0.5 bg-zinc-800 rounded">Academic Skills</span>
                                        <span class="px-2 py-0.5 bg-zinc-800 rounded">Descriptive Statistics</span>
                                        <span class="px-2 py-0.5 bg-zinc-800 rounded">Global Entrepreneurship</span>
                                        <span class="px-2 py-0.5 bg-zinc-800 rounded">Researching Strategy</span>
                                    </div>
                                </div>
                            </div>
                        </div>"""
jaar3_new = """                        <div class="relative pl-8 border-l border-zinc-800 ml-2 my-8">
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold flex items-center gap-2">
                                    <i data-lucide="line-chart" class="w-4 h-4"></i> Financiële Besluitvorming
                                </h4>
                                <p class="text-zinc-300 text-base leading-relaxed">
                                    Gericht op financiële analyses, strategische besluitvorming en bedrijfseconomische vraagstukken. Gewerkt met praktijkgerichte casuïstiek, financiële kengetallen en simulaties. Data-gedreven analyses gaven inzicht in de koppeling tussen financiële informatie en strategische koers.
                                </p>
                            </div>
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold flex items-center gap-2">
                                    <i data-lucide="graduation-cap" class="w-4 h-4"></i> Pre-master (Universiteit Twente)
                                </h4>
                                <p class="text-zinc-300 text-base leading-relaxed">
                                    Parallel hieraan werd de pre-master Business Administration gevolgd, met een focus op academisch onderzoek, strategische analyse en onderzoeksmethodologie op universitair niveau.
                                </p>
                                <div class="flex flex-wrap gap-2 mt-4">
                                    <span class="px-2 py-1 bg-zinc-800/50 text-zinc-300 text-[10px] uppercase font-bold rounded border border-zinc-700">Organization Theory</span>
                                    <span class="px-2 py-1 bg-zinc-800/50 text-zinc-300 text-[10px] uppercase font-bold rounded border border-zinc-700">Research Methodology</span>
                                    <span class="px-2 py-1 bg-zinc-800/50 text-zinc-300 text-[10px] uppercase font-bold rounded border border-zinc-700">Academic Skills</span>
                                </div>
                            </div>
                        </div>"""
content = content.replace(jaar3_old, jaar3_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

