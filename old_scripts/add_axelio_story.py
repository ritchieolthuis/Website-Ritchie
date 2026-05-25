import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_paragraph = """                                <p class="text-zinc-300 text-base leading-relaxed mb-4">
                                    Onderzoek naar de UK-aardappelmarkt, inclusief ketencomplexiteit, ERP-landschappen, operationele pijnpunten en koopcriteria. Via deskresearch en diepte-interviews met experts in Engeland, Schotland, Noord-Ierland en Wales werd de segmentfit voor Agrio geanalyseerd.
                                </p>"""

new_paragraph = """                                <p class="text-zinc-300 text-base leading-relaxed mb-4">
                                    Onderzoek naar de UK-aardappelmarkt, inclusief ketencomplexiteit, ERP-landschappen, operationele pijnpunten en koopcriteria. In eerste instantie had ik een uitgebreide vragenlijst opgesteld op basis van vier hoofdcriteria: (1) bedrijven & activiteiten, (2) ERP & automatisering, (3) de klant, ketenintegratie & pijnpunten, en (4) partners & concurrenten. 
                                </p>
                                <p class="text-zinc-300 text-base leading-relaxed mb-4">
                                    Tijdens het proces kwam ik er echter achter dat deze aanpak in de praktijk niet werkte. Het was exact het hoogseizoen voor de Britse aardappelsector, waardoor handelshuizen en verwerkers simpelweg geen tijd hadden. Ik probeerde cold-calling, maar kwam er niet doorheen en niemand kon mij helpen. 
                                </p>
                                <p class="text-zinc-300 text-base leading-relaxed mb-4">
                                    Om te anticiperen op deze situatie, heb ik mijn strategie radicaal aangepast. Ik heb de kernvragen omgebouwd tot een toegankelijke enquête en vervolgens bijna 700 e-mails uitgestuurd. Deze proactieve aanpak wierp zijn vruchten af: door de gerichte e-mails kreeg ik alsnog volop reacties en input op mijn vragenlijst. Nog belangrijker was dat dit de deuren opende voor verdieping; hierdoor heb ik alsnog een reeks waardevolle diepte-interviews met experts kunnen afnemen.
                                </p>"""

content = content.replace(old_paragraph, new_paragraph)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

