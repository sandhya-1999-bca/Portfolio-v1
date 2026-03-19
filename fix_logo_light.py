from PIL import Image

img = Image.open('/Users/sandhya/.gemini/antigravity/brain/ce7f7778-ad9b-46e8-b26a-5b0de79a714d/media__1772935368002.png')
img = img.convert("RGBA")
datas = img.getdata()
new_data = []

for item in datas:
    r, g, b, a = item
    
    # Remove white background
    if r > 240 and g > 240 and b > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save('/Users/sandhya/Documents/code/portfoliov1/public/images/sandhya-logo-transparent-light.png', 'PNG')
print("Light logo fixed and saved.")
