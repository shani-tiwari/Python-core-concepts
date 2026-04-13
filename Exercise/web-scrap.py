
import requests, json, re, os
from bs4 import BeautifulSoup


url = 'https://www.bu.edu/president/boston-university-facts-stats/'
html = requests.get(url, timeout=30).text
soup = BeautifulSoup(html, 'html.parser')

result = {
    'url': url,
    'title': soup.title.get_text(strip=True) if soup.title else 'BU Facts & Stats',
    'quick_facts': {},
    'sections': {}
}

# fallback structured extraction from visible text/content pattern
text = soup.get_text('\n', strip=True)
lines = [line.strip() for line in text.splitlines() if line.strip()]

# quick facts
for i, line in enumerate(lines):
    if line in ['Research Expenditures', 'Study Abroad Programs', 'Sponsored Research Awards']:
        if i + 1 < len(lines):
            result['quick_facts'][line] = lines[i + 1]

# section parsing from fetched structure known on page
sections = ['Community', 'Campus', 'Academics']
current = None
for i, line in enumerate(lines):
    if line in sections:
        current = line
        result['sections'][current] = {}
        continue
    if current:
        if line in sections:
            current = line
            result['sections'][current] = {}
        elif current in ['Community', 'Academics'] and (' ' in line):
            m = re.match(r'^(.*)\s+(\S+)$', line)
            if m:
                k, v = m.groups()
                result['sections'][current][k] = v
        elif current == 'Campus':
            if i + 1 < len(lines) and lines[i] not in sections:
                nxt = lines[i + 1]
                if line not in result['sections'][current] and re.search(r'^[\d,]+$', nxt):
                    result['sections'][current][line] = nxt

os.makedirs('output', exist_ok=True)
path = 'output/bu_facts_stats.json'
with open(path, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(path)
