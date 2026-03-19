import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

group_html = r'''
                <div class="tool-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/figma/figma-original.svg" alt="Figma" />
                </div>
                <div class="tool-icon">
                    <img src="https://cdn.simpleicons.org/miro/050038" alt="Miro" />
                </div>
                <div class="tool-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/xd/xd-plain.svg" alt="Adobe XD" />
                </div>
                <div class="tool-icon">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/canva/canva-original.svg" alt="Canva" />
                </div>
                <div class="tool-icon">
                    <img src="public/images/svgator.png" alt="SVGator" style="object-fit: contain; width: 100%; height: 100%; border-radius: 8px;" />
                </div>
                <div class="tool-icon">
                    <img src="public/images/chatgpt.png" alt="ChatGPT" style="object-fit: contain; width: 100%; height: 100%; border-radius: 8px;" />
                </div>
                <div class="tool-icon">
                    <img src="https://cdn.simpleicons.org/googlegemini/8E75B2" alt="Google Gemini" />
                </div>
                <div class="tool-icon">
                    <img src="https://cdn.simpleicons.org/anthropic/000000" alt="Claude" />
                </div>
                <div class="tool-icon">
                    <img src="public/images/ai-studio.png" alt="AI Studio" style="object-fit: contain; width: 100%; height: 100%; border-radius: 8px;" />
                </div>'''

replacement = f'''                <!-- Group 1 -->{group_html}
                <!-- Group 2 -->{group_html}
                <!-- Group 3 -->{group_html}
                <!-- Group 4 -->{group_html}'''

new_content = re.sub(
    r'(<div class="marquee-content">\s*)(.*?)(<!-- Selected Work Section -->)',
    lambda m: m.group(1) + replacement + '\n            </div>\n        </div>\n    </section>\n\n    ' + m.group(3),
    content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("done")
