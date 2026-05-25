import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Jaar 4 Replacement: We'll replace the two big project divs with a timeline
jaar4_old = """                        <div class="p-6 md:p-8 rounded-2xl bg-zinc-900/50 border border-zinc-800 space-y-4 my-6">
                            <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-4">
                                <div>
                                    <div class="text-xs font-mono text-white uppercase">Project 1</div>
                                    <h3 class="text-xl font-bold text-white mt-1">Perron038 | Factory NEXT Positionering</h3>
                                </div>
                                <div class="flex flex-col gap-2 flex-shrink-0">
                                    <a href="https://businesscaseperron038.hugo-fransen03.workers.dev/" target="_blank" class="px-4 py-2 bg-zinc-800 hover:bg-accent hover:text-black transition-colors rounded-full text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer data-hover-trigger">
                                        <i data-lucide="external-link" class="w-3.5 h-3.5"></i> Live Website
                                    </a>
                                    <a href="https://businesscaseperron038mindset.hugo-fransen03.workers.dev/" target="_blank" class="px-4 py-2 bg-zinc-800 hover:bg-accent hover:text-black transition-colors rounded-full text-xs font-bold flex items-center justify-center gap-1.5 cursor-pointer data-hover-trigger">
                                        <i data-lucide="external-link" class="w-3.5 h-3.5"></i> Live Mindset Website
                                    </a>
                                </div>
                            </div>
                            
                            <p class="text-zinc-400 text-sm leading-relaxed">
                                Voor Perron038 lag de focus op de positionering van Factory NEXT als innovatiehub binnen de maakindustrie. Binnen het project werden klantgedrag, marketingactiviteiten, leadopvolging en interne processen onderzocht. Uit interviews en analyses bleek dat organisaties vooral behoefte hadden aan concrete toepasbaarheid, snelheid en directe meerwaarde.
                            </p>
                            <p class="text-zinc-400 text-sm leading-relaxed">
                                Op basis van deze inzichten werden strategische aanbevelingen ontwikkeld rondom positionering, messaging en commerciële opvolging. Daarbij werd onder andere geadviseerd om gebruik te maken van Google Tag Manager, Google Analytics en een CRM-systeem om leadopvolging professioneler en beter meetbaar in te richten.
                            </p>

                            <div class="bg-black/30 p-4 rounded-xl border border-zinc-850">
                                <h5 class="text-xs font-mono text-white uppercase mb-2">Binnen het project werd gewerkt aan:</h5>
                                <ul class="space-y-1.5 text-zinc-400 text-xs">
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Positioneringsanalyse van Factory NEXT</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Onderzoek naar klantgedrag en stakeholderbehoeften</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Analyse van marketingactiviteiten en leadopvolging</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Strategische aanbevelingen voor commerciële optimalisatie</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Inrichting van meetbare marketing- en salesprocessen</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Advies rondom CRM-implementatie en data-analyse</li>
                                </ul>
                            </div>"""

jaar4_new = """                        <div class="relative pl-8 border-l border-zinc-800 ml-2 my-8">
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold">Project 1: Perron038 | Factory NEXT</h4>
                                <div class="flex gap-2 mb-4">
                                    <a href="https://businesscaseperron038.hugo-fransen03.workers.dev/" target="_blank" class="px-3 py-1 bg-zinc-800 hover:bg-accent hover:text-black transition-colors rounded-full text-[10px] font-bold flex items-center gap-1 cursor-pointer data-hover-trigger"><i data-lucide="external-link" class="w-3 h-3"></i> Live Website</a>
                                    <a href="https://businesscaseperron038mindset.hugo-fransen03.workers.dev/" target="_blank" class="px-3 py-1 bg-zinc-800 hover:bg-accent hover:text-black transition-colors rounded-full text-[10px] font-bold flex items-center gap-1 cursor-pointer data-hover-trigger"><i data-lucide="external-link" class="w-3 h-3"></i> Mindset Website</a>
                                </div>
                                <p class="text-zinc-300 text-base leading-relaxed mb-4">
                                    Onderzoek naar klantgedrag en interne processen voor de positionering van innovatiehub Factory NEXT. Strategische aanbevelingen ontwikkeld voor positionering, messaging, en het meetbaar inrichten van leadopvolging (GTM, GA4, CRM).
                                </p>
                            </div>"""
content = content.replace(jaar4_old, jaar4_new)

jaar4_vitens_old = """                        <!-- Project 2: Vitens -->
                        <div class="p-6 md:p-8 rounded-2xl bg-zinc-900/50 border border-zinc-800 space-y-4 my-6">
                            <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-4">
                                <div>
                                    <div class="text-xs font-mono text-white uppercase">Project 2</div>
                                    <h3 class="text-xl font-bold text-white mt-1">Vitens | Water as a Service Positionering</h3>
                                </div>
                                <div class="flex flex-col gap-2 flex-shrink-0">
                                </div>
                            </div>
                            
                            <p class="text-zinc-400 text-sm leading-relaxed">
                                Voor Vitens richtte het project zich op de ontwikkeling van een commerciëlere positionering binnen de grootzakelijke markt. Hierbij stond de transitie richting een Water as a Service-propositie centraal.
                            </p>
                            <p class="text-zinc-400 text-sm leading-relaxed">
                                Door middel van marktonderzoek, stakeholderanalyses en interviews werden klantbehoeften, concurrentie en positioneringsmogelijkheden onderzocht. Uiteindelijk werd een strategische richting ontwikkeld waarbij Vitens een aparte commerciële entiteit kon positioneren met behoud van het vertrouwen van het moedermerk.
                            </p>

                            <div class="bg-black/30 p-4 rounded-xl border border-zinc-850">
                                <h5 class="text-xs font-mono text-white uppercase mb-2">Binnen het project werd gewerkt aan:</h5>
                                <ul class="space-y-1.5 text-zinc-400 text-xs">
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Marktanalyse binnen de grootzakelijke watermarkt</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Stakeholder- en concurrentieanalyse</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Positioneringsvraagstukken rondom Water as a Service</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Strategische scenario’s voor commerciële marktbenadering</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Ontwikkeling van commerciële proposities</li>
                                    <li class="flex items-center gap-2"><i data-lucide="check" class="w-3.5 h-3.5 text-accent"></i> Onderzoek naar merkvertrouwen en commerciële positionering</li>
                                </ul>
                            </div>"""

jaar4_vitens_new = """                            <div class="mb-8 last:mb-0 relative mt-8 pt-8 border-t border-zinc-800">
                                <div class="absolute -left-[37px] top-9 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold">Project 2: Vitens | Water as a Service</h4>
                                <p class="text-zinc-300 text-base leading-relaxed mb-4">
                                    Ontwikkeling van een commerciële positionering in de grootzakelijke markt via een 'Water as a Service'-model. Marktonderzoek, stakeholderanalyses en strategische scenario's leidden tot advies voor een nieuwe commerciële entiteit met behoud van merkvertrouwen.
                                </p>
                            </div>"""
content = content.replace(jaar4_vitens_old, jaar4_vitens_new)

afstuderen_old = """                        <div class="p-6 rounded-2xl bg-zinc-900/30 border border-zinc-800 space-y-4 my-6">
                            <h4 class="text-base font-bold text-white">Uitgebreide Markt- & Sectoranalyse</h4>
                            <p class="text-zinc-400 text-sm leading-relaxed">
                                Binnen het onderzoek werd een uitgebreide markt- en sectoranalyse uitgevoerd naar:
                            </p>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-zinc-400 text-sm pl-2">
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> De structuur van de UK-aardappelmarkt</div>
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> Ketencomplexiteit binnen handel, verwerking en pootgoed</div>
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> ERP-landschappen binnen de sector</div>
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> Operationele pijnpunten</div>
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> Koopcriteria</div>
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> Concurrentiepositie</div>
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> Regelgeving en traceability-eisen</div>
                                <div class="flex items-start gap-2"><span class="text-accent">•</span> Segmentfit voor Agrio binnen de UK-markt</div>
                            </div>
                            <p class="text-zinc-400 text-xs italic">
                                Voor het onderzoek werden deskresearch, deskundige enquêtes en diepte-interviews uitgevoerd in de vorm van gesprekken met experts en potentiële klanten in England, Scotland, Noord-Ierland en Wales (United Kingdom).
                            </p>
                        </div>"""

afstuderen_new = """                        <div class="relative pl-8 border-l border-zinc-800 ml-2 my-8">
                            <div class="mb-8 last:mb-0 relative">
                                <div class="absolute -left-[37px] top-1 w-4 h-4 rounded-full bg-[#121212] border-2 border-accent"></div>
                                <h4 class="text-accent font-mono text-sm uppercase mb-2 font-bold">Uitgebreide Markt- & Sectoranalyse</h4>
                                <p class="text-zinc-300 text-base leading-relaxed mb-4">
                                    Onderzoek naar de UK-aardappelmarkt, inclusief ketencomplexiteit, ERP-landschappen, operationele pijnpunten en koopcriteria. Via deskresearch en diepte-interviews met experts in Engeland, Schotland, Noord-Ierland en Wales werd de segmentfit voor Agrio geanalyseerd.
                                </p>
                            </div>
                        </div>"""
content = content.replace(afstuderen_old, afstuderen_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

