import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update timeline styles in translations
def update_timeline_html(html):
    # Change left border line from border-l-2 to border-l
    # Change the hollow circle from bg-zinc-900 to bg-[#121212] or transparent, and adjust left offset
    # Change title from text-xs to text-sm mb-2
    # Change desc from text-sm to text-base
    
    html = html.replace('border-l-2', 'border-l')
    html = html.replace('-left-[31px] top-1.5 w-4 h-4 rounded-full bg-zinc-900', '-left-[33px] top-1 w-4 h-4 rounded-full bg-[#121212]')
    html = html.replace('text-xs uppercase mb-1', 'text-sm uppercase mb-2 font-bold')
    html = html.replace('text-sm leading-relaxed', 'text-base leading-relaxed text-zinc-300')
    return html

# Find all translation strings for descriptions
pattern = re.compile(r'(proj_(?:axel|1|2|3|4)_desc:\s*`)(.*?)(`,)', re.DOTALL)
def repl_trans(m):
    return m.group(1) + update_timeline_html(m.group(2)) + m.group(3)

content = pattern.sub(repl_trans, content)

# 2. Update default HTML in the slides
pattern_html = re.compile(r'(<div class="relative pl-6 border-l-2 border-zinc-800 ml-2">)(.*?)(</div>\s*</div>\s*<div class="flex flex-wrap)', re.DOTALL)
def repl_html(m):
    return update_timeline_html(m.group(1) + m.group(2)) + m.group(3)

content = pattern_html.sub(repl_html, content)

# 3. Update the titles to be text-2xl
content = content.replace('class="text-xl font-bold text-white group-hover/slide:text-accent transition-colors font-display uppercase tracking-tight mb-4"',
                          'class="text-2xl md:text-3xl font-bold text-white group-hover/slide:text-accent transition-colors font-display uppercase tracking-tight mb-8"')

# 4. Update the skills sections
skills_replacements = {
    'Market Entry': ['Market Entry', 'UK Market'],
    'Market Strategy': ['Market Strategy'],
    'Innovation Hub': ['Innovation Hub', 'Design Thinking'],
    'Sustainability': ['Sustainability', 'Design Thinking'],
    'Growth Marketing': ['Growth Marketing', 'Customer Journey']
}

def build_skills_html(skills):
    html = '<div class="mt-8 pt-6 border-t border-zinc-800">\n'
    html += '                                <h4 class="text-xs uppercase tracking-widest text-zinc-500 font-mono mb-4">Applied Skills</h4>\n'
    html += '                                <div class="grid grid-cols-2 gap-4">\n'
    for skill in skills:
        html += f'''                                    <div>
                                        <div class="flex justify-between items-center mb-2">
                                            <span class="text-zinc-300 font-bold uppercase text-[10px]">{skill}</span>
                                        </div>
                                        <div class="flex gap-1">
                                            <div class="w-1.5 h-1.5 rounded-full bg-accent"></div>
                                            <div class="w-1.5 h-1.5 rounded-full bg-accent"></div>
                                            <div class="w-1.5 h-1.5 rounded-full bg-accent"></div>
                                            <div class="w-1.5 h-1.5 rounded-full bg-accent"></div>
                                            <div class="w-1.5 h-1.5 rounded-full bg-zinc-800"></div>
                                        </div>
                                    </div>\n'''
    html += '                                </div>\n                            </div>'
    return html

# We will use regex to find and replace the flex-wrap gap-2 divs
skill_pattern = re.compile(r'<div class="flex flex-wrap gap-2 mt-4 pt-4 border-t border-zinc-800">(.*?)</div>', re.DOTALL)

def repl_skills(m):
    inner = m.group(1)
    skills = []
    if 'Market Entry' in inner: skills = ['Market Entry', 'UK Market']
    elif 'Market Strategy' in inner: skills = ['Market Strategy', 'Positioning']
    elif 'Innovation Hub' in inner: skills = ['Innovation Hub', 'Design Thinking']
    elif 'Sustainability' in inner: skills = ['Sustainability', 'Design Thinking']
    elif 'Growth Marketing' in inner: skills = ['Growth Marketing', 'Customer Journey']
    
    if not skills: return m.group(0)
    return build_skills_html(skills)

content = skill_pattern.sub(repl_skills, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

