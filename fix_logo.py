from PIL import Image
import math

img = Image.open('/Users/sandhya/.gemini/antigravity/brain/ce7f7778-ad9b-46e8-b26a-5b0de79a714d/media__1772935368002.png')
img = img.convert("RGBA")
datas = img.getdata()
new_data = []

for item in datas:
    r, g, b, a = item
    brightness = (r + g + b) / 3.0
    
    # colorfulness check: standard deviation of r, g, b
    # if it's grey/black/white, the std dev is very low.
    mean = brightness
    std = math.sqrt(((r - mean)**2 + (g - mean)**2 + (b - mean)**2) / 3.0)
    
    # Remove white background
    if r > 240 and g > 240 and b > 240:
        new_data.append((255, 255, 255, 0))
    # If it's a dark color (the text), let's invert it to be light or white for the dark theme
    elif std < 10 and brightness < 150:
        # It's a dark shade of grey or black. Make it white, keeping the anti-aliased edge (via alpha or light gray)
        # To make it contrast well, invert it!
        inverted_val = 255 - int(brightness)
        new_data.append((255, 255, 255, inverted_val))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save('/Users/sandhya/Documents/code/portfoliov1/public/images/sandhya-logo-transparent.png', 'PNG')
print("Logo fixed and saved.")
