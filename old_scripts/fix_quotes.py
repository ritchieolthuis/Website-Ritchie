import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix English
en_old_match = re.search(r'about_text: "<div.*?Read Full Profile.*?</div>",', content, re.DOTALL)
if en_old_match:
    en_new = '''about_text: "<div class='text-zinc-400 leading-relaxed font-sans'><p class='mb-4 text-sm md:text-base'>Fourth-year Commercial Economics student (Windesheim) with minors in Business Administration and Financial Decision Making.</p><div id='about-more-en' class='hidden opacity-0 transition-opacity duration-500 text-sm md:text-base'><p>Profile focuses on quantitative and qualitative analysis, iterative project management, and data-driven decision making to support business challenges.<br><br>Professional practice consists of analyzing process bottlenecks and implementing measurable process improvements. The emphasis is on applying academic theory in commercial practice to optimize efficiency and business results.</p></div><button onclick=\\"const more = document.getElementById('about-more-en'); const btn = this; if (more.classList.contains('hidden')) { more.classList.remove('hidden'); setTimeout(() => more.classList.remove('opacity-0'), 10); btn.innerHTML = `Hide details <i data-lucide='chevron-up' class='w-4 h-4'></i>`; } else { more.classList.add('opacity-0'); setTimeout(() => more.classList.add('hidden'), 500); btn.innerHTML = `Read Full Profile <i data-lucide='chevron-down' class='w-4 h-4'></i>`; } window.lucide.createIcons();\\" class='mt-4 flex items-center gap-2 text-accent text-sm font-bold hover:underline transition-all'>Read Full Profile <i data-lucide='chevron-down' class='w-4 h-4'></i></button></div>",'''
    content = content.replace(en_old_match.group(0), en_new)

# Fix Dutch
nl_old_match = re.search(r'about_text: "<div.*?Lees Volledig Profiel.*?</div>",', content, re.DOTALL)
if nl_old_match:
    nl_new = '''about_text: "<div class='text-zinc-400 leading-relaxed font-sans'><p class='mb-4 text-sm md:text-base'>Vierdejaarsstudent Commerciële Economie (Hogeschool Windesheim) met afgeronde minors in Bedrijfskunde en Financiële Besluitvorming.</p><div id='about-more' class='hidden opacity-0 transition-opacity duration-500 text-sm md:text-base'><p>Het profiel richt zich op kwantitatieve en kwalitatieve analyse, iteratief projectmanagement en datagedreven besluitvorming ter ondersteuning van bedrijfskundige vraagstukken.<br><br>De beroepspraktijk bestaat uit het analyseren van procesknelpunten en het implementeren van meetbare procesverbeteringen. De nadruk ligt op de toepassing van academische theorie in de commerciële praktijk om efficiëntie en bedrijfsresultaten te optimaliseren.</p></div><button onclick=\\"const more = document.getElementById('about-more'); const btn = this; if (more.classList.contains('hidden')) { more.classList.remove('hidden'); setTimeout(() => more.classList.remove('opacity-0'), 10); btn.innerHTML = `Verberg details <i data-lucide='chevron-up' class='w-4 h-4'></i>`; } else { more.classList.add('opacity-0'); setTimeout(() => more.classList.add('hidden'), 500); btn.innerHTML = `Lees Volledig Profiel <i data-lucide='chevron-down' class='w-4 h-4'></i>`; } window.lucide.createIcons();\\" class='mt-4 flex items-center gap-2 text-accent text-sm font-bold hover:underline transition-all'>Lees Volledig Profiel <i data-lucide='chevron-down' class='w-4 h-4'></i></button></div>",'''
    content = content.replace(nl_old_match.group(0), nl_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed syntax")
