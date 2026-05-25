import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the div tags of the cards with anchor tags and add the Google Drive link
# I will use replace on the class string since it's unique enough for these 3 cards.
old_card_class = '<div class="p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors">'
new_card_class = '<a href="https://drive.google.com/file/d/1tsutEYmsX6gbSlqcE0yby6SchmnQrFsT/view?usp=sharing" target="_blank" class="block p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors cursor-pointer group">'

content = content.replace(old_card_class, new_card_class)
# Also need to replace the closing `</div>` of those specific cards with `</a>`. 
# Because this could be tricky with replace, I will just manually replace the whole block.

old_block = """                            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
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

new_block = """                            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
                                <!-- Wiskunde -->
                                <a href="https://drive.google.com/file/d/1tsutEYmsX6gbSlqcE0yby6SchmnQrFsT/view?usp=sharing" target="_blank" class="block p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors cursor-pointer group">
                                    <div class="flex justify-between items-start mb-2">
                                        <h5 class="text-white font-bold text-sm flex items-center gap-2 group-hover:text-accent transition-colors"><i data-lucide="calculator" class="w-4 h-4 text-accent"></i> VPMC Wiskunde</h5>
                                        <i data-lucide="external-link" class="w-3 h-3 text-zinc-600 group-hover:text-accent transition-colors"></i>
                                    </div>
                                    <p class="text-zinc-500 text-[10px] uppercase font-mono mb-3 tracking-wider">Voorbereiding Universiteit</p>
                                    <ul class="text-zinc-400 text-xs space-y-1.5 list-disc list-inside">
                                        <li>Elementaire rekenkundige bewerkingen</li>
                                        <li>Lineaire & Tweedegraads functies</li>
                                        <li>Differentiëren & Integreren</li>
                                    </ul>
                                </a>
                                <!-- Statistiek -->
                                <a href="https://drive.google.com/file/d/1tsutEYmsX6gbSlqcE0yby6SchmnQrFsT/view?usp=sharing" target="_blank" class="block p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors cursor-pointer group">
                                    <div class="flex justify-between items-start mb-2">
                                        <h5 class="text-white font-bold text-sm flex items-center gap-2 group-hover:text-accent transition-colors"><i data-lucide="bar-chart-2" class="w-4 h-4 text-accent"></i> VPMC Statistiek</h5>
                                        <i data-lucide="external-link" class="w-3 h-3 text-zinc-600 group-hover:text-accent transition-colors"></i>
                                    </div>
                                    <p class="text-zinc-500 text-[10px] uppercase font-mono mb-3 tracking-wider">Voorbereiding Universiteit</p>
                                    <ul class="text-zinc-400 text-xs space-y-1.5 list-disc list-inside">
                                        <li>Beschrijvende Statistiek (Grafieken, kengetallen)</li>
                                        <li>Kansrekening (Regels, combinaties, permutaties)</li>
                                        <li>Verklarende statistiek (Betrouwbaarheidsinterval, toetsen)</li>
                                    </ul>
                                </a>
                                <!-- Engels -->
                                <a href="https://drive.google.com/file/d/1tsutEYmsX6gbSlqcE0yby6SchmnQrFsT/view?usp=sharing" target="_blank" class="block p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors cursor-pointer group">
                                    <div class="flex justify-between items-start mb-2">
                                        <h5 class="text-white font-bold text-sm flex items-center gap-2 group-hover:text-accent transition-colors"><i data-lucide="globe" class="w-4 h-4 text-accent"></i> VPMC Engels</h5>
                                        <i data-lucide="external-link" class="w-3 h-3 text-zinc-600 group-hover:text-accent transition-colors"></i>
                                    </div>
                                    <p class="text-zinc-500 text-[10px] uppercase font-mono mb-3 tracking-wider">Voorbereiding Universiteit</p>
                                    <ul class="text-zinc-400 text-xs space-y-1.5 list-disc list-inside">
                                        <li>Business English (Listening & Reading)</li>
                                        <li>Business English Grammar & Vocabulary</li>
                                        <li>Speaking and Writing Practice</li>
                                    </ul>
                                </a>
                            </div>"""

# Remove the partial replace I did on line 9 and 10 which is now commented out.
if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("WARNING: Could not find old block")
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

