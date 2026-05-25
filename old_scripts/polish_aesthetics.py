import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change semester-page width to max-w-4xl for better readability, and increase spacing
content = content.replace(
    'class="semester-page hidden space-y-8 text-white max-w-5xl mx-auto animate-fade-in"',
    'class="semester-page hidden space-y-10 text-white max-w-4xl mx-auto animate-fade-in py-4"'
)

# 2. Improve text readability: text-zinc-300 text-base leading-relaxed -> text-zinc-300 md:text-lg leading-[1.8] font-light
# Let's target paragraphs generally inside semester-page, but since we can't easily parse DOM, we'll do broad replacements.
content = content.replace('text-base leading-relaxed', 'text-base md:text-[17px] leading-[1.8] font-light tracking-wide')

# 3. Improve the iframes styling: they are currently w-full h-[500px] rounded-xl border border-zinc-800 bg-white
# Let's add a subtle shadow and pad the container if needed. Actually the classes are fine, but let's make the shadow richer.
content = content.replace(
    'rounded-xl border border-zinc-800 bg-white',
    'rounded-2xl border border-zinc-700/50 bg-white shadow-2xl shadow-black/50 ring-1 ring-white/5'
)
content = content.replace(
    'h-[500px]',
    'h-[500px] md:h-[600px]'
)

# 4. Improve the 'marktpijnpunten' gradient box on Afstuderen
content = content.replace(
    'bg-gradient-to-br from-zinc-900 to-black border border-accent/20',
    'bg-gradient-to-br from-[#1a1a1a] to-[#0a0a0a] border border-accent/30 shadow-[0_0_30px_rgba(204,255,0,0.05)]'
)

# 5. Fix the modal container itself: padding and width.
content = content.replace(
    'w-full max-w-[95vw] h-full max-h-[95vh] bg-[#121212] border border-zinc-800 rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in',
    'w-full max-w-[1400px] h-full max-h-[95vh] bg-[#0c0c0c] border border-zinc-800/80 rounded-3xl shadow-[0_0_50px_rgba(0,0,0,0.8)] overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in'
)

# 6. Make the timeline vertical line in semester pages slightly more elegant
content = content.replace(
    'border-l border-zinc-800',
    'border-l border-zinc-800/60'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

