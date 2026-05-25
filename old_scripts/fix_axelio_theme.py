import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the axelio logo class to match theme but not invert (since text is already white)
new_css = """      .logo-white {
        filter: grayscale(100%) brightness(0) invert(1); 
        mix-blend-mode: screen; 
        opacity: 0.6;
        transition: opacity 0.3s ease;
      }
      .logo-white:hover {
        opacity: 1;
      }
      .logo-theme-fixed {
        filter: grayscale(100%);
        mix-blend-mode: screen;
        opacity: 0.6;
        transition: opacity 0.3s ease;
      }
      .logo-theme-fixed:hover {
        opacity: 1;
      }"""

content = content.replace("""      .logo-white {
        filter: grayscale(100%) brightness(0) invert(1); 
        mix-blend-mode: screen; 
        opacity: 0.6;
        transition: opacity 0.3s ease;
      }
      .logo-white:hover {
        opacity: 1;
      }""", new_css)

content = content.replace('src="assets/axelio_white_text.png" alt="Axelio" class="h-14 w-auto object-contain opacity-60 hover:opacity-100 transition-opacity duration-300 mix-blend-screen"',
                          'src="assets/axelio_white_text.png" alt="Axelio" class="h-14 w-auto object-contain logo-theme-fixed"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

