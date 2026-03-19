import glob
import os

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_tag = '<!-- GitHub Pages path fix -->'
    end_tag = '</script>\n</head>'
    
    if start_tag in content:
        start_idx = content.find(start_tag)
        end_idx = content.find('</head>', start_idx)
        
        if start_idx != -1 and end_idx != -1:
            # We want to keep </head>
            new_content = content[:start_idx] + '</head>' + content[end_idx + 7:]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Cleaned up {file}")
