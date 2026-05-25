import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_covey_detail = "Waar ik in de eerste jaren de neiging had om alles kapot te analyseren (Betrokkenheid), heb ik tijdens mijn projecten ervaren dat wachten op 100% zekerheid je simpelweg stilzet. Door sneller beslissingen te nemen en actie te ondernemen binnen mijn Cirkel van Invloed, merk ik dat ik veel effectiever ben geworden in het sturen van projecten en het behalen van concrete resultaten."
new_covey_detail = "Waar in eerdere projectfasen de neiging bestond tot langdurige analyse (Betrokkenheid), heeft de praktijk aangetoond dat het wachten op absolute zekerheid stagnatie in de hand werkt. Door proactiever besluiten te nemen binnen de Cirkel van Invloed, is de effectiviteit in projectsturing en doelrealisatie significant toegenomen."
content = content.replace(old_covey_detail, new_covey_detail)

old_ruijters_detail = "Mijn grootste les uit de afgelopen jaren is dat ik mijn natuurlijke analytische kracht niet overboord hoef te gooien. Het gaat erom deze in balans te brengen met daadkracht. Binnen het Professionele Zelf frame betekent dit voor mij: analyseren om te begrijpen, maar beslissen om te versnellen. Deze balans stelt mij in staat om met meer zekerheid en minder stress door onzekere projectfases te navigeren."
new_ruijters_detail = "De belangrijkste bevinding van de afgelopen periode is dat analytisch vermogen een waardevol fundament blijft, mits dit adequaat wordt gebalanceerd met daadkracht. Binnen het Professionele Zelf frame vertaalt zich dit naar: analyseren ter begripsvorming, besluiten ter versnelling. Deze balans faciliteert een meer gecontroleerde en doelgerichte navigatie door complexe en onzekere projectfasen."
content = content.replace(old_ruijters_detail, new_ruijters_detail)

old_ikigai_detail = "Mijn professionele kompas. Dit model herinnert mij eraan dat ik op mijn best ben wanneer ik complexe theorieën kan vertalen naar praktische business oplossingen. Waar ik van hou (strategie en analyse) en waar ik goed in ben (conceptueel denken), komt samen met wat de wereld nodig heeft (heldere, onderbouwde adviezen) en waar ik voor betaald word (het creëren van commerciële waarde)."
new_ikigai_detail = "Het professionele kompas. Dit model illustreert dat maximale impact wordt gerealiseerd wanneer complexe theoretische kaders worden vertaald naar werkbare business-oplossingen. De intrinsieke motivatie (strategie en analyse) en kerncompetenties (conceptueel denken) komen hierbij samen met de marktvraag (gedegen, onderbouwd advies) en het verdienmodel (creatie van commerciële waarde)."
content = content.replace(old_ikigai_detail, new_ikigai_detail)

old_design_detail = "Ik pas Design Thinking toe om mijn neiging tot 'over-denken' tegen te gaan. In plaats van eindeloos plannen, dwingt dit model me om snel hypotheses te testen, feedback te verzamelen en iteratief te verbeteren. Het heeft me geleerd dat 'falen' in een vroege fase juist de meest waardevolle data oplevert voor een succesvol eindproduct."
new_design_detail = "De toepassing van Design Thinking fungeert als methodiek om langdurige analyse-fasen te doorbreken. Dit model structureert de noodzaak om aannames efficiënt te testen, feedback te integreren en iteratief te optimaliseren. De voornaamste uitkomst hiervan is het inzicht dat snelle validaties in een vroeg stadium de meest kritische data genereren voor een succesvol eindresultaat."
content = content.replace(old_design_detail, new_design_detail)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
