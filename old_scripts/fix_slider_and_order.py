import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# --- Reorder Recommendations ---
# We know the markers:
# <!-- Rec 1 -->
# <!-- Rec 2 -->
# <!-- Rec 3: Antoinette Alma -->
# <!-- Rec 4: Elmar van Brakel -->
# <!-- Rec 5: Marcel Logtenberg -->
# <!-- Rec 6: Bas de Leve -->
# <!-- Rec 7: Martijn Olde Weghuis -->
# <!-- Rec 8: Eric Vredeveldt -->
# And the end of Rec 8 is where `</div>` for rec-track ends, which is before `</div>\n            </div>\n            \n            <!-- Skills & Certificates Section -->`

# Let's extract the blocks using split.
parts = content.split('<!-- Rec 1 -->')
before_rec1 = parts[0]
rest = parts[1]

# Split by other markers
markers = [
    '<!-- Rec 2 -->',
    '<!-- Rec 3: Antoinette Alma -->',
    '<!-- Rec 4: Elmar van Brakel -->',
    '<!-- Rec 5: Marcel Logtenberg -->',
    '<!-- Rec 6: Bas de Leve -->',
    '<!-- Rec 7: Martijn Olde Weghuis -->',
    '<!-- Rec 8: Eric Vredeveldt -->'
]

blocks = []
current_rest = rest
for marker in markers:
    p = current_rest.split(marker)
    blocks.append(p[0])
    current_rest = p[1]

# current_rest contains Rec 8 and the rest of the HTML.
# Where does Rec 8 end? Let's split by the closing of the `rec-track` which is followed by `</div>\n            </div>\n            \n            <!-- Skills & Certificates Section -->`
# Better: just find the first `</div>\n                </div>\n            </div>\n            \n            <!-- Skills & Certificates Section -->`
end_marker = '</div>\n                </div>\n            </div>\n            \n            <!-- Skills & Certificates Section -->'
# Actually, let's just split by the `<!-- Skills & Certificates Section -->` and backtrack.
end_split = current_rest.split('<!-- Skills & Certificates Section -->')
rec8_and_closing = end_split[0]
after_recs = '<!-- Skills & Certificates Section -->' + end_split[1]

# The end of Rec 8 is before the closing tags of the slider.
# Let's just use a simple regex to find the last </div> of the rec 8 card.
# The card ends with `</a>\n                        </div>`
# Let's split `rec8_and_closing` at the last `</div>\n                        </div>` or similar? No, `</a>\n                        </div>\n`
rec8_match = re.search(r'(.*</a>\s*</div>\s*)(</div>\s*</div>\s*</div>\s*)$', rec8_and_closing, re.DOTALL)
if rec8_match:
    blocks.append(rec8_match.group(1))
    closing_tags = rec8_match.group(2)
else:
    # If regex fails, let's just use string split
    rec8_parts = rec8_and_closing.rsplit('</div>', 3)
    blocks.append(rec8_parts[0] + '</div>')
    closing_tags = '</div>' + '</div>'.join(rec8_parts[1:])

# Now blocks contains the 8 recommendation blocks in order.
# blocks[0] = Rec 1
# blocks[1] = Rec 2
# blocks[2] = Rec 3
# blocks[3] = Rec 4
# blocks[4] = Rec 5
# blocks[5] = Rec 6
# blocks[6] = Rec 7
# blocks[7] = Rec 8

# Reorder: Eric(7), Martijn(6), Rec1(0)...
new_order = [
    '<!-- Rec 8: Eric Vredeveldt -->\n' + blocks[7],
    '<!-- Rec 7: Martijn Olde Weghuis -->\n' + blocks[6],
    '<!-- Rec 1 -->\n' + blocks[0],
    '<!-- Rec 2 -->\n' + blocks[1],
    '<!-- Rec 3: Antoinette Alma -->\n' + blocks[2],
    '<!-- Rec 4: Elmar van Brakel -->\n' + blocks[3],
    '<!-- Rec 5: Marcel Logtenberg -->\n' + blocks[4],
    '<!-- Rec 6: Bas de Leve -->\n' + blocks[5]
]

new_rec_track = "".join(new_order) + closing_tags

content = before_rec1 + new_rec_track + after_recs


# --- Update Projects Slider JS ---
old_proj_js = """      // Carousel Logic (Projects)
      const track = document.getElementById('carousel-track');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const slides = document.querySelectorAll('.project-slide');
      let currentIndex = 0;
      
      function updateCarousel() {
          const width = slides[0].offsetWidth; // Use offsetWidth for robust sizing
          track.style.transform = `translateX(-${currentIndex * width}px)`;
      }
      
      nextBtn.addEventListener('click', () => {
          currentIndex = (currentIndex + 1) % slides.length;
          updateCarousel();
      });
      
      prevBtn.addEventListener('click', () => {
          currentIndex = (currentIndex - 1 + slides.length) % slides.length;
          updateCarousel();
      });"""

new_proj_js = """      // Carousel Logic (Projects)
      const track = document.getElementById('carousel-track');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const slides = document.querySelectorAll('.project-slide');
      let currentIndex = 0;
      
      function updateCarousel() {
          if (!slides.length) return;
          const width = slides[0].offsetWidth; 
          track.style.transform = `translateX(-${currentIndex * width}px)`;
      }
      
      nextBtn.addEventListener('click', () => {
          if (!slides.length) return;
          const width = slides[0].offsetWidth;
          const containerWidth = track.parentElement.offsetWidth;
          const visibleItems = Math.round(containerWidth / width);
          const maxIndex = Math.max(0, slides.length - visibleItems);
          
          currentIndex++;
          if(currentIndex > maxIndex) {
            currentIndex = 0;
          }
          updateCarousel();
      });
      
      prevBtn.addEventListener('click', () => {
          if (!slides.length) return;
          const width = slides[0].offsetWidth;
          const containerWidth = track.parentElement.offsetWidth;
          const visibleItems = Math.round(containerWidth / width);
          const maxIndex = Math.max(0, slides.length - visibleItems);
          
          currentIndex--;
          if(currentIndex < 0) {
            currentIndex = maxIndex;
          }
          updateCarousel();
      });"""

content = content.replace(old_proj_js, new_proj_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

