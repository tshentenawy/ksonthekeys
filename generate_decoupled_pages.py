import re
import os

project_dir = '/Users/tarekshentenawy/.gemini/antigravity/scratch/ksonthekeys/'

# Read index.html
with open(os.path.join(project_dir, 'index.html'), 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract top part (up to hero) from an existing subpage to get correct nav links
with open(os.path.join(project_dir, 'breakfast-buffet.html'), 'r', encoding='utf-8') as f:
    subpage_html = f.read()

top_match = re.search(r'(.*?)<section class="subpage-hero"', subpage_html, re.DOTALL)
top_content = top_match.group(1) if top_match else ''

bottom_match = re.search(r'(<!-- ══ ORDER CTA ══ -->.*)', subpage_html, re.DOTALL)
bottom_content = bottom_match.group(1) if bottom_match else ''

# Extract Event Spaces section from index.html
event_spaces_match = re.search(r'(<!-- ══ EVENT SPACES ══ -->.*?)(?=<!-- ══ CATERING ══ -->)', index_html, re.DOTALL)
event_spaces_content = event_spaces_match.group(1) if event_spaces_match else ''

# Extract Catering section from index.html
catering_match = re.search(r'(<!-- ══ CATERING ══ -->.*?)(?=<!-- ══ HOURS & INFO ══ -->)', index_html, re.DOTALL)
catering_content = catering_match.group(1) if catering_match else ''

# Add hero blocks to the extracted sections
event_spaces_full = f"""
  <section class="subpage-hero" aria-label="Event Spaces">
    <div class="subpage-hero-bg" style="background-image: url('images/events/grand-event-room-1.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Celebrate with us</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Event <em>Spaces</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Beautifully appointed private venues for 10 to 120+ guests.</p>
    </div>
  </section>
{event_spaces_content}
"""

catering_full = f"""
  <section class="subpage-hero" aria-label="Catering">
    <div class="subpage-hero-bg" style="background-image: url('images/events/grand-event-room-2.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Feast anywhere</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Event <em>Catering</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Custom menus and full service for your off-site or in-house events.</p>
    </div>
  </section>
{catering_content}
"""

# Write the new pages
with open(os.path.join(project_dir, 'event-spaces.html'), 'w', encoding='utf-8') as f:
    f.write(top_content + event_spaces_full + bottom_content)

with open(os.path.join(project_dir, 'catering.html'), 'w', encoding='utf-8') as f:
    f.write(top_content + catering_full + bottom_content)

# Now remove these blocks from index.html
new_index_html = index_html.replace(event_spaces_content, '')
new_index_html = new_index_html.replace(catering_content, '')

with open(os.path.join(project_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(new_index_html)

# Update nav links in all html files
html_files = [f for f in os.listdir(project_dir) if f.endswith('.html')]

for file in html_files:
    file_path = os.path.join(project_dir, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # In index.html, the anchors were #events and #catering.
    # In subpages, they were index.html#events and index.html#catering.
    content = content.replace('href="index.html#events"', 'href="event-spaces.html"')
    content = content.replace('href="index.html#catering"', 'href="catering.html"')
    content = content.replace('href="#events"', 'href="event-spaces.html"')
    content = content.replace('href="#catering"', 'href="catering.html"')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Decoupling complete!")
