import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert About
about_new = r"<div class='text-zinc-400 leading-relaxed font-sans'>\s*<p class='mb-4 text-sm md:text-base'>Vierdejaarsstudent.*?</div>\s*<button.*?Lees Volledig Profiel <i data-lucide='chevron-down' class='w-4 h-4'></i></button>\s*</div>"
about_old = '''<p class="text-zinc-400 leading-relaxed group-hover:text-zinc-300 transition-colors duration-300 font-sans" data-i18n="about_text">
                        Vierdejaarsstudent Commerciële Economie (Hogeschool Windesheim) met afgeronde minors in Bedrijfskunde (Pre-master Universiteit Twente) en Financiële Besluitvorming. Het profiel richt zich op kwantitatieve en kwalitatieve analyse, iteratief projectmanagement en datagedreven besluitvorming ter ondersteuning van bedrijfskundige vraagstukken.<br><br>De beroepspraktijk bestaat uit het analyseren van procesknelpunten en het implementeren van meetbare procesverbeteringen. De nadruk ligt op de toepassing van academische theory in de commerciële praktijk om efficiëntie en bedrijfsresultaten te optimaliseren.
                    </p>'''

content = re.sub(about_new, about_old, content, flags=re.DOTALL)

# Revert JS about strings (which I also modified)
en_js_new = r'about_text: "<div class=\'text-zinc-400 leading-relaxed font-sans\'>.*?</div>",'
en_js_old = '''about_text: "Fourth-year Commercial Economics student (Windesheim) with minors in Business Administration and Financial Decision Making. Profile focuses on quantitative and qualitative analysis, iterative project management, and data-driven decision making to support business challenges.<br><br>Professional practice consists of analyzing process bottlenecks and implementing measurable process improvements. The emphasis is on applying academic theory in commercial practice to optimize efficiency and business results.",'''
content = re.sub(en_js_new, en_js_old, content, count=1, flags=re.DOTALL)

nl_js_new = r'about_text: "<div class=\'text-zinc-400 leading-relaxed font-sans\'>.*?</div>",'
nl_js_old = '''about_text: "Vierdejaarsstudent Commerciële Economie (Hogeschool Windesheim) met afgeronde minors in Bedrijfskunde en Financiële Besluitvorming. Het profiel richt zich op kwantitatieve en kwalitatieve analyse, iteratief projectmanagement en datagedreven besluitvorming ter ondersteuning van bedrijfskundige vraagstukken.<br><br>De beroepspraktijk bestaat uit het analyseren van procesknelpunten en het implementeren van meetbare procesverbeteringen. De nadruk ligt op de toepassing van academische theorie in de commerciële praktijk om efficiëntie en bedrijfsresultaten te optimaliseren.",'''
content = re.sub(nl_js_new, nl_js_old, content, count=1, flags=re.DOTALL)

# 2. Revert Inst Frame
inst_new = r'<!-- STORY CHAPTER: INSTITUTIONEEL FRAME -->\s*<div class="reveal-on-scroll relative">.*?<div id="inst-frame-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">.*?</div>\s*</div>\s*</div>\s*</div>'
inst_old = '''<!-- STORY CHAPTER: INSTITUTIONEEL FRAME -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-accent text-black flex items-center justify-center font-bold text-xs">01</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Institutioneel Frame</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800/60 space-y-4">
                        <p class="text-zinc-400 text-sm md:text-base md:text-[17px] leading-[1.8] font-light tracking-wide">
                            De vooropleiding bestaat uit een afgeronde mbo-opleiding, gevolgd door de hbo-bachelor Commerciële Economie (Olthuis, 2023; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar1'); setTimeout(() => document.getElementById('jaar1-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>). De meting van vaardigheden geschiedt volgens de beoordelingscriteria uit de CE Skills Guide (Windesheim, 2026; zie <a href="https://docs.google.com/spreadsheets/d/1XqhvW2usQ9FYD7Tye1TzObGUiBtvB9cJrIJR7dbGhWg/edit?usp=drive_link" target="_blank" class="text-accent hover:underline font-bold inline-block mx-1">Bijlage VI</a>). De competentieontwikkeling concentreert zich op de meetbare criteria: Initiatief, Samenwerken, Verantwoordelijkheid (Eigenaarschap), Analytisch denken, Besluitvaardigheid en Iteratief werken (Design Thinking).
                        </p>
                        <div class="text-xs p-4 bg-zinc-900/50 rounded-lg text-zinc-300 font-medium border border-zinc-800">
                             "De vereiste ontwikkeling binnen het institutionele frame bestaat uit de verschuiving van operationele taken (mbo-niveau) naar strategische analyse en advisering (hbo-niveau)."
                        </div>
                    </div>
                </div>'''
content = re.sub(inst_new, inst_old, content, count=1, flags=re.DOTALL)

# 3. Revert Prof Frame
prof_new = r'<!-- STORY CHAPTER: PROFESSIONEEL FRAME -->\s*<div class="reveal-on-scroll relative">.*?<div id="prof-frame-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">.*?</div>\s*</div>\s*</div>\s*</div>'
prof_old = '''<!-- STORY CHAPTER: PROFESSIONEEL FRAME -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">02</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Professioneel Frame</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800/60 space-y-4">
                        <p class="text-zinc-400 text-sm md:text-base md:text-[17px] leading-[1.8] font-light tracking-wide">
                            Binnen de beroepspraktijk zijn adviesrapporten en beroepsproducten opgeleverd voor opdrachtgevers waaronder <strong class="text-white">Unica</strong> (Olthuis, 2024; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar2'); setTimeout(() => document.getElementById('jaar2-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage II</button>) en <strong class="text-white">Vitens / Perron038</strong> (Olthuis, 2026a; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar4'); setTimeout(() => document.getElementById('jaar4-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage IV</button>). Uit de projectevaluaties blijkt dat lange theorie- en analysefasen leiden tot vertraging in de doorlooptijd. Derhalve is de methodiek <em>Design Thinking</em> (Brown, 2009) geïmplementeerd om projecten middels kortcyclische testen en frequente validatie iteratief op te leveren.
                        </p>
                        <div class="text-zinc-300 text-sm p-4 bg-zinc-900/50 rounded-lg border border-zinc-800 font-medium mt-4">
                            <strong>Kritisch inzicht:</strong> Het minimaliseren van de ontwikkeltijd per projectfase leidt tot snellere feedbackloops en een hogere implementatiegraad bij de opdrachtgever.
                        </div>
                    </div>
                </div>'''
content = re.sub(prof_new, prof_old, content, count=1, flags=re.DOTALL)

# 4. Revert Prof Zelf
profzelf_new = r'<!-- STORY CHAPTER: PROFESSIONELE ZELF -->\s*<div class="reveal-on-scroll relative">.*?<div id="prof-zelf-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">.*?</div>\s*</div>\s*</div>\s*</div>'
profzelf_old = '''<!-- STORY CHAPTER: PROFESSIONELE ZELF -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">03</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Professionele Zelf</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800/60 space-y-4">
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
                                <p>Uit feedbackverslagen blijkt initieel een sterke neiging tot taaktoe-eigening (micromanagement) ter behoud van controle over de output. Door toepassing van theorie inzake de <strong class="text-accent">cirkel van invloed</strong> is dit structureel aangepast door actieve delegatie van taken aan groepsgenoten.</p>
                                <p class="mt-2">Gedurende de pre-master (Olthuis, 2025; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar3'); setTimeout(() => document.getElementById('jaar3-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage III</button>) resulteerde de verhoogde datacomplexiteit in de noodzaak om besluitvorming te versnellen. De toepassing van gestructureerde peer-feedback en functioneel overleg leidt tot aantoonbaar snellere besluitvaardigheid en efficiëntere teamsamenwerking.</p>
                            </div>
                        </div>
                    </div>
                </div>'''
content = re.sub(profzelf_new, profzelf_old, content, count=1, flags=re.DOTALL)

# 5. Revert Pers Zelf
perszelf_new = r'<!-- STORY CHAPTER: PERSOONLIJKE ZELF -->\s*<div class="reveal-on-scroll relative">.*?<div id="pers-zelf-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">.*?</div>\s*</div>\s*</div>\s*</div>'
perszelf_old = '''<!-- STORY CHAPTER: PERSOONLIJKE ZELF -->
                <div class="reveal-on-scroll space-y-4">
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">04</div>
                        <h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Persoonlijke Zelf</h2>
                    </div>
                    <div class="pl-12 border-l border-zinc-800/60 space-y-4">
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
                                <p>De arbeidsethos wordt empirisch bepaald door drie prestatie-indicatoren: de mate van kennisverwerving, de gerealiseerde output voor de opdrachtgever, en de toegewezen bevoegdheden. <strong>Flow</strong> treedt op wanneer taken een directe overlap vertonen met deze drie indicatoren.</p>
                                <p class="mt-2">Deze overlap is feitelijk vastgesteld tijdens de uitvoering van het afstudeeronderzoek bij Axelio (Olthuis, 2026b; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('afstuderen-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage V</button>). Hierbij wordt de bevoegdheid voor projectmanagement (eigenaarschap) toegepast voor het uitvoeren van kwantitatief en kwalitatief marktonderzoek.</p>
                            </div>
                        </div>
                    </div>
                </div>'''
content = re.sub(perszelf_new, perszelf_old, content, count=1, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

