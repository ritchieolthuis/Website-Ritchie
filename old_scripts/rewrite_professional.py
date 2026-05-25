import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CV / About Sectie
old_about = "Voor mij draait alles om het ontdekken van mogelijkheden in het onbekende en het vinden van oplossingen waar anderen vooral uitdagingen zien. Ik wil niet alleen het beste uit mezelf halen, maar ook uit de projecten waaraan ik werk. Ik combineer analytisch inzicht met de drive om daadwerkelijk verandering te realiseren. Of het nu gaat om het stroomlijnen van een proces of het neerzetten van een nieuwe commerciële propositie: ik geloof dat succes altijd een combinatie is van scherp nadenken en gewoon beginnen."

new_about = "Binnen mijn professionele ontwikkeling focus ik sterk op het identificeren van kansen binnen complexe vraagstukken en het formuleren van strategische oplossingen. De doelstelling is hierbij om niet alleen individuele kwaliteiten te benutten, maar de algehele projectkwaliteit te optimaliseren. Door analytisch inzicht te combineren met daadkracht, streef ik ernaar om tastbare veranderingen te realiseren. Of het nu gaat om procesoptimalisatie of de implementatie van een commerciële propositie: effectief resultaat vraagt om een doordachte analyse, gevolgd door een iteratieve uitvoering."

content = content.replace(old_about, new_about)

# 2. PDB Intro
old_pdb_intro = "Mijn reis begon met de overtuiging dat ik de overstap van mbo naar hbo succesvol wilde afronden"
new_pdb_intro = "Het startpunt van deze ontwikkeling vormde de transitie van het mbo naar het hbo, met als doel deze succesvol af te ronden"
content = content.replace(old_pdb_intro, new_pdb_intro)

old_pdb_quote1 = "\"Mijn ontwikkeling binnen dit frame draait om de transitie van een uitvoerende student naar een strategische denker die theorie koppelt aan praktijkwaarde.\""
new_pdb_quote1 = "De ontwikkeling binnen dit frame kenmerkt zich door de transitie van een uitvoerende rol naar die van een strategische denker, waarbij theorie direct wordt gekoppeld aan praktijkwaarde."
content = content.replace(old_pdb_quote1, new_pdb_quote1)

old_pdb_quote2 = "Mijn belangrijkste inzicht: Perfectie is de vijand van vooruitgang. Ik creëer de meeste waarde wanneer ik mijn drang naar controle loslaat en iteratief durf te werken."
new_pdb_quote2 = "Voornaamste inzicht: Perfectie mag vooruitgang niet in de weg staan. De meeste waarde wordt gecreëerd door de drang naar absolute controle los te laten ten gunste van een iteratieve, oplossingsgerichte werkwijze."
content = content.replace(old_pdb_quote2, new_pdb_quote2)

old_pdb_prof = "De keuze voor de universitaire pre-master ontstond vanuit een sterke drive om mezelf verder te ontwikkelen. Na de overstap van het mbo en twee jaar werken (deels tijdens corona), begon ik aan het hbo met twijfels of ik het niveau zou aankunnen. Toen ik in het eerste jaar mijn propedeuse behaalde, groeide mijn zelfvertrouwen aanzienlijk. Dit wakkerde de ambitie aan om mezelf verder uit te dagen en te ontdekken of een academische masteropleiding aan de Universiteit Twente bij mij zou passen."
new_pdb_prof = "De keuze voor de universitaire pre-master vloeide voort uit een structurele behoefte aan professionele en academische doorontwikkeling. Na de transitie vanuit het mbo en werkervaring in de praktijk, werd het hbo-traject gestart met een focus op competentie-opbouw. Het behalen van de propedeuse in het eerste jaar bevestigde het academisch potentieel. Dit vormde de katalysator voor de ambitie om het analytisch en strategisch denkniveau verder te toetsen en te vergroten middels een academische masteropleiding aan de Universiteit Twente."
content = content.replace(old_pdb_prof, new_pdb_prof)

old_pdb_prof_quote = "\"Mijn doel is om hierna door te stromen naar de master Business Administration. Deze richting sluit naadloos aan bij mijn interesses en biedt de strategische verdieping waar ik naar op zoek ben.\""
new_pdb_prof_quote = "Het uiteindelijke doel is de doorstroom naar de master Business Administration. Dit profiel sluit naadloos aan bij de strategische en analytische ambities en biedt de vereiste academische verdieping."
content = content.replace(old_pdb_prof_quote, new_pdb_prof_quote)

old_pdb_prof_end = "De overstap van het hbo naar het wetenschappelijk onderwijs (wo) vereiste wel aanpassingsvermogen, met name wat betreft tempo en academische zelfstandigheid. De inhoud was theoretisch zwaarder, maar met de juiste inzet en discipline goed te volgen. Ik heb deze periode ervaren als een ontzettend waardevolle stap, niet alleen als voorbereiding op de masteropleiding, maar ook voor mijn bredere persoonlijke en professionele ontwikkeling."
new_pdb_prof_end = "De transitie van het hbo naar het wetenschappelijk onderwijs (wo) vereiste een aanzienlijke mate van aanpassingsvermogen, specifiek inzake studietempo en academische zelfstandigheid. Hoewel de inhoud theoretisch complexer was, bleek deze met gerichte inzet en structuur goed te integreren. Deze academische voorbereidingsfase heeft zich bewezen als een cruciaal fundament, dienend voor zowel de aankomende masteropleiding als voor de bredere professionele ontwikkeling."
content = content.replace(old_pdb_prof_end, new_pdb_prof_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
