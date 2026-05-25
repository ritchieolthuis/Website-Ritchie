import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def do_replace(pattern, repl):
    global content
    content, count = re.subn(pattern, repl, content, count=1, flags=re.DOTALL)
    if count == 0:
        print(f"FAILED TO FIND PATTERN: {pattern[:50]}")
    return count

# 1. about_text_nl
do_replace(
    r'(about_text:\s*"Als vierdejaarsstudent Commerciële Economie aan Hogeschool Windesheim.*?de onderneming als de maatschappij\.")',
    'about_text: "Vierdejaarsstudent Commerciële Economie (Hogeschool Windesheim) met afgeronde minors in Bedrijfskunde (Pre-master Universiteit Twente) en Financiële Besluitvorming. Het profiel richt zich op kwantitatieve en kwalitatieve analyse, iteratief projectmanagement en datagedreven besluitvorming ter ondersteuning van bedrijfskundige vraagstukken.<br><br>De beroepspraktijk bestaat uit het analyseren van procesknelpunten en het implementeren van meetbare procesverbeteringen. De nadruk ligt op de toepassing van academische theorie in de commerciële praktijk om efficiëntie en bedrijfsresultaten te optimaliseren."'
)

# 2. pdb_intro
do_replace(
    r'(Om de professionele identiteit gestructureerd inzichtelijk te maken, wordt het model <em>Mijn Binnenste Buiten</em> \(Ruijters, 2015\) als analytisch kader gehanteerd\. Door de beroepsmatige ontwikkeling te duiden langs de vier frames, ontstaat een objectieve en onderbouwde reflectie op het gelopen groeiproces, de strategische keuzes en de professionele ambities\.)',
    'Ter verantwoording van de opgedane beroepscompetenties wordt het theoriemodel <em>Mijn Binnenste Buiten</em> (Ruijters, 2015) toegepast. Per frame (Institutioneel, Professioneel, Professionele Zelf, Persoonlijke Zelf) worden de gemaakte keuzes, projectresultaten en de resulterende competentieontwikkeling feitelijk onderbouwd aan de hand van de geproduceerde bewijsstukken.'
)

# 3. pdb_inst
do_replace(
    r'(Binnen de bacheloropleiding Commerciële Economie staat het creëren van waarde in een dynamische context centraal\. Het initiële vertrekpunt betrof de transitie van het mbo naar het hbo \(Olthuis, 2023; zie <button .*?>Bijlage I</button>\)\. Gedurende het curriculum fungeert de CE Skills Guide \(Windesheim, 2026; zie <a .*?>Bijlage VI</a>\) als structureel kompas voor competentie-ontwikkeling\. Binnen dit kader ligt de primaire focus op de kern-rubrics: Initiatief, Samenwerken, Verantwoordelijkheid \(Eigenaarschap\), Analytisch denken, Besluitvaardigheid en Iteratief werken \(Design Thinking\)\.)',
    r'De vooropleiding bestaat uit een afgeronde mbo-opleiding, gevolgd door de hbo-bachelor Commerciële Economie (Olthuis, 2023; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar1\'); setTimeout(() => document.getElementById(\'jaar1-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline inline-block mx-1">Bijlage I</button>). De meting van vaardigheden geschiedt volgens de beoordelingscriteria uit de CE Skills Guide (Windesheim, 2026; zie <a href="https://docs.google.com/spreadsheets/d/1XqhvW2usQ9FYD7Tye1TzObGUiBtvB9cJrIJR7dbGhWg/edit?usp=drive_link" target="_blank" class="text-accent hover:underline font-bold inline-block mx-1">Bijlage VI</a>). De competentieontwikkeling concentreert zich op de meetbare criteria: Initiatief, Samenwerken, Verantwoordelijkheid (Eigenaarschap), Analytisch denken, Besluitvaardigheid en Iteratief werken (Design Thinking).'
)

# 4. pdb_inst_quote
do_replace(
    r'("De kern van de ontwikkeling binnen het institutionele frame wordt gekenmerkt door de transitie van operationele uitvoering naar een strategisch denkniveau, waarbij theoretische concepten worden vertaald naar structurele praktijkwaarde\.")',
    '"De vereiste ontwikkeling binnen het institutionele frame bestaat uit de verschuiving van operationele taken (mbo-niveau) naar strategische analyse en advisering (hbo-niveau)."'
)

# 5. pdb_prof
do_replace(
    r'(Het professionele frame positioneert zich op het snijvlak van commerciële strategie en innovatie\. Beroepsproducten voor opdrachtgevers als <strong class="text-white">Unica</strong> \(Olthuis, 2024; zie <button .*?>Bijlage II</button>\) en <strong class="text-white">Vitens / Perron038</strong> \(Olthuis, 2026a; zie <button .*?>Bijlage IV</button>\) hebben de noodzaak onderstreept om fundamentele analyses te vertalen naar toepasbare business impact\. Deze aanpak rust op principes uit <em>Design Thinking</em> \(Brown, 2009\), waarbij de nadruk ligt op iteratief testen, valideren en bijsturen, ter voorkoming van stagnatie in de analytische ontwerpfase\.)',
    r'Binnen de beroepspraktijk zijn adviesrapporten en beroepsproducten opgeleverd voor opdrachtgevers waaronder <strong class="text-white">Unica</strong> (Olthuis, 2024; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar2\'); setTimeout(() => document.getElementById(\'jaar2-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline mx-1">Bijlage II</button>) en <strong class="text-white">Vitens / Perron038</strong> (Olthuis, 2026a; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar4\'); setTimeout(() => document.getElementById(\'jaar4-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline mx-1">Bijlage IV</button>). Uit de projectevaluaties blijkt dat lange theorie- en analysefasen leiden tot vertraging in de doorlooptijd. Derhalve is de methodiek <em>Design Thinking</em> (Brown, 2009) geïmplementeerd om projecten middels kortcyclische testen en frequente validatie iteratief op te leveren.'
)

# 6. pdb_prof_quote
do_replace(
    r'(<strong>Kritisch inzicht:</strong> Perfectie fungeert veelal als remmende factor op vooruitgang\. Optimale waardecreatie wordt gerealiseerd door rigide structuren gecontroleerd los te laten en iteratieve processen te omarmen\.)',
    '<strong>Kritisch inzicht:</strong> Het minimaliseren van de ontwikkeltijd per projectfase leidt tot snellere feedbackloops en een hogere implementatiegraad bij de opdrachtgever.'
)

# 7. covey_text
do_replace(
    r'(<p>In de beroepspraktijk blijkt een sterk gestructureerde en analytische inslag\. Waar deze focus op beheersing aanvankelijk leidde tot het centraal trekken van verantwoordelijkheden, heeft gestructureerde intervisie geresulteerd in een proactievere opstelling binnen de <strong class="text-accent">cirkel van invloed</strong>, inclusief de delegatie van taken naar samenwerkingspartners\.</p>\s*<p class="mt-2">Gedurende het pre-master traject \(Olthuis, 2025; zie <button .*?>Bijlage III</button>\) is besluitvaardigheid structureel versterkt door het versnellen van de vertaalslag van complexe data naar strategische keuzes\. Tevens is er een verhoogd bewustzijn gecreëerd omtrent de effectiviteit van constructieve samenwerking, waarbij actief luisteren en gerichte peer-feedback worden benut ter optimalisatie van teamresultaten\.</p>)',
    r'<p>Uit feedbackverslagen blijkt initieel een sterke neiging tot taaktoe-eigening (micromanagement) ter behoud van controle over de output. Door toepassing van theorie inzake de <strong class="text-accent">cirkel van invloed</strong> is dit structureel aangepast door actieve delegatie van taken aan groepsgenoten.</p>\n                                <p class="mt-2">Gedurende de pre-master (Olthuis, 2025; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar3\'); setTimeout(() => document.getElementById(\'jaar3-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage III</button>) resulteerde de verhoogde datacomplexiteit in de noodzaak om besluitvorming te versnellen. De toepassing van gestructureerde peer-feedback en functioneel overleg leidt tot aantoonbaar snellere besluitvaardigheid en efficiëntere teamsamenwerking.</p>'
)

# 8. ruijters_text
do_replace(
    r'(<p>De professionele identiteit vindt haar oorsprong in intrinsieke drijfveren, gekenmerkt door een sterke focus op persoonlijke ontwikkeling, de wil om maatschappelijke en commerciële impact te realiseren en het dragen van formele verantwoordelijkheden\. <strong>Flow</strong> ontstaat uitsluitend wanneer deze innerlijke overtuigingen structureel in balans zijn met de eisen vanuit de externe context\.</p>\s*<p class="mt-2">Deze optimale balans manifesteert zich actueel binnen het afstudeeronderzoek voor Axelio \(Olthuis, 2026b; zie <button .*?>Bijlage V</button>\), alwaar eigenaarschap direct wordt gekoppeld aan de uitvoering van strategische marktontwikkeling\.</p>)',
    r'<p>De arbeidsethos wordt empirisch bepaald door drie prestatie-indicatoren: de mate van kennisverwerving, de gerealiseerde output voor de opdrachtgever, en de toegewezen bevoegdheden. <strong>Flow</strong> treedt op wanneer taken een directe overlap vertonen met deze drie indicatoren.</p>\n                                <p class="mt-2">Deze overlap is feitelijk vastgesteld tijdens de uitvoering van het afstudeeronderzoek bij Axelio (Olthuis, 2026b; zie <button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'afstuderen\'); setTimeout(() => document.getElementById(\'afstuderen-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline font-bold inline-block">Bijlage V</button>). Hierbij wordt de bevoegdheid voor projectmanagement (eigenaarschap) toegepast voor het uitvoeren van kwantitatief en kwalitatief marktonderzoek.</p>'
)

# 9. dt_text
do_replace(
    r'(<p>Waar initiële processen gekenmerkt werden door intensieve theoretische analyses, hebben projectuitvoeringen bij Vitens en Perron038 aangetoond dat het streven naar absolute zekerheid veelal resulteert in processtagnatie \(<button .*?>Bijlage IV</button>\)\.</p>\s*<p class="mt-2">Conform de methodiek van <em>Design Thinking</em> is een transitie ingezet naar een iteratieve werkwijze\. Deze strategische verschuiving heeft geresulteerd in een vergrote handelingsruimte en de mogelijkheid om structureel eigenaarschap te tonen binnen complexe, ongestructureerde uitdagingen \(zie afstudeeronderzoek <button .*?>Bijlage V</button>\)\.</p>)',
    r'<p>Analyse van projectdoorlooptijden bij Vitens en Perron038 (<button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'jaar4\'); setTimeout(() => document.getElementById(\'jaar4-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline inline-block">Bijlage IV</button>) toont aan dat langdurige risicoanalyses de uitvoeringsfase vertragen.</p>\n                                    <p class="mt-2">De implementatie van <em>Design Thinking</em> reduceert deze ontwikkeltijd via kortcyclische opleveringen (iteraties). Dit stelt de onderzoeker in staat om projectrisico\'s sneller te identificeren en de projectsturing tijdig aan te passen, zoals gedocumenteerd in het afstudeeronderzoek (<button onclick="window.switchView(\'portfolio\'); window.showSemesterPage(\'afstuderen\'); setTimeout(() => document.getElementById(\'afstuderen-page\').scrollIntoView({behavior: \'smooth\'}), 100);" class="text-accent hover:underline inline-block">Bijlage V</button>).</p>'
)

# 10. ikigai_text
do_replace(
    r'(<p>Het overkoepelende inzicht uit het professionele leerproces stelt dat een natuurlijke, analytische dispositie niet verworpen dient te worden, maar effectiever moet worden ingezet\. Dit refereert direct aan de <strong>Ikigai balans</strong>: de analyse fungeert louter als robuust fundament\. Vanuit deze basis wordt overgegaan tot besluitvaardig en iteratief handelen binnen een dynamische organisatieomgeving\.</p>)',
    '<p>Conclusie uit portfolio-beoordelingen (semesters 1 t/m 8): Analytische vaardigheden dienen behouden te blijven, mits de urenbesteding aan theorievorming proportioneel blijft ten opzichte van de uitvoering. De <strong>Ikigai balans</strong> in de praktijk betekent: data verzamelen ter onderbouwing (theorie) en op basis van minimale vereisten direct overgaan tot besluitvorming (executie).</p>'
)

# 11. vpmc_ref1
do_replace(
    r'(De inschrijving voor het pre-master traject vloeide voort uit de ambitie om het analytisch kader fundamenteel te versterken\. Na een professionele transitie vanuit het mbo en een initiële onzekerheid omtrent het hbo-niveau, resulteerde het behalen van de propedeuse in het eerste jaar in de validatie van het academisch potentieel\. Deze prestatie katalyseerde het proces om te exploreren in hoeverre een strategische masteropleiding aan de Universiteit Twente aansluit bij de lange termijn doelstellingen\.)',
    'De keuze voor het WO pre-mastertraject was gericht op het aanleren van academische en statistische vaardigheden, als formele eis voor doorstroom naar de Masteropleiding. Het behalen van de hbo-propedeuse in 2023 diende hierbij als wettelijk verplicht toelatingsbewijs en indicator van academische haalbaarheid voor een WO-schakelprogramma.'
)

# 12. vpmc_quote
do_replace(
    r'("De primaire doelstelling behelst de succesvolle instroom in de Master Business Administration\. Deze disciplinaire focus correleert direct met het gekozen competentieprofiel en waarborgt de gewenste strategische en bedrijfskundige verdieping\.")',
    '"De doelstelling is instroom in de academische Master Business Administration. Het curriculum van deze opleiding faciliteert formele kennisverwerving op het gebied van strategisch en analytisch management."'
)

# 13. vpmc_ref2
do_replace(
    r'(De transitie naar het wetenschappelijk onderwijs \(wo\) legde een sterke nadruk op adaptief vermogen, in het bijzonder ten aanzien van informatieverwerking en academische onafhankelijkheid\. Hoewel de theoretische complexiteit evident was, bleek de leerstof met gestructureerde inzet en zelfmanagement goed behapbaar\. Het curriculum heeft substantieel bijgedragen aan de validatie van de wetenschappelijke potentie en vormt een robuuste basis voor verdere professionele academisering\.)',
    'Het academische niveau van de pre-master vereist een hogere dataverwerkingssnelheid en verminderde contacturen ten opzichte van het hbo. Door consequente urenregistratie en literatuurstudie bleek het curriculum qua studiebelasting (ECTS) haalbaar. De afgeronde VPMC-vakken (Wiskunde, Statistiek, Engels) voorzien in de vereiste kwantitatieve basis voor verdere bedrijfskundige theorievorming.'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
