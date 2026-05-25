import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the chart datasets
old_chart = """                  datasets: [{
                      label: currentLang === 'en' ? 'Strong Points' : 'Sterke punten',
                      data: skillsData.map(s => !s.isWeak ? s.score : null),
                      backgroundColor: 'rgba(204, 255, 0, 0.2)',
                      borderColor: '#ccff00',
                      pointBackgroundColor: '#ccff00',
                      spanGaps: true
                  }, {
                      label: currentLang === 'en' ? 'Improvement Points' : 'Verbeterpunten',
                      data: skillsData.map(s => s.isWeak ? s.score : null),
                      backgroundColor: 'rgba(244, 63, 94, 0.2)',
                      borderColor: '#f43f5e',
                      pointBackgroundColor: '#f43f5e',
                      spanGaps: true
                  }]"""

new_chart = """                  datasets: [{
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

content = content.replace(old_chart, new_chart)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

