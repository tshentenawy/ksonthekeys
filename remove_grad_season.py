import glob
import re
import os

html_files = glob.glob('*.html')

desktop_pattern = r'\s*<li><a href="grad-season\.html">Grad Season 2026</a></li>'
mobile_pattern = r'\s*<a href="grad-season\.html" class="mobile-link">Grad Season 2026</a>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(desktop_pattern, '', content)
    new_content = re.sub(mobile_pattern, '', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed from {filepath}")

