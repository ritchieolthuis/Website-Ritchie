#!/bin/bash
git checkout 45e67b6 index.html
python3 update_recs.py
python3 fix_projects.py
python3 fix_axelio.py
python3 fix_timeline.py
python3 fix_timeline2.py
python3 fix_chart.py
python3 fix_portfolio_overview.py
python3 fix_axelio_theme.py
python3 fix_jaar4_text.py
python3 fix_portfolio_overview_7cards.py
python3 fix_titles.py
python3 fix_sizing.py
python3 fix_div.py
python3 fix_apa_references.py
python3 fix_embedded_apa.py
python3 fix_chart_and_ikigai.py
python3 rewrite_reflection.py
python3 fix_bronnenlijst.py
python3 fix_bijlage6_link.py
python3 fix_bronnenlijst_links.py
python3 fix_forms_links.py
python3 fix_all_links.py
python3 add_axelio_story.py
python3 fix_feedback_rubric.py
python3 polish_aesthetics.py
python3 check_html.py
python3 final_polish.py
python3 fix_photos.py
python3 fix_slider.py
python3 fix_slider_and_order.py
python3 fix_slider_and_order_v2.py
python3 update_deficiencies.py
python3 fix_vpmc.py
python3 fix_vpmc_final.py
python3 make_interactive.py
python3 remove_js_ikigai.py
python3 sync_rubrics.py
python3 fix_colors.py

# Manually apply the VPMC links (done at 08:57 via replace_file_content)
python3 -c "
import sys
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(
    '<a href=\"https://drive.google.com/file/d/1tsutEYmsX6gbSlqcE0yby6SchmnQrFsT/view?usp=sharing\" target=\"_blank\" class=\"block p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors cursor-pointer group\">',
    '<a href=\"https://drive.google.com/file/d/10Cbi47PEdeNzJrWiJJd0EAz5SgOvTa9M/view?usp=sharing\" target=\"_blank\" class=\"block p-4 rounded-xl bg-zinc-800/30 border border-zinc-700/50 hover:border-zinc-600 transition-colors cursor-pointer group\">'
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
"

# Manually apply profile photo fix (done at 09:01 via sed)
python3 -c "
import sys
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('/assets/profile.jpg', '/assets/1766968193816.jpeg')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
"
