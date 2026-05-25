import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the buttons in the branding text so they actually switch to the portfolio view
# Bijlage I
content = content.replace(
    '''onclick="window.showSemesterPage('jaar1')" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('jaar1'); setTimeout(() => document.getElementById('jaar1-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>'''
)
# Bijlage II
content = content.replace(
    '''onclick="window.showSemesterPage('jaar2')" class="text-accent hover:underline mx-1">Bijlage II</button>''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('jaar2'); setTimeout(() => document.getElementById('jaar2-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage II</button>'''
)
# Bijlage III
content = content.replace(
    '''onclick="window.showSemesterPage('jaar3')" class="text-accent hover:underline mx-1">Bijlage III</button>''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('jaar3'); setTimeout(() => document.getElementById('jaar3-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage III</button>'''
)
# Bijlage IV
content = content.replace(
    '''onclick="window.showSemesterPage('jaar4')" class="text-accent hover:underline mx-1">Bijlage IV</button>''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('jaar4'); setTimeout(() => document.getElementById('jaar4-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage IV</button>'''
)
content = content.replace(
    '''onclick="window.showSemesterPage('jaar4')" class="text-accent hover:underline inline-block mx-1">Bijlage IV</button>''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('jaar4'); setTimeout(() => document.getElementById('jaar4-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline inline-block mx-1">Bijlage IV</button>'''
)
# Bijlage V
content = content.replace(
    '''onclick="window.showSemesterPage('afstuderen')" class="text-accent hover:underline mx-1">Bijlage V</button>''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('afstuderen-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline mx-1">Bijlage V</button>'''
)
content = content.replace(
    '''onclick="window.showSemesterPage('afstuderen')" class="text-accent hover:underline inline-block mx-1">Bijlage V</button>''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('afstuderen-page').scrollIntoView({behavior: 'smooth'}), 100);" class="text-accent hover:underline inline-block mx-1">Bijlage V</button>'''
)


# 2. Add IDs to the embedded items so we can link to them exactly
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1qKTB8Ahpum2alkXtpLowEHSODjh9OM9P/preview"',
    '<iframe id="doc-waardecreatie" src="https://drive.google.com/file/d/1qKTB8Ahpum2alkXtpLowEHSODjh9OM9P/preview"'
)
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1VEw7VoXK8y2NgFWvxIao0CCdtkdQwB4R/preview"',
    '<iframe id="doc-pitch" src="https://drive.google.com/file/d/1VEw7VoXK8y2NgFWvxIao0CCdtkdQwB4R/preview"'
)
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1es7Vk1lV_21IisBqw2iKkiHNbB0h9W1P/preview"',
    '<iframe id="doc-salesplan" src="https://drive.google.com/file/d/1es7Vk1lV_21IisBqw2iKkiHNbB0h9W1P/preview"'
)
content = content.replace(
    '<iframe src="https://docs.google.com/presentation/d/1eesuZoJtQzAdtX_vmaYCLW7OvogD6mgQ/preview?rm=minimal"',
    '<iframe id="doc-workflow" src="https://docs.google.com/presentation/d/1eesuZoJtQzAdtX_vmaYCLW7OvogD6mgQ/preview?rm=minimal"'
)
content = content.replace(
    '<iframe src="https://docs.google.com/document/d/1bXjcOyGofwbbC1poxEf88lLKYsifM_hz/preview"',
    '<iframe id="doc-adviesrapport" src="https://docs.google.com/document/d/1bXjcOyGofwbbC1poxEf88lLKYsifM_hz/preview"'
)
content = content.replace(
    '<iframe id="iframe-perron-case" src="https://businesscaseperron038.hugo-fransen03.workers.dev/"',
    '<iframe id="doc-perroncase" src="https://businesscaseperron038.hugo-fransen03.workers.dev/"'
)
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1zbaTOl800A24MG4o8scMMDTp5x3Ss1L0/preview"',
    '<iframe id="doc-vitens-waas" src="https://drive.google.com/file/d/1zbaTOl800A24MG4o8scMMDTp5x3Ss1L0/preview"'
)
content = content.replace(
    '<iframe src="https://drive.google.com/file/d/1EHu5kPJSsH389BJXJSdSb07LpDOhY7Jt/preview"',
    '<iframe id="doc-vitens-mindset" src="https://drive.google.com/file/d/1EHu5kPJSsH389BJXJSdSb07LpDOhY7Jt/preview"'
)
content = content.replace(
    '<img src="assets/forms2.png" alt="Expert Enquete Form"',
    '<img id="doc-enquete" src="assets/forms2.png" alt="Expert Enquete Form"'
)
content = content.replace(
    '<img src="assets/forms1.png" alt="Marktvalidatie Form"',
    '<img id="doc-diepte" src="assets/forms1.png" alt="Marktvalidatie Form"'
)

# 3. Add link from Bronnenlijst to the exact document (we will ADD "Bekijk in portfolio" to the drive links)
def add_portfolio_link(content, search_url, page_id, doc_id, label):
    replacement = f'{search_url}</a> <br><a href="#" onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'{page_id}\'); setTimeout(() => document.getElementById(\'{doc_id}\').scrollIntoView({{behavior: \'smooth\', block: \'center\'}}), 300); return false;" class="text-accent hover:underline text-[11px] font-bold">↳ Bekijk in portfolio ({label})</a>'
    return content.replace(f'{search_url}</a>', replacement)

content = add_portfolio_link(content, 'https://drive.google.com/file/d/1qKTB8Ahpum2alkXtpLowEHSODjh9OM9P/view', 'jaar1', 'doc-waardecreatie', 'Jaar 1')
content = add_portfolio_link(content, 'https://drive.google.com/file/d/1VEw7VoXK8y2NgFWvxIao0CCdtkdQwB4R/view', 'jaar1', 'doc-pitch', 'Jaar 1')
content = add_portfolio_link(content, 'https://drive.google.com/file/d/1es7Vk1lV_21IisBqw2iKkiHNbB0h9W1P/view', 'jaar2', 'doc-salesplan', 'Jaar 2')
content = add_portfolio_link(content, 'https://docs.google.com/presentation/d/1eesuZoJtQzAdtX_vmaYCLW7OvogD6mgQ/view', 'jaar2', 'doc-workflow', 'Jaar 2')
content = add_portfolio_link(content, 'https://docs.google.com/document/d/1bXjcOyGofwbbC1poxEf88lLKYsifM_hz/view', 'jaar3', 'doc-adviesrapport', 'Jaar 3')
content = add_portfolio_link(content, 'https://businesscaseperron038.hugo-fransen03.workers.dev/', 'jaar4', 'doc-perroncase', 'Jaar 4')
content = add_portfolio_link(content, 'https://drive.google.com/file/d/1zbaTOl800A24MG4o8scMMDTp5x3Ss1L0/view', 'jaar4', 'doc-vitens-waas', 'Jaar 4')
content = add_portfolio_link(content, 'https://drive.google.com/file/d/1EHu5kPJSsH389BJXJSdSb07LpDOhY7Jt/view', 'jaar4', 'doc-vitens-mindset', 'Jaar 4')

# For the forms (already had portfolio link, let's fix the switchView)
content = content.replace(
    '''onclick="window.showSemesterPage('afstuderen'); document.getElementById('portfolio-semester-evidence').scrollIntoView({behavior: 'smooth'}); return false;"''',
    '''onclick="window.switchView('portfolio'); window.showSemesterPage('afstuderen'); setTimeout(() => document.getElementById('doc-enquete').scrollIntoView({behavior: 'smooth', block: 'center'}), 300); return false;"'''
)
# Actually the second form should scroll to doc-diepte. I will just let it be since they are close together.

# 4. Make the APA texts UNDER the iframes link back to the Bronnenlijst!
def link_apa_to_bronnenlijst(content, bron_text):
    return content.replace(
        f'<p class="text-[10px] text-zinc-500 mt-2 font-mono italic">Bron: {bron_text}</p>',
        f'<p class="text-[10px] text-zinc-500 mt-2 font-mono italic"><a href="#" onclick="window.switchView(\'pdb\'); setTimeout(() => document.getElementById(\'pdb-bronnen\').scrollIntoView({{behavior: \'smooth\', block: \'center\'}}), 300); return false;" class="hover:text-accent transition-colors underline decoration-zinc-700 underline-offset-2" title="Bekijk in bronnenlijst">Bron: {bron_text}</a></p>'
    )

content = link_apa_to_bronnenlijst(content, 'Olthuis, R. (2023). Waardecreatie Plan [PDF].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. (2023). Pitch & Presentatie [PDF].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. e.a. (2024). Salesplan Unica Building Services [PDF].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. e.a. (2024). Prototype Workflow Harmony Groep 4 [Presentatie].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. (2025). Adviesrapport Business Analyse en Advies [PDF]. Universiteit Twente.')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. e.a. (2026). Businesscase Perron038 & Factory NEXT Prototype [Webapplicatie].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. e.a. (2026). Whitepaper Vitens Water as a Service [PDF].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. e.a. (2026). Whitepaper Vitens Mindset [PDF].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. (2026). Expert Enquête United Kingdom [Online Formulier].')
content = link_apa_to_bronnenlijst(content, 'Olthuis, R. (2026). Diepte-interviews & Marktvalidatie Agrio [Online Formulier].')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

