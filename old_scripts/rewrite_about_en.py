import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

en_old = r'about_text:\s*"I am an ambitious fourth-year Commercial Economics student at Windesheim University of Applied Sciences.*?the world around us\.",'

en_new = '''about_text: "<div class='text-zinc-400 leading-relaxed font-sans'><p class='mb-4 text-sm md:text-base'>Fourth-year Commercial Economics student (Windesheim) with minors in Business Administration and Financial Decision Making.</p><div id='about-more-en' class='hidden opacity-0 transition-opacity duration-500 text-sm md:text-base'><p>Profile focuses on quantitative and qualitative analysis, iterative project management, and data-driven decision making to support business challenges.<br><br>Professional practice consists of analyzing process bottlenecks and implementing measurable process improvements. The emphasis is on applying academic theory in commercial practice to optimize efficiency and business results.</p></div><button onclick='const more = document.getElementById(\\"about-more-en\\"); const btn = this; if (more.classList.contains(\\"hidden\\")) { more.classList.remove(\\"hidden\\"); setTimeout(() => more.classList.remove(\\"opacity-0\\"), 10); btn.innerHTML = \\"Hide details <i data-lucide=\\\\\\"chevron-up\\\\\\" class=\\\\\\"w-4 h-4\\\\\\"></i>\\"; } else { more.classList.add(\\"opacity-0\\"); setTimeout(() => more.classList.add(\\"hidden\\"), 500); btn.innerHTML = \\"Read Full Profile <i data-lucide=\\\\\\"chevron-down\\\\\\" class=\\\\\\"w-4 h-4\\\\\\"></i>\\"; } window.lucide.createIcons();' class='mt-4 flex items-center gap-2 text-accent text-sm font-bold hover:underline transition-all'>Read Full Profile <i data-lucide='chevron-down' class='w-4 h-4'></i></button></div>",'''

content, count_en = re.subn(en_old, en_new, content, count=1, flags=re.DOTALL)
print("EN About replace:", count_en)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

