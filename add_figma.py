import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

figma_block = """                <div class="tool-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/figma/figma-original.svg" alt="Figma" />
                </div>
"""

# We want to insert this block after <!-- Group 1 --> and after <!-- Group 2 ... -->
def repl(match):
    return match.group(0) + "\n" + figma_block

new_text = re.sub(r'<!-- Group 1 -->|<!-- Group 2 \(Duplicate for infinite loop\) -->', repl, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("figma added")
