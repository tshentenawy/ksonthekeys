with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

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
    html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html links successfully.")
