import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def do_replace(pattern, repl):
    global content
    content, count = re.subn(pattern, repl, content, count=1, flags=re.DOTALL)
    return count

# 1. about_text_nl
count = do_replace(
    r'(about_text:\s*"Ik ben een ambitieuze vierdejaarsstudent.*?wereld om ons heen\.")',
    'about_text: "Als vierdejaarsstudent Commerciële Economie aan Hogeschool Windesheim, gespecialiseerd in mensgericht ontwerp en innovatieprocessen, combineer ik een stevig analytisch fundament met iteratieve daadkracht. Naast de bachelor zijn competenties verdiept middels minors in Bedrijfskunde (Pre-master) en Financiële Besluitvorming.<br><br>Binnen professionele contexten ligt de focus op het transformeren van complexe uitdagingen naar strategische kansen. Het doel is hierbij om organisaties te faciliteren in datagedreven en weloverwogen besluitvorming, waardoor duurzame en betekenisvolle impact wordt gerealiseerd voor zowel de onderneming als de maatschappij."'
)
print("about_text_nl:", count)

# 2. pdb_intro
count = do_replace(
    r'(Om mijn professionele identiteit als student Commerciële Economie inzichtelijk te maken, maak ik gebruik van het model <em>Mijn Binnenste Buiten</em> van Manon Ruijters \(2015\)\. Door mijn ontwikkeling binnen de vier frames te beschrijven, geef ik een onderbouwde reflectie op mijn groei, keuzes en ambities\.)',
    'Om de professionele identiteit gestructureerd inzichtelijk te maken, wordt het model <em>Mijn Binnenste Buiten</em> (Ruijters, 2015) als analytisch kader gehanteerd. Door de beroepsmatige ontwikkeling te duiden langs de vier frames, ontstaat een objectieve en onderbouwde reflectie op het gelopen groeiproces, de strategische keuzes en de professionele ambities.'
)
print("pdb_intro:", count)

# 3. pdb_inst
count = do_replace(
    r'(Binnen de opleiding Commerciële Economie aan Windesheim leer ik waarde te creëren in een omgeving die voortdurend verandert\. Mijn reis begon met de overtuiging dat ik de overstap van mbo naar hbo succesvol wilde afronden \(Olthuis, 2023; zie <button .*?>Bijlage I</button>\)\. De CE Skills Guide \(Windesheim, 2026; zie <a .*?>Bijlage VI</a>\) vormt hierbij een belangrijk kompas om te reflecteren op mijn vaardigheden\. Van de zestien vaardigheden focus ik mij met name op de kern-rubrics: Initiatief, Samenwerken, Verantwoordelijkheid \(Eigenaarschap\), Analytisch denken, Besluitvaardigheid en Iteratief werken \(Design Thinking\)\.)',
    r'Binnen de bacheloropleiding Commerciële Economie staat het creëren van waarde in een dynamische context centraal. Het initiële vertrekpunt betrof de transitie van het mbo naar het hbo (Olthuis, 2023; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar1\'); setTimeout(() => document.getElementById(\'jaar1-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>). Gedurende het curriculum fungeert de CE Skills Guide (Windesheim, 2026; zie <a href="https://docs.google.com/spreadsheets/d/1XqhvW2usQ9FYD7Tye1TzObGUiBtvB9cJrIJR7dbGhWg/edit?usp=drive_link" target="_blank" class="text-accent hover:underline font-bold inline-block mx-1">Bijlage VI</a>) als structureel kompas voor competentie-ontwikkeling. Binnen dit kader ligt de primaire focus op de kern-rubrics: Initiatief, Samenwerken, Verantwoordelijkheid (Eigenaarschap), Analytisch denken, Besluitvaardigheid en Iteratief werken (Design Thinking).'
)
print("pdb_inst:", count)

# 4. pdb_inst_quote
count = do_replace(
    r'("Mijn ontwikkeling binnen dit frame draait om de transitie van een uitvoerende student naar een strategische denker die theorie koppelt aan praktijkwaarde\.")',
    '"De kern van de ontwikkeling binnen het institutionele frame wordt gekenmerkt door de transitie van operationele uitvoering naar een strategisch denkniveau, waarbij theoretische concepten worden vertaald naar structurele praktijkwaarde."'
)
print("pdb_inst_quote:", count)

# 5. pdb_prof
count = do_replace(
    r'(Mijn professionele frame richt zich op het snijvlak van commerciële strategie en innovatie\. Tijdens projecten zoals <strong class="text-white">Unica</strong> \(Olthuis, 2024; zie <button .*?>Bijlage II</button>\) en <strong class="text-white">Vitens / Perron038</strong> \(Olthuis, 2026a; zie <button .*?>Bijlage IV</button>\) heb ik ervaren hoe cruciaal het is om analytisch denken om te zetten in concrete business impact\. Hierbij hanteer ik principes uit <em>Design Thinking</em> \(Brown, 2009\): sneller testen, valideren en bijsturen in plaats van te blijven hangen in de ontwerpfase\.)',
    r'Het professionele frame positioneert zich op het snijvlak van commerciële strategie en innovatie. Beroepsproducten voor opdrachtgevers als <strong class="text-white">Unica</strong> (Olthuis, 2024; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar2\'); setTimeout(() => document.getElementById(\'jaar2-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline mx-1">Bijlage II</button>) en <strong class="text-white">Vitens / Perron038</strong> (Olthuis, 2026a; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar4\'); setTimeout(() => document.getElementById(\'jaar4-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline mx-1">Bijlage IV</button>) hebben de noodzaak onderstreept om fundamentele analyses te vertalen naar toepasbare business impact. Deze aanpak rust op principes uit <em>Design Thinking</em> (Brown, 2009), waarbij de nadruk ligt op iteratief testen, valideren en bijsturen, ter voorkoming van stagnatie in de analytische ontwerpfase.'
)
print("pdb_prof:", count)

# 6. pdb_prof_quote
count = do_replace(
    r'(<strong>Mijn belangrijkste inzicht:</strong> Perfectie is de vijand van vooruitgang\. Ik creëer de meeste waarde wanneer ik mijn drang naar controle loslaat en iteratief durf te werken\.)',
    '<strong>Kritisch inzicht:</strong> Perfectie fungeert veelal als remmende factor op vooruitgang. Optimale waardecreatie wordt gerealiseerd door rigide structuren gecontroleerd los te laten en iteratieve processen te omarmen.'
)
print("pdb_prof_quote:", count)

# 7. covey_text
count = do_replace(
    r'(<p>In de praktijk ben ik een initiatiefrijke, analytische en gestructureerde professional\. Omdat ik hoog scoor op controle, had ik in het verleden de neiging om verantwoordelijkheid volledig naar me toe te trekken\. Door intervisie heb ik geleerd om proactiever binnen mijn <strong class="text-accent">cirkel van invloed</strong> te handelen en meer ruimte te geven aan anderen\.</p>\s*<p class="mt-2">Tijdens de pre-master \(Olthuis, 2025; zie <button .*?>Bijlage III</button>\) heb ik mijn besluitvaardigheid versterkt door complexe data sneller te vertalen naar keuzes\. Ik ben me bewuster geworden van constructief samenwerken: actief luisteren en kritische peer-feedback benutten om gezamenlijke output in teamsessies naar een hoger niveau te tillen\.</p>)',
    r'<p>In de beroepspraktijk blijkt een sterk gestructureerde en analytische inslag. Waar deze focus op beheersing aanvankelijk leidde tot het centraal trekken van verantwoordelijkheden, heeft gestructureerde intervisie geresulteerd in een proactievere opstelling binnen de <strong class="text-accent">cirkel van invloed</strong>, inclusief de delegatie van taken naar samenwerkingspartners.</p>\n                                <p class="mt-2">Gedurende het pre-master traject (Olthuis, 2025; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar3\'); setTimeout(() => document.getElementById(\'jaar3-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage III</button>) is besluitvaardigheid structureel versterkt door het versnellen van de vertaalslag van complexe data naar strategische keuzes. Tevens is er een verhoogd bewustzijn gecreëerd omtrent de effectiviteit van constructieve samenwerking, waarbij actief luisteren en gerichte peer-feedback worden benut ter optimalisatie van teamresultaten.</p>'
)
print("covey_text:", count)

# 8. ruijters_text
count = do_replace(
    r'(<p>Wie ik ben als professional, is diep geworteld in mijn persoonlijke drijfveren: de wil om te ontwikkelen, impact te maken en verantwoordelijkheid te dragen\. Er is pas sprake van <strong>flow</strong> wanneer deze innerlijke waarden in balans zijn met de externe context\.</p>\s*<p class="mt-2">Deze balans \(flow\) komt voor mij momenteel het sterkst naar voren in mijn afstudeeronderzoek voor Axelio \(Olthuis, 2026b; zie <button .*?>Bijlage V</button>\), waar ik eigenaarschap combineer met strategische marktontwikkeling\.</p>)',
    r'<p>De professionele identiteit vindt haar oorsprong in intrinsieke drijfveren, gekenmerkt door een sterke focus op persoonlijke ontwikkeling, de wil om maatschappelijke en commerciële impact te realiseren en het dragen van formele verantwoordelijkheden. <strong>Flow</strong> ontstaat uitsluitend wanneer deze innerlijke overtuigingen structureel in balans zijn met de eisen vanuit de externe context.</p>\n                                <p class="mt-2">Deze optimale balans manifesteert zich actueel binnen het afstudeeronderzoek voor Axelio (Olthuis, 2026b; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'afstuderen\'); setTimeout(() => document.getElementById(\'afstuderen-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage V</button>), alwaar eigenaarschap direct wordt gekoppeld aan de uitvoering van strategische marktontwikkeling.</p>'
)
print("ruijters_text:", count)

# 9. dt_text
count = do_replace(
    r'(<p>Waar ik in de eerste jaren de neiging had om alles kapot te analyseren, heb ik tijdens mijn projecten bij Vitens en Perron038 ervaren dat wachten op 100% zekerheid je simpelweg stilzet \(<button .*?>Bijlage IV</button>\)\.</p>\s*<p class="mt-2">In lijn met <em>Design Thinking</em> ben ik steeds iteratiever gaan werken\. Dit gaf me de ruimte om daadwerkelijk verantwoordelijkheid te pakken en eigenaarschap te tonen in complexe uitdagingen \(zie afstudeeronderzoek <button .*?>Bijlage V</button>\)\.</p>)',
    r'<p>Waar initiële processen gekenmerkt werden door intensieve theoretische analyses, hebben projectuitvoeringen bij Vitens en Perron038 aangetoond dat het streven naar absolute zekerheid veelal resulteert in processtagnatie (<button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar4\'); setTimeout(() => document.getElementById(\'jaar4-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline inline-block">Bijlage IV</button>).</p>\n                                    <p class="mt-2">Conform de methodiek van <em>Design Thinking</em> is een transitie ingezet naar een iteratieve werkwijze. Deze strategische verschuiving heeft geresulteerd in een vergrote handelingsruimte en de mogelijkheid om structureel eigenaarschap te tonen binnen complexe, ongestructureerde uitdagingen (zie afstudeeronderzoek <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'afstuderen\'); setTimeout(() => document.getElementById(\'afstuderen-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline inline-block">Bijlage V</button>).</p>'
)
print("dt_text:", count)

# 10. ikigai_text
count = do_replace(
    r'(<p>Mijn grootste les uit de afgelopen jaren is dat ik mijn natuurlijke analytische kracht niet overboord hoef te gooien\. Het gaat om de <strong>Ikigai balans</strong>: de analyse gebruiken als fundament, om van daaruit durf te tonen, keuzes te maken en daadkrachtig te handelen in een omgeving die continu verandert\.</p>)',
    '<p>Het overkoepelende inzicht uit het professionele leerproces stelt dat een natuurlijke, analytische dispositie niet verworpen dient te worden, maar effectiever moet worden ingezet. Dit refereert direct aan de <strong>Ikigai balans</strong>: de analyse fungeert louter als robuust fundament. Vanuit deze basis wordt overgegaan tot besluitvaardig en iteratief handelen binnen een dynamische organisatieomgeving.</p>'
)
print("ikigai_text:", count)

# 11. vpmc_ref1
count = do_replace(
    r'(De keuze voor de universitaire pre-master ontstond vanuit een sterke drive om mezelf verder te ontwikkelen\. Na de overstap van het mbo en twee jaar werken \(deels tijdens corona\), begon ik aan het hbo met twijfels of ik het niveau zou aankunnen\. Toen ik in het eerste jaar mijn propedeuse behaalde, groeide mijn zelfvertrouwen aanzienlijk\. Dit wakkerde de ambitie aan om mezelf verder uit te dagen en te ontdekken of een academische masteropleiding aan de Universiteit Twente bij mij zou passen\.)',
    'De inschrijving voor het pre-master traject vloeide voort uit de ambitie om het analytisch kader fundamenteel te versterken. Na een professionele transitie vanuit het mbo en een initiële onzekerheid omtrent het hbo-niveau, resulteerde het behalen van de propedeuse in het eerste jaar in de validatie van het academisch potentieel. Deze prestatie katalyseerde het proces om te exploreren in hoeverre een strategische masteropleiding aan de Universiteit Twente aansluit bij de lange termijn doelstellingen.'
)
print("vpmc_ref1:", count)

# 12. vpmc_quote
count = do_replace(
    r'("Mijn doel is om hierna door te stromen naar de master Business Administration\. Deze richting sluit naadloos aan bij mijn interesses en biedt de strategische verdieping waar ik naar op zoek ben\.")',
    '"De primaire doelstelling behelst de succesvolle instroom in de Master Business Administration. Deze disciplinaire focus correleert direct met het gekozen competentieprofiel en waarborgt de gewenste strategische en bedrijfskundige verdieping."'
)
print("vpmc_quote:", count)

# 13. vpmc_ref2
count = do_replace(
    r'(De overstap van het hbo naar het wetenschappelijk onderwijs \(wo\) vereiste wel aanpassingsvermogen, met name wat betreft tempo en academische zelfstandigheid\. De inhoud was theoretisch zwaarder, maar met de juiste inzet en discipline goed te volgen\. Ik heb deze periode ervaren als een ontzettend waardevolle stap, niet alleen als voorbereiding op de masteropleiding, maar ook voor mijn bredere persoonlijke en professionele ontwikkeling\.)',
    'De transitie naar het wetenschappelijk onderwijs (wo) legde een sterke nadruk op adaptief vermogen, in het bijzonder ten aanzien van informatieverwerking en academische onafhankelijkheid. Hoewel de theoretische complexiteit evident was, bleek de leerstof met gestructureerde inzet en zelfmanagement goed behapbaar. Het curriculum heeft substantieel bijgedragen aan de validatie van de wetenschappelijke potentie en vormt een robuuste basis voor verdere professionele academisering.'
)
print("vpmc_ref2:", count)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

