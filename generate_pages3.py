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

# Write nonprofits
nonprofits_main = """
  <section class="subpage-hero" aria-label="Non-Profits">
    <div class="subpage-hero-bg" style="background-image: url('images/events/boardroom-1.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Community First</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Non-Profit <em>Support</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Proudly supporting Ottawa's local charities and non-profit organizations for over 50 years.</p>
    </div>
  </section>

  <section class="subpage-content">
    <div class="container fade-in">
      <div class="document-content">
        <div style="text-align: center; margin-bottom: 40px;">
          <h2 style="font-family: var(--font-serif); font-size: 2rem; color: var(--burgundy-dark); margin-bottom: 16px;">Partnering with Our Community</h2>
          <p style="color: var(--text-mid); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">At KS on the Keys, we believe deeply in giving back. Since 1971, we have worked alongside numerous non-profit organizations to help them achieve their fundraising goals and host successful events.</p>
        </div>

        <h3>Special Pricing for Charity Events</h3>
        <p>We understand that non-profits operate on tight budgets. That's why we offer special discounted rates on our venue spaces and customized catering menus tailored specifically for charitable organizations.</p>

        <h3>Event Types We Host</h3>
        <ul>
          <li>Fundraising Galas and Dinners</li>
          <li>Silent Auctions</li>
          <li>Board Meetings</li>
          <li>Volunteer Appreciation events</li>
          <li>Community Outreach gatherings</li>
        </ul>

        <div class="pricing-block">
          <h4>Need a Donation or Sponsorship?</h4>
          <p style="margin:0;">KS on the Keys regularly donates gift cards and sponsorships for local school fundraisers, sports teams, and charity events. Please reach out to us with your event details!</p>
        </div>

        <div style="text-align: center; margin-top: 48px;">
          <p style="margin-bottom: 16px;">Ready to discuss your organization's event needs?</p>
          <a href="mailto:RSVP@ksrestaurant.ca" class="btn btn-primary btn-lg">Email RSVP@ksrestaurant.ca</a>
        </div>
      </div>
    </div>
  </section>
"""
with open('nonprofits.html', 'w', encoding='utf-8') as f:
    f.write(top_content + nonprofits_main + bottom_content)

# Write delivery
delivery_main = """
  <section class="subpage-hero" aria-label="Delivery">
    <div class="subpage-hero-bg" style="background-image: url('images/hero-bg.jpg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">Fresh To Your Door</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Food <em>Delivery</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Order KS on the Keys for quick, hot delivery right to your door in Ottawa South.</p>
    </div>
  </section>

  <section class="subpage-content">
    <div class="container fade-in">
      <div class="document-content">
        <div style="text-align: center; margin-bottom: 40px;">
          <h2 style="font-family: var(--font-serif); font-size: 2rem; color: var(--burgundy-dark); margin-bottom: 16px;">Craving KS at Home?</h2>
          <p style="color: var(--text-mid); font-size: 1.1rem;">Enjoy our famous pizza, pasta, and comfort classics without leaving the house. We utilize a dedicated delivery team to ensure your food arrives hot, fresh, and fast.</p>
        </div>

        <h3>Delivery Details</h3>
        <ul>
          <li><strong>Delivery Zone:</strong> We deliver throughout Ottawa South (Gloucester, South Keys, Greenboro, Hunt Club, and surrounding areas).</li>
          <li><strong>How to Order:</strong> Use our fast and secure online ordering platform via TBDine to place your order directly with our kitchen.</li>
          <li><strong>Delivery Partner:</strong> If you are outside our own delivery zone, you can also find us on major delivery apps like UberEats and SkipTheDishes!</li>
        </ul>

        <div class="pricing-block">
          <h4>Order Direct and Save</h4>
          <p style="margin:0;">Ordering directly through our website via the TBDine link helps support us as a local independent business, and often ensures the best pricing and most accurate delivery times.</p>
        </div>

        <div style="text-align: center; margin-top: 48px;">
          <a href="https://order.tbdine.com/pickup/30078/menu" target="_blank" class="btn btn-primary btn-lg">Order Delivery Online Now</a>
        </div>
      </div>
    </div>
  </section>
"""
with open('delivery.html', 'w', encoding='utf-8') as f:
    f.write(top_content + delivery_main + bottom_content)

# Write upcoming events
upcoming_main = """
  <section class="subpage-hero" aria-label="Upcoming Events">
    <div class="subpage-hero-bg" style="background-image: url('images/events/mezzanine-1.jpeg');"></div>
    <div class="subpage-hero-overlay"></div>
    <div class="subpage-hero-content fade-in">
      <p class="hero-eyebrow" style="justify-content:center;">What's Happening</p>
      <h1 class="hero-title" style="font-size:clamp(2rem, 5vw, 4rem);">Upcoming <em>Events</em></h1>
      <p class="hero-subtitle" style="margin: 0 auto;">Check out all the holiday specials, live music, and special themed nights coming up at KS.</p>
    </div>
  </section>

  <section class="subpage-content">
    <div class="container fade-in">
      <div class="document-content">
        <div style="text-align: center; margin-bottom: 40px;">
          <h2 style="font-family: var(--font-serif); font-size: 2rem; color: var(--burgundy-dark); margin-bottom: 16px;">Celebrate with Us</h2>
          <p style="color: var(--text-mid); font-size: 1.1rem;">From festive holiday buffets to summer patio parties, there's always something going on at KS.</p>
        </div>
        
        <div style="text-align: center; padding: 40px; background: rgba(196,154,60,0.05); border-radius: var(--radius-md); border: 1px dashed rgba(196,154,60,0.5);">
          <h3 style="margin-top: 0;">Stay Tuned!</h3>
          <p style="margin-bottom: 0;">We don't have any special ticketed events scheduled right now. In the meantime, don't miss out on our <a href="dailyspecials.html" style="color: var(--burgundy); font-weight: bold; text-decoration: underline;">Daily Specials</a>!</p>
        </div>

        <div style="text-align: center; margin-top: 48px;">
          <a href="https://www.tbdine.com/book/restaurant/ks-on-the-keys-restaurant?idApp=69099&language=en-us" target="_blank" class="btn btn-primary btn-lg">Book a Standard Table</a>
        </div>
      </div>
    </div>
  </section>
"""
with open('upcoming-events.html', 'w', encoding='utf-8') as f:
    f.write(top_content + upcoming_main + bottom_content)

print("Created nonprofits.html, delivery.html, upcoming-events.html")
