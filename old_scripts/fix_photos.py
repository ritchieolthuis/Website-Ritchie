import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

alma_current = 'https://media.licdn.com/dms/image/v2/D4E03AQEakbDrMEcHpQ/profile-displayphoto-crop_800_800/B4EZ4_soOqKYAI-/0/1779185129622?e=1781136000&v=beta&t=3Hh5VPmtMKUpVy_LsUSxKi5QDlSkes7SsaN6kHAwV5A'
eric_current = '/assets/eric_vredeveldt.jpg'
martijn_current = 'https://media.licdn.com/dms/image/v2/C5603AQEtbc-9HmikSg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1517727248745?e=1781136000&v=beta&t=wfQJYIQv-aVK9sNJRFSazCT5-EvWoFeDW_TAHR5J2NU'
elma_current = 'https://media.licdn.com/dms/image/v2/C4D03AQFEDuVRvqzM_w/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1547551348628?e=1781136000&v=beta&t=xfr5Hl5TjEvWLd6aJQLhOZBraayWzr80bxf3OqlmkAA'

alma_new = 'https://media.licdn.com/dms/image/v2/D4E03AQHIOvSk7dG1aQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1718250141902?e=1781136000&v=beta&t=eRjivt-Nt5NXiFEHN0skuZhyt4QhsO0dK6W0UaFvgU4'
eric_new = alma_current
martijn_new = elma_current
elma_new = martijn_current

# Replace Alma's photo
content = content.replace(alma_current, alma_new)
# Since I replaced alma_current with alma_new in the entire file, the old alma_current is GONE.
# But Eric needs it! So I should have been careful not to replace it globally.
# Actually, Eric's box had `eric_current`. I just need to replace `eric_current` with `eric_new`!
content = content.replace(eric_current, eric_new)

# Swap Martijn and Elma
# Because they might swap back and forth, let's use a temporary string
content = content.replace(martijn_current, 'TEMP_MARTIJN_PHOTO')
content = content.replace(elma_current, martijn_current)
content = content.replace('TEMP_MARTIJN_PHOTO', elma_current)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

