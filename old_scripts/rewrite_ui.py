import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Modify the About section on the homepage
about_old = r'<p class="text-zinc-400 leading-relaxed group-hover:text-zinc-300 transition-colors duration-300 font-sans" data-i18n="about_text">\s*Vierdejaarsstudent Commerciële Economie \(Hogeschool Windesheim\) met afgeronde minors in Bedrijfskunde \(Pre-master Universiteit Twente\) en Financiële Besluitvorming\. Het profiel richt zich op kwantitatieve en kwalitatieve analyse, iteratief projectmanagement en datagedreven besluitvorming ter ondersteuning van bedrijfskundige vraagstukken\.<br><br>De beroepspraktijk bestaat uit het analyseren van procesknelpunten en het implementeren van meetbare procesverbeteringen\. De nadruk ligt op de toepassing van academische theorie in de commerciële praktijk om efficiëntie en bedrijfsresultaten te optimaliseren\.\s*</p>'

about_new = '''<div class="text-zinc-400 leading-relaxed font-sans">
                        <p class="mb-4 text-sm md:text-base">Vierdejaarsstudent Commerciële Economie (Hogeschool Windesheim) met afgeronde minors in Bedrijfskunde en Financiële Besluitvorming.</p>
                        
                        <div id="about-more" class="hidden opacity-0 transition-opacity duration-500 text-sm md:text-base">
                           <p>Het profiel richt zich op kwantitatieve en kwalitatieve analyse, iteratief projectmanagement en datagedreven besluitvorming ter ondersteuning van bedrijfskundige vraagstukken.<br><br>De beroepspraktijk bestaat uit het analyseren van procesknelpunten en het implementeren van meetbare procesverbeteringen. De nadruk ligt op de toepassing van academische theorie in de commerciële praktijk om efficiëntie en bedrijfsresultaten te optimaliseren.</p>
                        </div>
                        
                        <button onclick="
                            const more = document.getElementById('about-more');
                            const btn = this;
                            if (more.classList.contains('hidden')) {
                                more.classList.remove('hidden');
                                setTimeout(() => more.classList.remove('opacity-0'), 10);
                                btn.innerHTML = 'Verberg details <i data-lucide=\\\'chevron-up\\\' class=\\\'w-4 h-4\\\'></i>';
                            } else {
                                more.classList.add('opacity-0');
                                setTimeout(() => more.classList.add('hidden'), 500);
                                btn.innerHTML = 'Lees Volledig Profiel <i data-lucide=\\\'chevron-down\\\' class=\\\'w-4 h-4\\\'></i>';
                            }
                            lucide.createIcons();
                        " class="mt-4 flex items-center gap-2 text-accent text-sm font-bold hover:underline transition-all">
                            Lees Volledig Profiel <i data-lucide="chevron-down" class="w-4 h-4"></i>
                        </button>
                    </div>'''

content, count = re.subn(about_old, about_new, content, count=1, flags=re.DOTALL)
print("About section:", count)


# 2. Modify PDB Inst Frame
inst_old = r'<!-- STORY CHAPTER: INSTITUTIONEEL FRAME -->\s*<div class="reveal-on-scroll space-y-4">\s*<div class="flex items-center gap-4">\s*<div class="w-8 h-8 rounded-full bg-accent text-black flex items-center justify-center font-bold text-xs">01</div>\s*<h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Institutioneel Frame</h2>\s*</div>\s*<div class="pl-12 border-l border-zinc-800/60 space-y-4">\s*<p class="text-zinc-400 text-sm md:text-base md:text-\[17px\] leading-\[1.8\] font-light tracking-wide">\s*De vooropleiding bestaat uit een afgeronde mbo-opleiding.*?Iteratief werken \(Design Thinking\)\.\s*</p>\s*<div class="text-xs p-4 bg-zinc-900/50 rounded-lg text-zinc-300 font-medium border border-zinc-800">\s*"De vereiste ontwikkeling.*?"\s*</div>\s*</div>\s*</div>'

inst_new = '''<!-- STORY CHAPTER: INSTITUTIONEEL FRAME -->
                <div class="reveal-on-scroll relative">
                    <div class="absolute left-[15px] top-[40px] bottom-[-40px] w-px bg-zinc-800"></div>
                    <div class="flex items-center gap-4 mb-4 relative z-10">
                        <div class="w-8 h-8 rounded-full bg-accent text-black flex items-center justify-center font-bold text-xs flex-shrink-0">01</div>
                        <div>
                            <h2 class="text-xl font-display font-bold uppercase text-white">Institutioneel Frame</h2>
                            <p class="text-zinc-400 text-sm">Focus op de transitie van operationeel naar strategisch denkniveau.</p>
                        </div>
                    </div>
                    <div class="pl-12 space-y-4 relative z-10 pb-8">
                        <button onclick="
                            const content = document.getElementById('inst-frame-content');
                            if (content.classList.contains('hidden')) {
                                content.classList.remove('hidden');
                                setTimeout(() => content.classList.remove('opacity-0', 'translate-y-2'), 10);
                                this.innerHTML = '<i data-lucide=\\\'minus-circle\\\' class=\\\'w-4 h-4\\\'></i> Verberg academische verantwoording';
                            } else {
                                content.classList.add('opacity-0', 'translate-y-2');
                                setTimeout(() => content.classList.add('hidden'), 500);
                                this.innerHTML = '<i data-lucide=\\\'plus-circle\\\' class=\\\'w-4 h-4\\\'></i> Klik hier voor academische verantwoording';
                            }
                            lucide.createIcons();
                        " class="flex items-center gap-2 text-accent text-xs font-bold uppercase tracking-wider hover:text-white transition-colors py-2">
                            <i data-lucide="plus-circle" class="w-4 h-4"></i> Klik hier voor academische verantwoording
                        </button>
                        
                        <div id="inst-frame-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">
                            <p class="text-zinc-400 text-sm md:text-[15px] leading-relaxed">
                                De vooropleiding bestaat uit een afgeronde mbo-opleiding, gevolgd door de hbo-bachelor Commerciële Economie (Olthuis, 2023; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar1'); setTimeout(() => document.getElementById('jaar1-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>). De meting van vaardigheden geschiedt volgens de beoordelingscriteria uit de CE Skills Guide (Windesheim, 2026; zie <a href="https://docs.google.com/spreadsheets/d/1XqhvW2usQ9FYD7Tye1TzObGUiBtvB9cJrIJR7dbGhWg/edit?usp=drive_link" target="_blank" class="text-accent hover:underline font-bold inline-block mx-1">Bijlage VI</a>). De competentieontwikkeling concentreert zich op de meetbare criteria: Initiatief, Samenwerken, Verantwoordelijkheid (Eigenaarschap), Analytisch denken, Besluitvaardigheid en Iteratief werken (Design Thinking).
                            </p>
                            <div class="text-xs p-4 bg-zinc-900/50 rounded-lg text-zinc-300 font-medium border border-zinc-800">
                                "De vereiste ontwikkeling binnen het institutionele frame bestaat uit de verschuiving van operationele taken (mbo-niveau) naar strategische analyse en advisering (hbo-niveau)."
                            </div>
                        </div>
                    </div>
                </div>'''

content, count = re.subn(inst_old, inst_new, content, count=1, flags=re.DOTALL)
print("Inst Frame:", count)

# 3. Modify PDB Prof Frame
prof_old = r'<!-- STORY CHAPTER: PROFESSIONEEL FRAME -->\s*<div class="reveal-on-scroll space-y-4">\s*<div class="flex items-center gap-4">\s*<div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">02</div>\s*<h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Professioneel Frame</h2>\s*</div>\s*<div class="pl-12 border-l border-zinc-800/60 space-y-4">\s*<p class="text-zinc-400 text-sm md:text-base md:text-\[17px\] leading-\[1.8\] font-light tracking-wide">\s*Binnen de beroepspraktijk zijn adviesrapporten en beroepsproducten.*?iteratief op te leveren\.\s*</p>\s*<div class="text-zinc-300 text-sm p-4 bg-zinc-900/50 rounded-lg border border-zinc-800 font-medium mt-4">\s*<strong>Kritisch inzicht:</strong> Het minimaliseren van de ontwikkeltijd.*?\s*</div>\s*</div>\s*</div>'

prof_new = '''<!-- STORY CHAPTER: PROFESSIONEEL FRAME -->
                <div class="reveal-on-scroll relative">
                    <div class="absolute left-[15px] top-[40px] bottom-[-40px] w-px bg-zinc-800"></div>
                    <div class="flex items-center gap-4 mb-4 relative z-10">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs flex-shrink-0">02</div>
                        <div>
                            <h2 class="text-xl font-display font-bold uppercase text-white">Professioneel Frame</h2>
                            <p class="text-zinc-400 text-sm">Focus op Design Thinking en snellere feedbackloops.</p>
                        </div>
                    </div>
                    <div class="pl-12 space-y-4 relative z-10 pb-8">
                        <button onclick="
                            const content = document.getElementById('prof-frame-content');
                            if (content.classList.contains('hidden')) {
                                content.classList.remove('hidden');
                                setTimeout(() => content.classList.remove('opacity-0', 'translate-y-2'), 10);
                                this.innerHTML = '<i data-lucide=\\\'minus-circle\\\' class=\\\'w-4 h-4\\\'></i> Verberg academische verantwoording';
                            } else {
                                content.classList.add('opacity-0', 'translate-y-2');
                                setTimeout(() => content.classList.add('hidden'), 500);
                                this.innerHTML = '<i data-lucide=\\\'plus-circle\\\' class=\\\'w-4 h-4\\\'></i> Klik hier voor academische verantwoording';
                            }
                            lucide.createIcons();
                        " class="flex items-center gap-2 text-accent text-xs font-bold uppercase tracking-wider hover:text-white transition-colors py-2">
                            <i data-lucide="plus-circle" class="w-4 h-4"></i> Klik hier voor academische verantwoording
                        </button>
                        
                        <div id="prof-frame-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">
                            <p class="text-zinc-400 text-sm md:text-[15px] leading-relaxed">
                                Binnen de beroepspraktijk zijn adviesrapporten en beroepsproducten opgeleverd voor opdrachtgevers waaronder <strong class="text-white">Unica</strong> (Olthuis, 2024; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar2'); setTimeout(() => document.getElementById('jaar2-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage II</button>) en <strong class="text-white">Vitens / Perron038</strong> (Olthuis, 2026a; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar4'); setTimeout(() => document.getElementById('jaar4-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage IV</button>). Uit de projectevaluaties blijkt dat lange theorie- en analysefasen leiden tot vertraging in de doorlooptijd. Derhalve is de methodiek <em>Design Thinking</em> (Brown, 2009) geïmplementeerd om projecten middels kortcyclische testen en frequente validatie iteratief op te leveren.
                            </p>
                            <div class="text-zinc-300 text-sm p-4 bg-zinc-900/50 rounded-lg border border-zinc-800 font-medium mt-4">
                                <strong>Kritisch inzicht:</strong> Het minimaliseren van de ontwikkeltijd per projectfase leidt tot snellere feedbackloops en een hogere implementatiegraad bij de opdrachtgever.
                            </div>
                        </div>
                    </div>
                </div>'''

content, count = re.subn(prof_old, prof_new, content, count=1, flags=re.DOTALL)
print("Prof Frame:", count)

# 4. Modify PDB Prof Zelf
profzelf_old = r'<!-- STORY CHAPTER: PROFESSIONELE ZELF -->\s*<div class="reveal-on-scroll space-y-4">\s*<div class="flex items-center gap-4">\s*<div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">03</div>\s*<h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Professionele Zelf</h2>\s*</div>\s*<div class="pl-12 border-l border-zinc-800/60 space-y-4">.*?</div>\s*</div>\s*</div>'

profzelf_new = '''<!-- STORY CHAPTER: PROFESSIONELE ZELF -->
                <div class="reveal-on-scroll relative">
                    <div class="absolute left-[15px] top-[40px] bottom-[-40px] w-px bg-zinc-800"></div>
                    <div class="flex items-center gap-4 mb-4 relative z-10">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs flex-shrink-0">03</div>
                        <div>
                            <h2 class="text-xl font-display font-bold uppercase text-white">Professionele Zelf</h2>
                            <p class="text-zinc-400 text-sm">Focus op delegatie, besluitvaardigheid en teamsamenwerking.</p>
                        </div>
                    </div>
                    <div class="pl-12 space-y-4 relative z-10 pb-8">
                        <button onclick="
                            const content = document.getElementById('prof-zelf-content');
                            if (content.classList.contains('hidden')) {
                                content.classList.remove('hidden');
                                setTimeout(() => content.classList.remove('opacity-0', 'translate-y-2'), 10);
                                this.innerHTML = '<i data-lucide=\\\'minus-circle\\\' class=\\\'w-4 h-4\\\'></i> Verberg academische verantwoording';
                            } else {
                                content.classList.add('opacity-0', 'translate-y-2');
                                setTimeout(() => content.classList.add('hidden'), 500);
                                this.innerHTML = '<i data-lucide=\\\'plus-circle\\\' class=\\\'w-4 h-4\\\'></i> Klik hier voor academische verantwoording';
                            }
                            lucide.createIcons();
                        " class="flex items-center gap-2 text-accent text-xs font-bold uppercase tracking-wider hover:text-white transition-colors py-2">
                            <i data-lucide="plus-circle" class="w-4 h-4"></i> Klik hier voor academische verantwoording
                        </button>
                        
                        <div id="prof-zelf-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">
                            <!-- Interactief Model: Covey -->
                            <div class="bg-zinc-900/40 border border-zinc-800 rounded-xl p-5 group">
                                <div class="flex items-center gap-4 mb-4">
                                    <div class="relative w-12 h-12 flex items-center justify-center">
                                        <div class="absolute inset-0 border border-zinc-600 rounded-full"></div>
                                        <div class="absolute inset-2 border-2 border-accent rounded-full covey-circle"></div>
                                    </div>
                                    <div>
                                        <h4 class="text-white font-bold font-display text-sm">Cirkel van Invloed (Covey, 1989)</h4>
                                    </div>
                                </div>
                                <div class="covey-details pt-4 border-t border-zinc-800 text-zinc-400 text-sm md:text-[15px] leading-relaxed">
                                    <p>Uit feedbackverslagen blijkt initieel een sterke neiging tot taaktoe-eigening (micromanagement) ter behoud van controle over de output. Door toepassing van theorie inzake de <strong class="text-accent">cirkel van invloed</strong> is dit structureel aangepast door actieve delegatie van taken aan groepsgenoten.</p>
                                    <p class="mt-2">Gedurende de pre-master (Olthuis, 2025; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('jaar3'); setTimeout(() => document.getElementById('jaar3-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage III</button>) resulteerde de verhoogde datacomplexiteit in de noodzaak om besluitvorming te versnellen. De toepassing van gestructureerde peer-feedback en functioneel overleg leidt tot aantoonbaar snellere besluitvaardigheid en efficiëntere teamsamenwerking.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

content, count = re.subn(profzelf_old, profzelf_new, content, count=1, flags=re.DOTALL)
print("Prof Zelf:", count)


# 5. Modify PDB Pers Zelf
perszelf_old = r'<!-- STORY CHAPTER: PERSOONLIJKE ZELF -->\s*<div class="reveal-on-scroll space-y-4">\s*<div class="flex items-center gap-4">\s*<div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs">04</div>\s*<h2 class="text-xl md:text-2xl font-display font-bold uppercase text-white">Persoonlijke Zelf</h2>\s*</div>\s*<div class="pl-12 border-l border-zinc-800/60 space-y-4">.*?</div>\s*</div>\s*</div>'

perszelf_new = '''<!-- STORY CHAPTER: PERSOONLIJKE ZELF -->
                <div class="reveal-on-scroll relative">
                    <div class="absolute left-[15px] top-[40px] bottom-[-40px] w-px bg-zinc-800"></div>
                    <div class="flex items-center gap-4 mb-4 relative z-10">
                        <div class="w-8 h-8 rounded-full bg-zinc-800 text-white flex items-center justify-center font-bold text-xs flex-shrink-0">04</div>
                        <div>
                            <h2 class="text-xl font-display font-bold uppercase text-white">Persoonlijke Zelf</h2>
                            <p class="text-zinc-400 text-sm">Focus op arbeidsethos, prestatie-indicatoren en flow.</p>
                        </div>
                    </div>
                    <div class="pl-12 space-y-4 relative z-10 pb-8">
                        <button onclick="
                            const content = document.getElementById('pers-zelf-content');
                            if (content.classList.contains('hidden')) {
                                content.classList.remove('hidden');
                                setTimeout(() => content.classList.remove('opacity-0', 'translate-y-2'), 10);
                                this.innerHTML = '<i data-lucide=\\\'minus-circle\\\' class=\\\'w-4 h-4\\\'></i> Verberg academische verantwoording';
                            } else {
                                content.classList.add('opacity-0', 'translate-y-2');
                                setTimeout(() => content.classList.add('hidden'), 500);
                                this.innerHTML = '<i data-lucide=\\\'plus-circle\\\' class=\\\'w-4 h-4\\\'></i> Klik hier voor academische verantwoording';
                            }
                            lucide.createIcons();
                        " class="flex items-center gap-2 text-accent text-xs font-bold uppercase tracking-wider hover:text-white transition-colors py-2">
                            <i data-lucide="plus-circle" class="w-4 h-4"></i> Klik hier voor academische verantwoording
                        </button>
                        
                        <div id="pers-zelf-content" class="hidden opacity-0 translate-y-2 transition-all duration-500 space-y-4">
                            <!-- Interactief Model: Ruijters -->
                            <div class="bg-zinc-900/40 border border-zinc-800 rounded-xl p-5 group">
                                <div class="flex items-center gap-4 mb-4">
                                    <div class="w-12 h-12 flex flex-col items-center justify-center border-l-2 border-r-2 border-accent/30 gap-1 overflow-hidden">
                                        <div class="w-full h-1 bg-accent/20 rounded">
                                            <div class="h-full bg-accent rounded w-full"></div>
                                        </div>
                                        <div class="w-full h-1 bg-accent/20 rounded">
                                            <div class="h-full bg-accent rounded w-full"></div>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="text-white font-bold font-display text-sm">Mijn Binnenste Buiten (Ruijters, 2015)</h4>
                                    </div>
                                </div>
                                <div class="ruijters-details pt-4 border-t border-zinc-800 text-zinc-400 text-sm md:text-[15px] leading-relaxed">
                                    <p>De arbeidsethos wordt empirisch bepaald door drie prestatie-indicatoren: de mate van kennisverwerving, de gerealiseerde output voor de opdrachtgever, en de toegewezen bevoegdheden. <strong>Flow</strong> treedt op wanneer taken een directe overlap vertonen met deze drie indicatoren.</p>
                                    <p class="mt-2">Deze overlap is feitelijk vastgesteld tijdens de uitvoering van het afstudeeronderzoek bij Axelio (Olthuis, 2026b; zie <button onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('afstuderen-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage V</button>). Hierbij wordt de bevoegdheid voor projectmanagement (eigenaarschap) toegepast voor het uitvoeren van kwantitatief en kwalitatief marktonderzoek.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''

content, count = re.subn(perszelf_old, perszelf_new, content, count=1, flags=re.DOTALL)
print("Pers Zelf:", count)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
