from pathlib import Path

html = Path('index.html').read_text(encoding='utf-8')

# 1) closing tags should appear exactly once at end
assert html.count('</body>') == 1, 'Expected a single </body> tag'
assert html.count('</html>') == 1, 'Expected a single </html> tag'
assert html.rstrip().endswith('</html>'), 'Document must end with </html>'

# 2) Open Graph core tags should exist
for tag in ['og:type', 'og:url', 'og:title', 'og:description', 'og:image']:
    assert tag in html, f'Missing Open Graph tag: {tag}'

# 3) reservation field and handler wiring
assert 'id="phoneNum"' in html, 'Missing reservation phone input id'
assert 'onclick="submitForm()"' in html, 'Missing submit button handler'
assert 'function submitForm()' in html, 'Missing submitForm function declaration'

print('index.html static checks passed')
