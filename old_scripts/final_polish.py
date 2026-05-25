import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject Premium Custom Scrollbars and Selection Colors into the <style> tag
custom_styles = """
        /* Premium Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0a0a0a;
        }
        ::-webkit-scrollbar-thumb {
            background: #2a2a2a;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #CCFF00;
        }
        
        /* Premium Text Selection */
        ::selection {
            background-color: #CCFF00;
            color: #000;
        }
"""
content = content.replace('</style>', custom_styles + '\n    </style>')

# 2. Make timeline dots look more premium (filled or glowing)
# Right now they are: <div class="absolute -left-[41px] md:-left-[57px] top-8 w-5 h-5 rounded-full bg-[#121212] border-2 border-accent group-hover:bg-accent transition-colors z-10 shadow-[0_0_10px_rgba(204,255,0,0)] group-hover:shadow-[0_0_15px_rgba(204,255,0,0.5)]"></div>
# Let's add a permanent soft glow to them, and make sure they are aligned.
content = content.replace(
    'shadow-[0_0_10px_rgba(204,255,0,0)]',
    'shadow-[0_0_12px_rgba(204,255,0,0.2)]'
)

# 3. Enhance modal backdrop blur to make it look expensive
content = content.replace(
    'bg-black/80 backdrop-blur-sm',
    'bg-black/80 backdrop-blur-md'
)

# 4. Make sure all buttons have a smooth transform
content = content.replace(
    'hover:scale-105 transition-all',
    'hover:scale-105 transition-all duration-300 ease-out'
)

# 5. Fix any empty space in the portfolio grid by ensuring cards are beautifully spaced
content = content.replace(
    'space-y-16',
    'space-y-12 md:space-y-16' # Just to ensure it's responsive
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

