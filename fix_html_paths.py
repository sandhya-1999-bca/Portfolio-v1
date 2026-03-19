import glob
import os

js_snippet = """
    <!-- GitHub Pages path fix -->
    <script>
        if (window.location.hostname.includes('github.io')) {
            document.addEventListener('DOMContentLoaded', function() {
                var fixPath = function(val) {
                    if (!val || val.startsWith('http') || val.startsWith('#') || val.startsWith('mailto:') || val.startsWith('javascript:')) return val;
                    return val.split('/').pop();
                };
                document.querySelectorAll('img').forEach(function(img) {
                    var src = img.getAttribute('src');
                    if (src) img.setAttribute('src', fixPath(src));
                });
                document.querySelectorAll('a').forEach(function(a) {
                    var href = a.getAttribute('href');
                    if (href && (href.endsWith('.pdf') || href.endsWith('.jpg') || href.endsWith('.png') || href.endsWith('.svg'))) {
                        a.setAttribute('href', fixPath(href));
                    }
                });
            });
        }
    </script>
</head>
"""

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already injected
    if 'GitHub Pages path fix' in content:
        continue
        
    content = content.replace('</head>', js_snippet)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print(f"Injected GitHub pages fix into {len(html_files)} files.")
