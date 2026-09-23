import glob
import re
import os

html_files = glob.glob('*.html')
desktop_target = r'(<li class="has-dropdown">\s*<span>Upcoming Events ▾</span>\s*<ul class="dropdown">)'
desktop_replacement = r'\1\n            <li><a href="thanksgiving.html">Thanksgiving Buffet</a></li>'

mobile_target = r'(<a href="big-band-ottawa.html" class="mobile-link">Big Band Ottawa</a>)'
mobile_replacement = r'<a href="thanksgiving.html" class="mobile-link">Thanksgiving Buffet</a>\n    \1'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply Desktop Navbar Change
    new_content = re.sub(desktop_target, desktop_replacement, content, flags=re.IGNORECASE)
    
    # Apply Mobile Navbar Change
    new_content = re.sub(mobile_target, mobile_replacement, new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated nav in {filepath}")
    else:
        print(f"No changes needed in {filepath}")

