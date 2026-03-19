import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The pattern is the entire <div class="marquee-content" aria-hidden="true">...</div>
pattern = r'(            <div class="marquee-content" aria-hidden="true">[\s\S]+?            </div>)\n(        </div>\n    </section>)'

def repl(match):
    block = match.group(1)
    # block is the marquee-content block. We have 1 visible, 1 hidden. Let's make it 3 hidden.
    return block + "\n" + block + "\n" + block + "\n" + match.group(2)

new_text = re.sub(pattern, repl, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)
