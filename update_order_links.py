import os
import glob
import re

html_files = glob.glob("*.html")

desktop_replacement = """        <li class="has-dropdown order-dropdown">
          <a href="#" class="nav-cta" id="order-now-nav">Order Now ▾</a>
          <ul class="dropdown dropdown-right" style="min-width: 200px;">
            <li><a href="https://order.tbdine.com/pickup/30078/menu" target="_blank">Pickup</a></li>
            <li><a href="https://www.ksonthekeys.com/delivery" target="_blank">In-House Delivery</a></li>
            <li><a href="https://www.ubereats.com/ca/store/ks-on-the-keys-restaurant/mw7AnpmYQ72yR1jO_5y1fw?srsltid=AfmBOop7SM1DoP4ko2bmMMWE7K1Ss4xnOpDgI-W4P5cbwxT4GvgxUe4j" target="_blank">Uber Eats</a></li>
            <li><a href="https://www.skipthedishes.com/ks-on-the-keys-restaurant" target="_blank">Skip the Dishes</a></li>
            <li><a href="https://www.doordash.com/store/ks-on-the-keys-ottawa-298448/1000/?srsltid=AfmBOooBdAlGQBW514EKMfhkyeXV0IZvEtwex9keIY4OxJLaS16fcusN" target="_blank">DoorDash</a></li>
          </ul>
        </li>"""

mobile_replacement = """    <div class="mobile-dropdown-container">
      <span class="mobile-link" style="color: var(--gold-light) !important; font-weight: 700; margin-top: 12px; display: block;">🍕 Order Online ▾</span>
      <div class="mobile-sublinks" style="padding-left: 20px; margin-bottom: 15px;">
        <a href="https://order.tbdine.com/pickup/30078/menu" target="_blank" class="mobile-link" style="font-size: 0.9rem;">Pickup</a>
        <a href="https://www.ksonthekeys.com/delivery" target="_blank" class="mobile-link" style="font-size: 0.9rem;">In-House Delivery</a>
        <a href="https://www.ubereats.com/ca/store/ks-on-the-keys-restaurant/mw7AnpmYQ72yR1jO_5y1fw?srsltid=AfmBOop7SM1DoP4ko2bmMMWE7K1Ss4xnOpDgI-W4P5cbwxT4GvgxUe4j" target="_blank" class="mobile-link" style="font-size: 0.9rem;">Uber Eats</a>
        <a href="https://www.skipthedishes.com/ks-on-the-keys-restaurant" target="_blank" class="mobile-link" style="font-size: 0.9rem;">Skip the Dishes</a>
        <a href="https://www.doordash.com/store/ks-on-the-keys-ottawa-298448/1000/?srsltid=AfmBOooBdAlGQBW514EKMfhkyeXV0IZvEtwex9keIY4OxJLaS16fcusN" target="_blank" class="mobile-link" style="font-size: 0.9rem;">DoorDash</a>
      </div>
    </div>"""


desktop_pattern1 = re.compile(r'<li>\s*<a href="https://order\.tbdine\.com/pickup/30078/menu" target="_blank" class="nav-cta" id="order-now-nav">Order Now</a>\s*</li>')
mobile_pattern1 = re.compile(r'<a href="https://order\.tbdine\.com/pickup/30078/menu" target="_blank" class="nav-cta" style="margin-top: 12px;">🍕 Order Online Now</a>')
mobile_pattern2 = re.compile(r'<a href="https://order\.tbdine\.com/pickup/30078/menu" target="_blank" style="color: var\(--gold-light\) !important; font-weight: 700; margin-top: 12px;">🍕 Order Online Now</a>')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Replace desktop
    content = desktop_pattern1.sub(desktop_replacement, content)
    
    # Replace mobile
    content = mobile_pattern1.sub(mobile_replacement, content)
    content = mobile_pattern2.sub(mobile_replacement, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No match found in {filepath}")
