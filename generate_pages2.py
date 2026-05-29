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

# Write dailyspecials
dailyspecials_main = """
  <section class="subpage-hero" aria-label="Daily Specials">
    <div class="subpage-hero-bg" style="background-image: url('images/food/food-10.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Fresh Every Day</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Daily <em>Specials</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Wing Wednesday, Wine & Pasta Thursday, Late Night Appies. Make your cravings count.</p>
    </div>
  </section>

  <section class="subpage-content">
    <div class="container fade-in">
      <div class="document-content">
        <p style="font-size: 1.1rem; color: var(--text-mid); text-align: center; margin-bottom: 40px;">At KS on the Keys, we believe your cravings should never have to wait for the weekend. That’s why we’re serving up daily specials that bring the flavour, value, and fun every time you visit.</p>

        <div class="pricing-block" style="border-color: #df4759;">
          <h4 style="color: #df4759;">Asian Night & $6 Draft Beers</h4>
          <p style="margin:0;">Enjoy 2 Egg Rolls or Spring Rolls <strong>FREE</strong> with any Asian dish.<br>Sip on $6 14oz Draft Beers all evening.</p>
        </div>

        <div class="pricing-block" style="border-color: #e67e22;">
          <h4 style="color: #e67e22;">Wing Wednesday</h4>
          <p style="margin:0;">The midweek MVP. Just <strong>$1 per wing</strong> (minimum 5 wings) + $6 bar rail drinks.</p>
        </div>

        <div class="pricing-block" style="border-color: var(--burgundy);">
          <h4 style="color: var(--burgundy);">Wine & Pasta Thursday</h4>
          <p style="margin:0; margin-bottom: 12px;">It’s carbs and cabernet. Perfect for date night or a night out with your crew.</p>
          <ul style="margin:0;">
            <li>25% Off all pasta dishes</li>
            <li>½ Price bottles of wine</li>
          </ul>
        </div>

        <div class="pricing-block" style="border-color: #2ecc71;">
          <h4 style="color: #2ecc71;">Late Night (After 8PM)</h4>
          <p style="margin:0;">Unwind your week with our crowd-favorite snacks and sips. <strong>25% Off Select Appetizers and Drinks</strong> (Think: Thai Bites, Zucchini Sticks, Breaded Shrimp, and more – includes alcohol and mocktails.)</p>
        </div>

        <div class="pricing-block" style="border-color: var(--gold);">
          <h4 style="color: var(--gold-dark);">Breakfast Savings</h4>
          <p style="margin:0;"><strong>15% Off our Full Brunch Buffet</strong> – All Summer Long! Includes coffee, tea, and juice. The perfect start to your Sunday with comfort food and good vibes.</p>
        </div>

        <div style="text-align: center; margin-top: 48px;">
          <p style="font-weight: bold; margin-bottom: 24px;">Join us at KS on the Keys, where every day has its flavor. Walk-ins welcome!</p>
          <a href="https://www.tbdine.com/book/restaurant/ks-on-the-keys-restaurant?idApp=69099&language=en-us" target="_blank" class="btn btn-primary btn-lg">Reserve a Table</a>
        </div>
      </div>
    </div>
  </section>
"""
with open('dailyspecials.html', 'w', encoding='utf-8') as f:
    f.write(top_content + dailyspecials_main + bottom_content)

# Write private events
events_main = """
  <section class="subpage-hero" aria-label="Private Events">
    <div class="subpage-hero-bg" style="background-image: url('images/events/grand-event-room-1.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Host With Us</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Private <em>Events</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Modern corporate event spaces and large group venues in Ottawa South. Corporate lunches, meetings, weddings & galas.</p>
    </div>
  </section>

  <section class="subpage-content">
    <div class="container fade-in">
      <div class="document-content">
        <h2 style="font-family: var(--font-serif); font-size: 2rem; color: var(--burgundy-dark); margin-bottom: 24px; text-align: center;">Your Event, Perfectly Hosted</h2>
        <p style="text-align: center; margin-bottom: 48px;">From intimate boardroom gatherings to grand celebrations of over 100 people, KS on the Keys offers beautifully appointed spaces designed to impress your guests and make hosting effortless.</p>

        <h3>1. The Grand Event Room</h3>
        <p>Our largest and most versatile space. Perfect for large corporate presentations, retirement parties, weddings, and holiday galas. Fully private with customizable table layouts.</p>
        <ul>
          <li><strong>Capacity:</strong> Up to 110 Guests</li>
          <li><strong>Features:</strong> Full AV equipment available, dedicated service staff, high-speed Wi-Fi, customizable catering or buffet setup.</li>
        </ul>

        <h3>2. The Mezzanine Floor</h3>
        <p>A classic, semi-private elevated space offering a sophisticated dining experience while keeping the energetic atmosphere of our main restaurant.</p>
        <ul>
          <li><strong>Capacity:</strong> Up to 60 Guests</li>
          <li><strong>Features:</strong> Elevator accessibility, lovely views of the restaurant below, perfect for medium-sized corporate dinners or family gatherings.</li>
        </ul>

        <h3>3. The Private Board Room</h3>
        <p>A professional, quiet space built specifically for corporate meetings, strategy sessions, or intimate group dining.</p>
        <ul>
          <li><strong>Capacity:</strong> Up to 20 Guests</li>
          <li><strong>Features:</strong> Large flat-screen TV with HDMI connectivity, wireless microphone, dedicated service.</li>
        </ul>

        <div class="pricing-block">
          <h4>Custom Menus & Dietary Accommodations</h4>
          <p style="margin:0;">We understand the complexities of hosting large groups. Our executive chef can create tailored menus ranging from formal plated dinners to casual buffets. We confidently accommodate Halal, Vegan, Vegetarian, and Gluten-Free dietary requirements.</p>
        </div>

        <div style="text-align: center; margin-top: 48px;">
          <p style="margin-bottom: 16px;">Ready to start planning? Our event coordinators are here to help.</p>
          <a href="mailto:RSVP@ksrestaurant.ca" class="btn btn-primary btn-lg">Email RSVP@ksrestaurant.ca to Inquire</a>
        </div>
      </div>
    </div>
  </section>
"""
with open('private-events.html', 'w', encoding='utf-8') as f:
    f.write(top_content + events_main + bottom_content)

print("Created dailyspecials.html and private-events.html")
