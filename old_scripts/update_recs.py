import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update CSS for bento-card to be cleaner
content = re.sub(
    r'\.bento-card \{\n\s*background: #[0-9a-fA-F]+;\n\s*border: 1px solid #[0-9a-fA-F]+;\n\s*border-radius: 1.5rem;\n\s*position: relative;\n\s*overflow: hidden;\n\s*\}',
    '.bento-card {\\n        background: rgba(24, 24, 27, 0.4);\\n        border: 1px solid rgba(39, 39, 42, 0.4);\\n        border-radius: 1.5rem;\\n        position: relative;\\n        overflow: hidden;\\n      }',
    content
)

# 2. Extract and replace recommendations layout
recs_pattern = re.compile(r'<!-- Recommendations Carousel -->.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)

new_recs_html = """<!-- Recommendations Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 w-full mt-8">
                
                <!-- Rec 1 -->
                <a href="https://www.linkedin.com/in/joelrepko/?locale=nl" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0">
                            <img src="https://media.licdn.com/dms/image/v2/C5603AQEtbc-9HmikSg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1517727248745?e=1781136000&v=beta&t=wfQJYIQv-aVK9sNJRFSazCT5-EvWoFeDW_TAHR5J2NU" alt="Joël Repko" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all">
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm flex items-center gap-1 group-hover:text-accent transition-colors">Joël Repko <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs" data-i18n="rec_joel_role">Lecturer Commercial Economics, Windesheim</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                         <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                            <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_joel_text">
                                "During the classes and workshops I taught him in the Commercial Economics program at Windesheim University of Applied Sciences, Ritchie was an involved student who continues to think critically and asks the right questions to get the most out of his projects for his clients in the field."
                            </p>
                         </div>
                    </div>
                </a>

                <!-- Rec 2 -->
                <a href="https://www.linkedin.com/in/markversluis/" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0">
                            <img src="https://media.licdn.com/dms/image/v2/C4D03AQG6GbwvEe8Edw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1568294449762?e=1781136000&v=beta&t=FszmarvdnLJWJXoKpTDY5MCiPt5-Abl2bM3vr_5wBVU" alt="Mark Versluis" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all">
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm flex items-center gap-1 group-hover:text-accent transition-colors">Mark Versluis <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs" data-i18n="rec_mark_role">Senior Marketer KNGF / Lecturer Marketing Windesheim</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                         <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                            <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_mark_text">
                                "As Ritchie's teacher, I got to know him as an independent and result-oriented student who fits well in the group. As a young professional, he will be an asset to many companies."
                            </p>
                         </div>
                    </div>
                </a>

                <!-- Rec 3 -->
                <a href="https://www.linkedin.com/in/antoinettealma/" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0">
                            <img src="https://media.licdn.com/dms/image/v2/D4E03AQEakbDrMEcHpQ/profile-displayphoto-crop_800_800/B4EZ4_soOqKYAI-/0/1779185129622?e=1781136000&v=beta&t=3Hh5VPmtMKUpVy_LsUSxKi5QDlSkes7SsaN6kHAwV5A" alt="Antoinette Alma" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all">
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm group-hover:text-accent transition-colors flex items-center gap-1"><span data-i18n="rec_3_name">Antoinette Alma</span> <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs" data-i18n="rec_3_role">Speaker, Trainer & Lecturer</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                        <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                             <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_3_text">
                                "I know Ritchie as a smart and inquisitive student. He asks sharp questions that stimulate further thinking in others. He actively seeks depth and quickly bridges the gap between theory and practice."
                            </p>
                        </div>
                    </div>
                </a>
                
                <!-- Rec 4 -->
                <a href="https://www.linkedin.com/in/elmar-van-brakel-33362710/" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0">
                            <img src="https://media.licdn.com/dms/image/v2/C4D03AQFEDuVRvqzM_w/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1547551348628?e=1781136000&v=beta&t=xfr5Hl5TjEvWLd6aJQLhOZBraayWzr80bxf3OqlmkAA" alt="Elmar van Brakel" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all">
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm group-hover:text-accent transition-colors flex items-center gap-1"><span data-i18n="rec_4_name">Elmar van Brakel</span> <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs line-clamp-2" data-i18n="rec_4_role">Trainer I docent I coach I sales I customer experience</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                        <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                             <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_4_text">
                                "I have had Ritchie in training several times over the past few years during the CE program at Windesheim Zwolle... Knows his responsibilities, seeks depth in his assignments, shows ownership and works well with other students."
                            </p>
                        </div>
                    </div>
                </a>
                
                <!-- Rec 5 -->
                 <a href="https://www.linkedin.com/in/marcellogtenberg/" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0">
                            <img src="https://media.licdn.com/dms/image/v2/C4D03AQHYhRKwL0qDOA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1632229718870?e=1781136000&v=beta&t=aCpIEID7ZgTiWwN3nzyAAMup8opnKlGKBtWsOaDF82g" alt="Marcel Logtenberg" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all">
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm group-hover:text-accent transition-colors flex items-center gap-1"><span data-i18n="rec_5_name">Marcel Logtenberg</span> <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs" data-i18n="rec_5_role">Analist • Coach • Projectmanager</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                        <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                             <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_5_text">
                                "I experienced Ritchie as a committed student who actively contributes to lectures. He asked good questions and took the initiative in conducting a good dialogue."
                            </p>
                        </div>
                    </div>
                </a>
                
                <!-- Rec 6 -->
                <a href="https://www.linkedin.com/in/bas-de-leve-4a625615/" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0">
                            <img src="https://media.licdn.com/dms/image/v2/D4E03AQGUgwKS0vpQ_Q/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1689663050281?e=1781136000&v=beta&t=JSuPidRYP5h_fQDtrcOXV_pqlXP3zH7hDSIAaKA4xwk" alt="Bas de Leve" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all">
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm group-hover:text-accent transition-colors flex items-center gap-1"><span data-i18n="rec_6_name">Bas de Leve</span> <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs" data-i18n="rec_6_role">English Language Instructor and Trainer</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                        <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                             <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_6_text">
                                "An ambitious, intelligent, and motivated student, Ritchie, is always eager to investigate possibilities. He is also introspective, and very friendly. In short, an asset for every organisation."
                            </p>
                        </div>
                    </div>
                </a>
                
                <!-- Rec 7 -->
                <a href="https://www.linkedin.com/in/martijnoldeweghuis/?locale=nl" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0 flex items-center justify-center text-zinc-500">
                            <i data-lucide="user" class="w-6 h-6"></i>
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm group-hover:text-accent transition-colors flex items-center gap-1"><span data-i18n="rec_7_name">Martijn Olde Weghuis</span> <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs" data-i18n="rec_7_role">Directeur bij Axelio | Agrio Software</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                        <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                             <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_7_text">
                                "Jullie hebben er samen een mooi onderzoek van gemaakt en zijn uiteindelijk met een goed advies gekomen. Ook mooie nieuwe inzichten gekregen die wij zelf nog niet hadden."
                            </p>
                        </div>
                    </div>
                </a>
                
                <!-- Rec 8 -->
                <a href="https://www.linkedin.com/in/eric-vredeveldt-a7b4b815/" target="_blank" class="bento-card p-6 flex flex-col gap-4 group h-full hover:border-zinc-600 transition-colors data-hover-trigger">
                    <div class="spotlight-overlay"></div>
                    <div class="flex items-center gap-3">
                         <div class="w-12 h-12 rounded-full bg-zinc-800 border border-zinc-700 overflow-hidden flex-shrink-0">
                            <img src="/assets/eric_vredeveldt.jpg" alt="Eric Vredeveldt" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all">
                         </div>
                         <div>
                             <h4 class="text-white font-bold text-sm group-hover:text-accent transition-colors flex items-center gap-1"><span data-i18n="rec_8_name">Eric Vredeveldt</span> <i data-lucide="external-link" class="w-3 h-3 text-zinc-600"></i></h4>
                             <p class="text-zinc-500 text-xs" data-i18n="rec_8_role">Business Development Manager bij Vitens</p>
                         </div>
                    </div>
                    <div class="relative flex-grow">
                         <i data-lucide="quote" class="absolute -top-1 -left-1 w-4 h-4 text-zinc-700 fill-zinc-700 opacity-30 transform -scale-x-100"></i>
                        <div class="h-[180px] overflow-y-auto custom-scrollbar pr-2">
                             <p class="text-zinc-400 text-sm leading-relaxed pl-4 italic" data-i18n="rec_8_text">
                                "Ritchie is een positieve en doordachte student die graag eerst goed inzicht krijgt voordat hij tot resultaat komt. Op de werkvloer zet hij die houding effectief in, waardoor hij een waardevolle aanvulling is op ieder team."
                            </p>
                        </div>
                    </div>
                </a>

            </div>"""

content = re.sub(recs_pattern, new_recs_html, content)

# 3. Remove tilt functionality to make it less busy
content = content.replace("VanillaTilt.init(document.querySelectorAll('[data-tilt]'), {", "/* VanillaTilt.init(document.querySelectorAll('[data-tilt]'), {")
content = content.replace("glare: true,", "glare: true, */")

with open('index.html', 'w') as f:
    f.write(content)
