import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace the whole block starting with `<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">`
# Let's find it.
start_str = '<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">'
end_str = '                            <p class="text-zinc-400 text-sm leading-relaxed">\n                                Deze voorbereidende vakken'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    old_block = content[start_idx:end_idx]
    
    new_block = """<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
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
                            </div>\n"""
    
    content = content.replace(old_block, new_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("COULD NOT FIND BLOCK")

