import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_text = "Van de zestien vaardigheden focus ik mij met name op Initiatief, Samenwerken, Verantwoordelijkheid en het durven handelen in onzekerheid."
new_text = "Van de zestien vaardigheden focus ik mij met name op de kern-rubrics: Initiatief, Samenwerken, Verantwoordelijkheid (Eigenaarschap), Analytisch denken, Besluitvaardigheid en Iteratief werken (Design Thinking)."

content = content.replace(old_text, new_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
