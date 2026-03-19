import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the bad inline styles that squish horizontal logos
content = content.replace('style="object-fit: contain; width: 100%; height: 100%; border-radius: 8px;"', 'style="object-fit: contain; height: 100%; width: auto; border-radius: 8px;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("fixed")
