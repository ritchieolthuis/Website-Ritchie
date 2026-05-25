import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Chart Datasets
old_datasets = """                  datasets: [{
                      label: currentLang === 'en' ? 'Competence Score' : 'Competentie Score',
                      data: skillsData.map(s => s.score),
                      backgroundColor: 'rgba(204, 255, 0, 0.15)',
                      borderColor: '#ccff00',
                      borderWidth: 2,
                      pointBackgroundColor: skillsData.map(s => s.isWeak ? '#f43f5e' : '#ccff00'),
                      pointBorderColor: skillsData.map(s => s.isWeak ? '#f43f5e' : '#ccff00'),
                      pointRadius: 4,
                      pointHoverRadius: 6,
                  }]"""

new_datasets = """                  datasets: [
                      {
                          label: currentLang === 'en' ? 'Strong Points' : 'Sterke Punten',
                          data: skillsData.map(s => s.isWeak ? null : s.score),
                          backgroundColor: 'rgba(204, 255, 0, 0.1)',
                          borderColor: '#ccff00',
                          borderWidth: 2,
                          pointBackgroundColor: '#ccff00',
                          pointBorderColor: '#ccff00',
                          pointRadius: 4,
                          pointHoverRadius: 6,
                          spanGaps: true
                      },
                      {
                          label: currentLang === 'en' ? 'Improvement Points' : 'Verbeterpunten',
                          data: skillsData.map(s => s.isWeak ? s.score : null),
                          backgroundColor: 'rgba(244, 63, 94, 0.1)',
                          borderColor: '#f43f5e',
                          borderWidth: 2,
                          pointBackgroundColor: '#f43f5e',
                          pointBorderColor: '#f43f5e',
                          pointRadius: 4,
                          pointHoverRadius: 6,
                          spanGaps: true
                      }
                  ]"""
content = content.replace(old_datasets, new_datasets)

# 2. Update Ikigai Text (Dutch)
old_ikigai_nl = "ikigai_reflection: '<p>Wat vooral naar voren komt binnen mijn Ikigai, is dat ontwikkeling en uitdaging in vrijwel alle onderdelen centraal staan (zie figuur hierboven).</p><p>Energie haal ik voornamelijk uit situaties waarin strategisch en inhoudelijk denken wordt gecombineerd met verantwoordelijkheid en persoonlijke groei, wat direct in lijn ligt met mijn drijfveren (Ruijters, 2015).</p><p>Daarnaast is gebleken dat de grootste uitdaging ligt in het versnellen van de vertaalslag van ideeën en analyses naar concrete uitvoering. Dit sluit aan bij de noodzaak om proactief binnen mijn cirkel van invloed te handelen (Covey, 1989). De focus ligt hierbij op het versterken van besluitvaardigheid, adequaat handelen in onzekere situaties en het efficiënt omzetten van strategische inzichten naar resultaat.</p>',"

new_ikigai_nl = """ikigai_reflection: '<p>Als ik kijk naar wie ik ben gegroeid als persoon en professional, zie ik een duidelijke verschuiving in mijn manier van denken en doen. Waar ik in de eerste jaren de neiging had om alles kapot te analyseren voordat ik een stap zette, heb ik tijdens mijn projecten bij Vitens en Perron038 (Olthuis, 2026a; zie <button onclick="window.showSemesterPage(\\'jaar4\\')" class="text-accent hover:underline inline-block mx-1">Bijlage IV</button>) ervaren dat wachten op 100% zekerheid je simpelweg stilzet.</p><p>In lijn met het concept van <em>Design Thinking</em> (Brown, 2009), ben ik steeds iteratiever gaan werken. Dit was in het begin best oncomfortabel, omdat ik als persoon sterk hecht aan structuur en controle. Echter, door proactiever te opereren binnen mijn cirkel van invloed (Covey, 1989) heb ik geleerd om sneller knopen door te hakken. Dit gaf me de ruimte om daadwerkelijk verantwoordelijkheid te pakken en eigenaarschap te tonen in complexe uitdagingen, zoals ook gebleken is tijdens mijn recente afstudeeronderzoek (Olthuis, 2026b; zie <button onclick="window.showSemesterPage(\\'afstuderen\\')" class="text-accent hover:underline inline-block mx-1">Bijlage V</button>).</p><p>Mijn grootste les uit de afgelopen jaren is dat ik mijn natuurlijke analytische kracht niet overboord hoef te gooien. Het gaat om de balans: de analyse gebruiken als fundament, om van daaruit durf te tonen, keuzes te maken en daadkrachtig te handelen in een omgeving die continu verandert.</p>',"""
content = content.replace(old_ikigai_nl, new_ikigai_nl)

# 3. Update Ikigai Text (English)
old_ikigai_en = "ikigai_reflection: '<p>What stands out most within my Ikigai is that development and challenge are central to virtually all areas (see figure above).</p><p>I derive energy primarily from situations where strategic and substantive thinking are combined with responsibility and personal growth, which is directly in line with my core motivations (Ruijters, 2015).</p><p>It has become clear that the greatest challenge lies not in motivation or ambition, but in accelerating the translation of ideas and analyses into concrete execution. This connects to the necessity of acting proactively within my circle of influence (Covey, 1989). The focus is on strengthening decisiveness, acting swiftly amidst uncertainty, and efficiently converting insights into actionable results.</p>',"

new_ikigai_en = """ikigai_reflection: '<p>Looking at my growth as a person and professional, I see a clear shift in how I think and act. While I used to over-analyze everything before making a move, projects at Vitens and Perron038 (Olthuis, 2026a; see <button onclick="window.showSemesterPage(\\'jaar4\\')" class="text-accent hover:underline inline-block mx-1">Appendix IV</button>) taught me that waiting for 100% certainty simply brings you to a halt.</p><p>In line with the principles of <em>Design Thinking</em> (Brown, 2009), I have embraced a much more iterative approach. This was quite uncomfortable at first, as I naturally value structure and control. However, by operating more proactively within my circle of influence (Covey, 1989), I learned to make decisions faster. This gave me the freedom to take genuine responsibility and show ownership in complex challenges, which was clearly reflected during my recent graduation research (Olthuis, 2026b; see <button onclick="window.showSemesterPage(\\'afstuderen\\')" class="text-accent hover:underline inline-block mx-1">Appendix V</button>).</p><p>My biggest takeaway from the past years is that I don\\'t need to discard my natural analytical strengths. It is about balance: using analysis as a strong foundation, and from there, showing the courage to make choices and act decisively in a constantly changing environment.</p>',"""
content = content.replace(old_ikigai_en, new_ikigai_en)

# There is also an HTML div with id="ikigai-reflection" which has the default dutch text
old_html_ikigai = """<div class="text-zinc-300 text-sm leading-relaxed space-y-4 font-sans mb-4" id="ikigai-reflection" data-i18n="ikigai_reflection">
                            <p>Wat vooral naar voren komt binnen mijn Ikigai, is dat ontwikkeling en uitdaging in vrijwel alle onderdelen centraal staan (zie figuur hierboven).</p>
                            <p>Energie haal ik voornamelijk uit situaties waarin strategisch en inhoudelijk denken wordt gecombineerd met verantwoordelijkheid en persoonlijke groei, wat direct in lijn ligt met mijn drijfveren (Ruijters, 2015).</p>
                            <p>Daarnaast is gebleken dat de grootste uitdaging ligt in het versnellen van de vertaalslag van ideeën en analyses naar concrete uitvoering. Dit sluit aan bij de noodzaak om proactief binnen mijn cirkel van invloed te handelen (Covey, 1989). De focus ligt hierbij op het versterken van besluitvaardigheid, adequaat handelen in onzekere situaties en het efficiënt omzetten van strategische inzichten naar resultaat.</p>
                        </div>"""

new_html_ikigai = """<div class="text-zinc-300 text-sm leading-relaxed space-y-4 font-sans mb-4" id="ikigai-reflection" data-i18n="ikigai_reflection">
                            <p>Als ik kijk naar wie ik ben gegroeid als persoon en professional, zie ik een duidelijke verschuiving in mijn manier van denken en doen. Waar ik in de eerste jaren de neiging had om alles kapot te analyseren voordat ik een stap zette, heb ik tijdens mijn projecten bij Vitens en Perron038 (Olthuis, 2026a; zie <button onclick="window.showSemesterPage('jaar4')" class="text-accent hover:underline inline-block mx-1">Bijlage IV</button>) ervaren dat wachten op 100% zekerheid je simpelweg stilzet.</p>
                            <p>In lijn met het concept van <em>Design Thinking</em> (Brown, 2009), ben ik steeds iteratiever gaan werken. Dit was in het begin best oncomfortabel, omdat ik als persoon sterk hecht aan structuur en controle. Echter, door proactiever te opereren binnen mijn cirkel van invloed (Covey, 1989) heb ik geleerd om sneller knopen door te hakken. Dit gaf me de ruimte om daadwerkelijk verantwoordelijkheid te pakken en eigenaarschap te tonen in complexe uitdagingen, zoals ook gebleken is tijdens mijn recente afstudeeronderzoek (Olthuis, 2026b; zie <button onclick="window.showSemesterPage('afstuderen')" class="text-accent hover:underline inline-block mx-1">Bijlage V</button>).</p>
                            <p>Mijn grootste les uit de afgelopen jaren is dat ik mijn natuurlijke analytische kracht niet overboord hoef te gooien. Het gaat om de balans: de analyse gebruiken als fundament, om van daaruit durf te tonen, keuzes te maken en daadkrachtig te handelen in een omgeving die continu verandert.</p>
                        </div>"""
content = content.replace(old_html_ikigai, new_html_ikigai)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

