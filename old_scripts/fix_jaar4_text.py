import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the text inside Jaar 4 card
# Currently it has:
# <p class="text-white font-bold text-lg md:text-xl mb-3">Young Professional Commerce</p>
# <p class="text-zinc-500 text-sm font-mono uppercase tracking-wider">Semester 7</p>

# Let's replace the content block for Jaar 4
old_block = """<p class="text-white font-bold text-lg md:text-xl mb-3">Young Professional Commerce</p>"""
new_block = """<p class="text-white font-bold text-lg md:text-xl mb-2">Young Professional Commerce Programme</p>
                            <p class="text-zinc-400 text-sm mb-3">Perron038 | Factory NEXT Positionering<br>Vitens | Water as a Service Positionering</p>"""

content = content.replace(old_block, new_block)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

