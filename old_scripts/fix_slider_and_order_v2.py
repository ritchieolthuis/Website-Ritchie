import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reorder Recommendations
# The track starts with `id="rec-track"` and `<!-- Rec 1 -->`
# Let's extract the Rec 7 block and Rec 8 block.
rec7_pattern = r'(<!-- Rec 7: Martijn Olde Weghuis -->.*?)(?=<!-- Rec 8: Eric Vredeveldt -->)'
rec7_match = re.search(rec7_pattern, content, re.DOTALL)
rec7_content = rec7_match.group(1) if rec7_match else ''

# Rec 8 is from `<!-- Rec 8: Eric Vredeveldt -->` to `</a>\n                        </div>` right before the end of rec-track.
rec8_pattern = r'(<!-- Rec 8: Eric Vredeveldt -->.*?</a>\s*</div>)'
rec8_match = re.search(rec8_pattern, content, re.DOTALL)
rec8_content = rec8_match.group(1) if rec8_match else ''

if rec7_content and rec8_content:
    # Remove them from the original location
    content = content.replace(rec7_content, '')
    content = content.replace(rec8_content, '')
    
    # Insert them before Rec 1
    content = content.replace('<!-- Rec 1 -->', rec8_content + '\n                        ' + rec7_content + '\n                        <!-- Rec 1 -->')


# Fix Project Slider JS
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

