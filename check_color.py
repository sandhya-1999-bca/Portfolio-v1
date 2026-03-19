from PIL import Image
import glob
import sys
for f in sorted(glob.glob('/Users/sandhya/.gemini/antigravity/brain/6b959b33-6eca-47e9-b1b3-f66ff1063d4f/media__1773109*.png')):
    img = Image.open(f)
    img = img.resize((1, 1))
    color = img.getpixel((0, 0))
    print(f"{f}: {color}")
