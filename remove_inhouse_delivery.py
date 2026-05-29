import os
import glob
import re

html_files = glob.glob("*.html")

desktop_pattern = re.compile(r'\s*<li><a href="https://www\.ksonthekeys\.com/delivery" target="_blank">In-House Delivery</a></li>')
mobile_pattern = re.compile(r'\s*<a href="https://www\.ksonthekeys\.com/delivery" target="_blank" class="mobile-link" style="font-size: 0\.9rem;">In-House Delivery</a>')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Remove desktop link
    content = desktop_pattern.sub('', content)
    
    # Remove mobile link
    content = mobile_pattern.sub('', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No match found in {filepath}")
