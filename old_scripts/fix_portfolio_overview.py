import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the grid with the vertical roadmap
old_grid_pattern = re.compile(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">(.*?)<!-- Afstuderen Card -->.*?</div>\s*</div>\s*</div>', re.DOTALL)

def create_roadmap_card(id_str, img_src, year_title, main_title, semester_text):
    return f"""                  <!-- {year_title} Card -->
                  <div class="relative group cursor-pointer data-hover-trigger" onclick="window.showSemesterPage('{id_str}')">
                     <!-- Timeline Dot -->
                     <div class="absolute -left-[41px] md:-left-[57px] top-8 w-5 h-5 rounded-full bg-[#121212] border-2 border-accent group-hover:bg-accent transition-colors z-10 shadow-[0_0_10px_rgba(204,255,0,0)] group-hover:shadow-[0_0_15px_rgba(204,255,0,0.5)]"></div>
                     
                     <div class="bg-zinc-900/40 border border-zinc-800 rounded-3xl overflow-hidden hover:border-zinc-700 transition-all duration-500 flex flex-col md:flex-row shadow-lg hover:shadow-2xl">
                         <div class="h-56 md:h-auto md:w-2/5 overflow-hidden relative border-b md:border-b-0 md:border-r border-zinc-800">
                             <img src="{img_src}" class="w-full h-full object-cover grayscale opacity-80 group-hover:grayscale-0 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700" alt="{year_title}">
                             <div class="absolute inset-0 bg-gradient-to-t md:bg-gradient-to-r from-[#121212] to-transparent opacity-60"></div>
                         </div>
                         <div class="p-8 md:p-12 flex-grow flex flex-col justify-center relative bg-[#121212]">
                            <div class="flex justify-between items-start mb-6">
                               <h3 class="text-3xl md:text-4xl font-display text-white group-hover:text-accent font-bold transition-colors">{year_title}</h3>
                               <div class="w-12 h-12 rounded-full bg-zinc-900 border border-zinc-800 flex items-center justify-center text-zinc-400 group-hover:bg-accent group-hover:text-black group-hover:border-accent transition-all flex-shrink-0">
                                  <i data-lucide="arrow-right" class="w-6 h-6 group-hover:translate-x-1 transition-transform"></i>
                               </div>
                            </div>
                            <p class="text-white font-bold text-lg md:text-xl mb-3">{main_title}</p>
                            <p class="text-zinc-500 text-sm font-mono uppercase tracking-wider">{semester_text}</p>
                         </div>
                     </div>
                  </div>"""

new_grid = f"""<div class="relative pl-8 md:pl-12 border-l-2 border-zinc-800 ml-4 max-w-5xl mx-auto space-y-16">
{create_roadmap_card('jaar1', 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?q=80&w=2070', 'Jaar 1', 'Fundament & Professionele Ontwikkeling', 'Semester 1 & 2')}
{create_roadmap_card('jaar2', 'https://stapintechniek.nl/wp-content/uploads/2025/10/7r31189-scaled.jpg', 'Jaar 2', 'Business Development | Unica', 'Semester 3 & 4')}
{create_roadmap_card('jaar3', 'https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=2070', 'Jaar 3', 'Minor Financiële & Pre-master UT', 'Semester 5 & 6')}
{create_roadmap_card('jaar4', 'https://www.h2owaternetwerk.nl/images/2020/December/vitens_strategie_duurzaam.jpg', 'Jaar 4', 'Young Professional Commerce', 'Semester 7')}
{create_roadmap_card('afstuderen', 'https://axelio-prod.s3.nl-ams.scw.cloud/Axelio_corporate_foto_a9f672c561.jpg', 'Afstuderen', 'Axelio / Agrio UK Market Entry', 'Semester 8')}
               </div>"""

# Replace in content
match = old_grid_pattern.search(content)
if match:
    # Need to correctly replace the full grid block
    old_full_block = match.group(0)
    # The regex captured up to <!-- Afstuderen Card -->... </div></div></div>
    # Actually it's safer to just split by <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"> and the closing div of the grid.
    pass

# Let's use a simpler string replace since we know the exact start.
start_str = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
end_str = '<!-- Semester Pages Container -->'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_grid + "\n            " + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

