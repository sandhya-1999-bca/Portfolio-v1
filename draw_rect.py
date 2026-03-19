import sys
from PIL import Image, ImageDraw

def draw_rect(x, y, w, h):
    img = Image.open('public/images/verveo-hero-mockup.png').convert('RGB')
    draw = ImageDraw.Draw(img)
    draw.rectangle([x, y, x+w, y+h], outline="red", width=3)
    img.save('public/images/test-rect.png')

draw_rect(55, 65, 530, 310)
