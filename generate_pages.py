import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract top part (up to hero)
top_match = re.search(r'(.*?)<!-- ══ HERO ══ -->', html, re.DOTALL)
top_content = top_match.group(1) if top_match else ''

# Extract bottom part (from CTA banner to end)
bottom_match = re.search(r'(<!-- ══ ORDER CTA ══ -->.*)', html, re.DOTALL)
bottom_content = bottom_match.group(1) if bottom_match else ''

# Replace # links with index.html# in the top_content
# e.g., href="#about" -> href="index.html#about"
for anchor in ['about', 'menu', 'events', 'catering', 'faq']:
    top_content = top_content.replace(f'href="#{anchor}"', f'href="index.html#{anchor}"')
    
# Replace external links with local links
link_replacements = {
    'https://www.ksonthekeys.com/breakfast-buffet': 'breakfast-buffet.html',
    'https://www.ksonthekeys.com/brunch-buffet': 'brunch-buffet.html',
    'https://www.ksonthekeys.com/dailyspecials': 'dailyspecials.html',
    'https://www.ksonthekeys.com/corporate-events': 'private-events.html',
    'https://www.ksonthekeys.com/nonprofits': 'nonprofits.html',
    'https://www.ksonthekeys.com/delivery': 'delivery.html',
    'https://www.ksonthekeys.com/upcoming-events': 'upcoming-events.html',
    'https://www.ksonthekeys.com/large-group-events': 'private-events.html',
    'https://www.ksonthekeys.com/more-than-10': 'private-events.html'
}

for old, new in link_replacements.items():
    top_content = top_content.replace(old, new)
    bottom_content = bottom_content.replace(old, new)

# Write breakfast buffet
breakfast_main = """
  <section class="subpage-hero" aria-label="Breakfast Buffet">
    <div class="subpage-hero-bg" style="background-image: url('images/brunch/brunch-7.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Weekend Mornings</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Breakfast <em>Buffet</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Ottawa's favourite Saturday and Sunday breakfast. Omelettes, waffles, pancakes, eggs benedict & more.</p>
    </div>
  </section>

  <section class="subpage-content">
    <div class="container fade-in">
      <div class="document-content">
        <div style="text-align: center; margin-bottom: 40px;">
          <h2 style="font-family: var(--font-serif); font-size: 2rem; color: var(--burgundy-dark); margin-bottom: 8px;">Weekend Breakfast Buffet</h2>
          <p style="color: var(--text-mid);">Every Saturday from 10:00am–2:00pm<br>Sunday from 9:00am–2:30pm</p>
        </div>

        <div class="pricing-block">
          <h4>Buffet Pricing</h4>
          <ul style="list-style: none; padding: 0; margin: 0;">
            <li><strong>Adults:</strong> $22.95</li>
            <li><strong>Seniors (65 and older):</strong> $19.95</li>
            <li><strong>Kids under 12 years old:</strong> $14.95</li>
          </ul>
        </div>

        <h3>Traditional Breakfast Items</h3>
        <p>Omelettes made to order, scrambled eggs, eggs benedict, hard boiled eggs, bacon, sausage, toast, home fries, hash browns, breakfast pastries, yogurt, muffins, croissants.</p>

        <h3>Waffle / Pancake / Crepe Station</h3>
        <p>Waffles, pancakes, crepes, French toast, English cream, banana slices, mixed berries, chocolate sauce, syrup, jams, and honey.</p>

        <h3>Dessert Station</h3>
        <p>Fruit, dessert squares, cream pie, jello, pudding, cinnamon balls, cookies, ice cream.</p>

        <h3>Beverages</h3>
        <p>Coffee, tea, juice, and pop are included with your buffet.</p>
        
        <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 40px;">
          <em>Note: Prices and food selection are subject to change without notice. Please note, if you are still eating your Breakfast buffet while the Brunch buffet begins, you are welcome to enjoy the Brunch items, however, the Brunch prices will apply.</em>
        </p>

        <div style="text-align: center; margin-top: 48px;">
          <a href="https://www.tbdine.com/book/restaurant/ks-on-the-keys-restaurant?idApp=69099&language=en-us" target="_blank" class="btn btn-primary btn-lg">Book Your Table</a>
        </div>
      </div>
    </div>
  </section>
"""
with open('breakfast-buffet.html', 'w', encoding='utf-8') as f:
    f.write(top_content + breakfast_main + bottom_content)

# Write brunch buffet
brunch_main = """
  <section class="subpage-hero" aria-label="Sunday Brunch Buffet">
    <div class="subpage-hero-bg" style="background-image: url('images/brunch/brunch-1.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Sunday Special</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Sunday <em>Brunch</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Ottawa's favourite Sunday brunch buffet. Full hot spread, waffles, General Tso chicken, Lebanese mezza & more.</p>
    </div>
  </section>

  <section class="subpage-content">
    <div class="container fade-in">
      <div class="document-content">
        <div style="text-align: center; margin-bottom: 40px;">
          <h2 style="font-family: var(--font-serif); font-size: 2rem; color: var(--burgundy-dark); margin-bottom: 8px;">Signature Sunday Brunch</h2>
          <p style="color: var(--text-mid);">Every Sunday from 10:30am–2:30pm</p>
          <p style="font-style: italic; color: var(--text-light); font-size: 0.95rem;">"If breakfast is the most important meal of the day, then brunch is the most important meal of the week... come try our Sunday Brunch."</p>
        </div>

        <div class="pricing-block">
          <h4>Buffet Pricing</h4>
          <ul style="list-style: none; padding: 0; margin: 0;">
            <li><strong>Adults:</strong> $32.95</li>
            <li><strong>Seniors (65 and older):</strong> $26.95</li>
            <li><strong>Kids under 12 years old:</strong> $16.95</li>
          </ul>
        </div>

        <h3>Traditional Breakfast Items</h3>
        <p>Omelettes made to order, scrambled eggs, eggs benedict, bacon, sausage, toast, home fries, hash browns, fruit, breakfast pastries, muffins, croissants.</p>

        <h3>Waffle / Pancake / Crepe Station</h3>
        <p>Waffles, pancakes, crepes, French toast, English cream, mixed berries, chocolate sauce, syrup, and jams.</p>

        <h3>Hot Brunch Station</h3>
        <p>Meat loaf, Chicken Florentine, assorted pizza, chicken Marsala, rice pilaf, General Tso chicken, vegetable fried rice, eggrolls, spring rolls, lasagna, swedish meatballs, penne cream sauce, chicken kabobs, potatoes, stuffed grape leaf rolls, hummus, chicken wings, steamed vegetables.</p>

        <h3>Cold Buffet & Lebanese Station</h3>
        <p>A variety of cold salads, Lebanese zaatar pies and cheese pies.</p>

        <h3>Dessert Station</h3>
        <p>Dessert squares, cake, cookies, Jello, pudding, fruit & ice cream.</p>

        <h3>Beverages</h3>
        <p>Coffee, tea, juice, and pop are included with your buffet.</p>

        <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 40px;">
          <em>Note: Prices and food selection are subject to change without notice. Please note, if you are still eating your Breakfast buffet while the Brunch buffet begins, you are welcome to enjoy the Brunch items, however, the Brunch prices will apply.</em>
        </p>

        <div style="text-align: center; margin-top: 48px;">
          <a href="https://www.tbdine.com/book/restaurant/ks-on-the-keys-restaurant?idApp=69099&language=en-us" target="_blank" class="btn btn-primary btn-lg">Book Your Table</a>
        </div>
      </div>
    </div>
  </section>
"""
with open('brunch-buffet.html', 'w', encoding='utf-8') as f:
    f.write(top_content + brunch_main + bottom_content)

print("Created breakfast-buffet.html and brunch-buffet.html")
