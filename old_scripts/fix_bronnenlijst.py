import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the "Bijlage VI" link under Skills Visualization so it doesn't link to the bronnenlijst
# Right now it is: <button onclick="window.scrollTo({top: document.getElementById('pdb-bronnen').offsetTop, behavior: 'smooth'})" class="text-accent hover:underline inline-block mx-1">Bijlage VI</button>
content = re.sub(
    r'<button onclick="window\.scrollTo\([^>]+>Bijlage VI</button>',
    r'<span class="text-accent font-bold">Bijlage VI</span>',
    content
)

# Also fix the one in the Dutch / English translations
content = content.replace(
    '<button onclick="window.scrollTo({top: document.getElementById(\'pdb-bronnen\').offsetTop, behavior: \'smooth\'})" class="text-accent hover:underline font-bold">Bijlage VI</button>',
    '<span class="text-accent font-bold">Bijlage VI</span>'
)

# 2. Extract and rebuild the entire Bronnenlijst <ul>
ul_pattern = re.compile(r'(<ul class="text-zinc-400 text-xs md:text-sm font-sans space-y-3\.5 pl-1 leading-relaxed">)(.*?)(</ul>)', re.DOTALL)

# All references to be included:
references = [
    'Argyris, C., & Schön, D. A. (1978). <span class="italic">Organizational learning: A theory of action perspective</span>. Addison-Wesley',
    'Brown, T. (2009). <span class="italic">Change by design: How design thinking creates new alternatives for business and society</span>. HarperBusiness',
    'Covey, S. R. (1989). <span class="italic">The 7 habits of highly effective people: Restoring the character ethic</span>. Free Press',
    'Marston, W. M. (1928). <span class="italic">Emotions of normal people</span>. Harcourt, Brace.<br><a href="https://www.abundantlife.nl/disc/uitleg-disc-model" target="_blank" class="text-accent hover:underline break-words">https://www.abundantlife.nl/disc/uitleg-disc-model</a>',
    'Ruijters, M. C. P. (2015). <span class="italic">Mijn binnenste buiten: Over leren, ontwikkelen en identiteit</span>. Vakmedianet',
    'Windesheim. (2026). <span class="italic">Ingevulde CE Skillsguide door medestudenten</span> [Bijlage VI]. Ongepubliceerd manuscript, Windesheim.',
    'Olthuis, R. (2023). <span class="italic">Portfolio Jaar 1: Fundament & Professionele Ontwikkeling</span> [Bijlage I]. Ongepubliceerd portfolio, Windesheim.',
    'Olthuis, R. (2024). <span class="italic">Portfolio Jaar 2: Business Development | Unica Building Services</span> [Bijlage II]. Ongepubliceerd portfolio, Windesheim.',
    'Olthuis, R. (2025). <span class="italic">Portfolio Jaar 3: Minor Financiële Besluitvorming & Pre-master Business Administration</span> [Bijlage III]. Ongepubliceerd portfolio, Universiteit Twente.',
    'Olthuis, R. (2026a). <span class="italic">Portfolio Jaar 4: Young Professional Commerce Programme</span> [Bijlage IV]. Ongepubliceerd portfolio, Windesheim.',
    'Olthuis, R. (2026b). <span class="italic">Afstudeerportfolio: Axelio / Agrio UK Market Entry</span> [Bijlage V]. Ongepubliceerd portfolio, Windesheim.',
    
    # Extra embedded references:
    'Olthuis, R. (2023). <span class="italic">Waardecreatie Plan</span> [PDF]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. (2023). <span class="italic">Pitch & Presentatie</span> [PDF]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. e.a. (2024). <span class="italic">Salesplan Unica Building Services</span> [PDF]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. e.a. (2024). <span class="italic">Prototype Workflow Harmony Groep 4</span> [Presentatie]. Ongepubliceerd, Windesheim.',
    'Olthuis, R. (2025). <span class="italic">Adviesrapport Business Analyse en Advies</span> [PDF]. Ongepubliceerd, Universiteit Twente.',
    'Olthuis, R. e.a. (2026). <span class="italic">Businesscase Perron038 & Factory NEXT Prototype</span> [Webapplicatie].',
    'Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Water as a Service</span> [PDF]. Ongepubliceerd.',
    'Olthuis, R. e.a. (2026). <span class="italic">Whitepaper Vitens Mindset</span> [PDF]. Ongepubliceerd.',
    'Olthuis, R. (2026). <span class="italic">Expert Enquête United Kingdom</span> [Online Formulier].',
    'Olthuis, R. (2026). <span class="italic">Diepte-interviews & Marktvalidatie Agrio</span> [Online Formulier].'
]

# Sort alphabetically
references.sort()

# Build the new <ul> content
new_ul_inner = "\n"
for ref in references:
    new_ul_inner += f'                            <li class="pl-4 -indent-4 mb-2">\n                                {ref}\n                            </li>\n'
new_ul_inner += "                        "

def replace_ul(match):
    return match.group(1) + new_ul_inner + match.group(3)

content = re.sub(ul_pattern, replace_ul, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

