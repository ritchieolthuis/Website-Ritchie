import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the modal larger
content = content.replace(
    'class="w-full max-w-6xl h-full max-h-[90vh] bg-[#121212] border border-zinc-800 rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in"',
    'class="w-full max-w-[95vw] h-full max-h-[95vh] bg-[#121212] border border-zinc-800 rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in"'
)

# Also for expertise modal
content = content.replace(
    'class="w-full max-w-5xl h-full max-h-[85vh] bg-[#121212] border border-zinc-800 rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in"',
    'class="w-full max-w-[95vw] h-full max-h-[95vh] bg-[#121212] border border-zinc-800 rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in"'
)

# Also for services modal
content = content.replace(
    'class="w-full max-w-6xl h-auto max-h-[90vh] bg-[#121212] border border-zinc-800 rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in"',
    'class="w-full max-w-[95vw] h-full max-h-[95vh] bg-[#121212] border border-zinc-800 rounded-3xl shadow-2xl overflow-hidden flex flex-col pointer-events-auto relative transform transition-all animate-fade-in"'
)

# And increase the max-width of the inner semester pages from max-w-4xl to max-w-5xl
content = content.replace('class="semester-page hidden space-y-8 text-white max-w-4xl mx-auto animate-fade-in"', 
                          'class="semester-page hidden space-y-8 text-white max-w-5xl mx-auto animate-fade-in"')
content = content.replace('class="semester-page space-y-8 text-white max-w-4xl mx-auto animate-fade-in"',
                          'class="semester-page space-y-8 text-white max-w-5xl mx-auto animate-fade-in"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

