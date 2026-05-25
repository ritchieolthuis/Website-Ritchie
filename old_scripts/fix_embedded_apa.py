import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace each iframe block with the iframe + the Bron text underneath.

# Jaar 1 - Waardecreatie
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1qKTB8Ahpum2alkXtpLowEHSODjh9OM9P/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>',
    '<iframe src="https://drive.google.com/file/d/1qKTB8Ahpum2alkXtpLowEHSODjh9OM9P/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>\n                                        <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. (2023). Waardecreatie Plan [PDF].</p>'
)

# Jaar 1 - Marketing Canvas / Pitch
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1VEw7VoXK8y2NgFWvxIao0CCdtkdQwB4R/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>',
    '<iframe src="https://drive.google.com/file/d/1VEw7VoXK8y2NgFWvxIao0CCdtkdQwB4R/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>\n                                        <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. (2023). Pitch & Presentatie [PDF].</p>'
)

# Jaar 2 - Salesplan Unica
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1es7Vk1lV_21IisBqw2iKkiHNbB0h9W1P/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>',
    '<iframe src="https://drive.google.com/file/d/1es7Vk1lV_21IisBqw2iKkiHNbB0h9W1P/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>\n                                        <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. e.a. (2024). Salesplan Unica Building Services [PDF].</p>'
)

# Jaar 2 - Pitch Workflow Harmony
content = content.replace(
    '<iframe src="https://docs.google.com/presentation/d/1eesuZoJtQzAdtX_vmaYCLW7OvogD6mgQ/preview?rm=minimal" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>',
    '<iframe src="https://docs.google.com/presentation/d/1eesuZoJtQzAdtX_vmaYCLW7OvogD6mgQ/preview?rm=minimal" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>\n                                        <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. e.a. (2024). Prototype Workflow Harmony Groep 4 [Presentatie].</p>'
)

# Jaar 3 - Adviesrapport
content = content.replace(
    '<iframe src="https://docs.google.com/document/d/1bXjcOyGofwbbC1poxEf88lLKYsifM_hz/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>',
    '<iframe src="https://docs.google.com/document/d/1bXjcOyGofwbbC1poxEf88lLKYsifM_hz/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>\n                                <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. (2025). Adviesrapport Business Analyse en Advies [PDF]. Universiteit Twente.</p>'
)

# Jaar 4 - Perron038 Container (we put the bron under the iframe container)
old_perron = '<!-- Frame 3 (Prototype) -->\n                                    <iframe id="iframe-perron-prototype" src="" class="hidden w-full h-[560px] border-0 bg-transparent relative z-10" onload="this.style.backgroundColor=\'white\'"></iframe>\n                                </div>'
new_perron = '<!-- Frame 3 (Prototype) -->\n                                    <iframe id="iframe-perron-prototype" src="" class="hidden w-full h-[560px] border-0 bg-transparent relative z-10" onload="this.style.backgroundColor=\'white\'"></iframe>\n                                </div>\n                                <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. e.a. (2026). Businesscase Perron038 & Factory NEXT Prototype [Webapplicatie].</p>'
content = content.replace(old_perron, new_perron)

# Jaar 4 - Whitepaper Vitens
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1zbaTOl800A24MG4o8scMMDTp5x3Ss1L0/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>',
    '<iframe src="https://drive.google.com/file/d/1zbaTOl800A24MG4o8scMMDTp5x3Ss1L0/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>\n                                        <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. e.a. (2026). Whitepaper Vitens Water as a Service [PDF].</p>'
)

# Jaar 4 - Whitepaper Vitens Mindset
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1EHu5kPJSsH389BJXJSdSb07LpDOhY7Jt/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>',
    '<iframe src="https://drive.google.com/file/d/1EHu5kPJSsH389BJXJSdSb07LpDOhY7Jt/preview" class="w-full h-[500px] rounded-xl border border-zinc-800 bg-white" loading="lazy"></iframe>\n                                        <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. e.a. (2026). Whitepaper Vitens Mindset [PDF].</p>'
)

# Afstuderen - Form 1 (assets/forms2.png)
old_form2 = '<img src="assets/forms2.png" alt="Expert Enquete Form" class="w-full h-auto object-cover max-h-[480px] opacity-80 group-hover:opacity-100 transition-opacity duration-300">\n                                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">'
new_form2 = '<img src="assets/forms2.png" alt="Expert Enquete Form" class="w-full h-auto object-cover max-h-[480px] opacity-80 group-hover:opacity-100 transition-opacity duration-300">\n                                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">'
old_form2_full = '</a>\n                            </div>'
new_form2_full = '</a>\n                            </div>\n                            <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. (2026). Expert Enquête United Kingdom [Online Formulier].</p>'
# Wait, let's just do a specific replace for the a-tag block.
content = content.replace(
    '<img src="assets/forms2.png" alt="Expert Enquete Form" class="w-full h-auto object-cover max-h-[480px] opacity-80 group-hover:opacity-100 transition-opacity duration-300">\n                                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">\n                                        <div class="w-16 h-16 bg-accent/90 rounded-full flex items-center justify-center shadow-lg text-black transform group-hover:scale-110 transition-transform duration-300">\n                                            <i data-lucide="external-link" class="w-6 h-6"></i>\n                                        </div>\n                                    </div>\n                                </a>\n                            </div>',
    '<img src="assets/forms2.png" alt="Expert Enquete Form" class="w-full h-auto object-cover max-h-[480px] opacity-80 group-hover:opacity-100 transition-opacity duration-300">\n                                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">\n                                        <div class="w-16 h-16 bg-accent/90 rounded-full flex items-center justify-center shadow-lg text-black transform group-hover:scale-110 transition-transform duration-300">\n                                            <i data-lucide="external-link" class="w-6 h-6"></i>\n                                        </div>\n                                    </div>\n                                </a>\n                            </div>\n                            <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. (2026). Expert Enquête United Kingdom [Online Formulier].</p>'
)

# Afstuderen - Form 2 (assets/forms1.png)
content = content.replace(
    '<img src="assets/forms1.png" alt="Marktvalidatie Form" class="w-full h-auto object-cover max-h-[480px] opacity-80 group-hover:opacity-100 transition-opacity duration-300">\n                                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">\n                                        <div class="w-16 h-16 bg-accent/90 rounded-full flex items-center justify-center shadow-lg text-black transform group-hover:scale-110 transition-transform duration-300">\n                                            <i data-lucide="external-link" class="w-6 h-6"></i>\n                                        </div>\n                                    </div>\n                                </a>\n                            </div>',
    '<img src="assets/forms1.png" alt="Marktvalidatie Form" class="w-full h-auto object-cover max-h-[480px] opacity-80 group-hover:opacity-100 transition-opacity duration-300">\n                                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">\n                                        <div class="w-16 h-16 bg-accent/90 rounded-full flex items-center justify-center shadow-lg text-black transform group-hover:scale-110 transition-transform duration-300">\n                                            <i data-lucide="external-link" class="w-6 h-6"></i>\n                                        </div>\n                                    </div>\n                                </a>\n                            </div>\n                            <p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: Olthuis, R. (2026). Diepte-interviews & Marktvalidatie Agrio [Online Formulier].</p>'
)


# 3. Add to Bronnenlijst
extra_bronnen = """
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2023). <span class="italic">Waardecreatie Plan</span> [PDF]. Ongepubliceerd, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2023). <span class="italic">Pitch & Presentatie</span> [PDF]. Ongepubliceerd, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. e.a. (2024). <span class="italic">Salesplan Unica Building Services</span> [PDF]. Ongepubliceerd, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. e.a. (2024). <span class="italic">Prototype Workflow Harmony Groep 4</span> [Presentatie]. Ongepubliceerd, Windesheim.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2025). <span class="italic">Adviesrapport Business Analyse en Advies</span> [PDF]. Ongepubliceerd, Universiteit Twente.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. e.a. (2026). <span class="italic">Businesscase Perron038 & Factory NEXT Prototype</span> [Webapplicatie].
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Water as a Service</span> [PDF]. Ongepubliceerd.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Mindset</span> [PDF]. Ongepubliceerd.
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2026). <span class="italic">Expert Enquête United Kingdom</span> [Online Formulier].
                            </li>
                            <li class="pl-4 -indent-4">
                                Olthuis, R. (2026). <span class="italic">Diepte-interviews & Marktvalidatie Agrio</span> [Online Formulier].
                            </li>
"""

# Insert right after the last Olthuis reference in Bronnenlijst
content = content.replace(
    'Olthuis, R. (2026b). <span class="italic">Afstudeerportfolio: Axelio / Agrio UK Market Entry</span> [Bijlage V]. Ongepubliceerd portfolio, Windesheim.</li>',
    'Olthuis, R. (2026b). <span class="italic">Afstudeerportfolio: Axelio / Agrio UK Market Entry</span> [Bijlage V]. Ongepubliceerd portfolio, Windesheim.</li>' + extra_bronnen
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

