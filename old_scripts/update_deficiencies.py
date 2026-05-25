import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """                            <div class="flex gap-4 text-sm text-zinc-300 font-medium pl-2">
                                <div class="flex items-center gap-2"><i data-lucide="plus" class="w-4 h-4 text-accent"></i> Wiskunde</div>
                                <div class="flex items-center gap-2"><i data-lucide="plus" class="w-4 h-4 text-accent"></i> Statistiek</div>
                                <div class="flex items-center gap-2"><i data-lucide="plus" class="w-4 h-4 text-accent"></i> Engels</div>
                            </div>"""

new_block = """                            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
                                <!-- Wiskunde -->
                                <div class="p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors">
                                    <div class="flex justify-between items-start mb-2">
                                        <h5 class="text-white font-bold text-sm flex items-center gap-2"><i data-lucide="calculator" class="w-4 h-4 text-accent"></i> VPMC Wiskunde</h5>
                                        <span class="text-xs font-mono text-accent bg-accent/10 px-2 py-0.5 rounded">7.1</span>
                                    </div>
                                    <p class="text-zinc-500 text-[10px] uppercase font-mono mb-3 tracking-wider">2 EC behaald</p>
                                    <ul class="text-zinc-400 text-xs space-y-1.5 list-disc list-inside">
                                        <li>Elementaire rekenkundige bewerkingen</li>
                                        <li>Lineaire & Tweedegraads functies</li>
                                        <li>Differentiëren & Integreren</li>
                                    </ul>
                                </div>
                                <!-- Statistiek -->
                                <div class="p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors">
                                    <div class="flex justify-between items-start mb-2">
                                        <h5 class="text-white font-bold text-sm flex items-center gap-2"><i data-lucide="bar-chart-2" class="w-4 h-4 text-accent"></i> VPMC Statistiek</h5>
                                        <span class="text-xs font-mono text-accent bg-accent/10 px-2 py-0.5 rounded">5.8</span>
                                    </div>
                                    <p class="text-zinc-500 text-[10px] uppercase font-mono mb-3 tracking-wider">2 EC behaald</p>
                                    <ul class="text-zinc-400 text-xs space-y-1.5 list-disc list-inside">
                                        <li>Beschrijvende Statistiek (Grafieken, kengetallen)</li>
                                        <li>Kansrekening (Regels, combinaties, permutaties)</li>
                                        <li>Verklarende statistiek (Betrouwbaarheidsinterval, toetsen)</li>
                                    </ul>
                                </div>
                                <!-- Engels -->
                                <div class="p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors">
                                    <div class="flex justify-between items-start mb-2">
                                        <h5 class="text-white font-bold text-sm flex items-center gap-2"><i data-lucide="globe" class="w-4 h-4 text-accent"></i> VPMC Engels</h5>
                                        <span class="text-xs font-mono text-accent bg-accent/10 px-2 py-0.5 rounded">7.7</span>
                                    </div>
                                    <p class="text-zinc-500 text-[10px] uppercase font-mono mb-3 tracking-wider">2 EC behaald</p>
                                    <ul class="text-zinc-400 text-xs space-y-1.5 list-disc list-inside">
                                        <li>Business English (Listening & Reading, B2 level)</li>
                                        <li>Business English Grammar & Vocabulary</li>
                                        <li>Speaking and Writing Practice</li>
                                    </ul>
                                </div>
                            </div>"""

content = content.replace(old_block, new_block)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

