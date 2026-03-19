from PIL import Image

img = Image.open('public/images/verveo-hero-mockup.png').convert('RGB')
w, h = img.size
pixels = img.load()

# The background of verveo-hero-mockup.png is likely transparent or a solid color.
# Let's find the background color
bg_color = pixels[0, 0]
print("Background color:", bg_color)

# Find the iMac frame bounding box (non-background pixels)
min_x, max_x = w, 0
min_y, max_y = h, 0

for y in range(h):
    for x in range(w):
        if pixels[x, y] != bg_color:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"iMac Frame Bounds: Left={min_x}, Top={min_y}, Right={max_x}, Bottom={max_y}")
print(f"Frame Width={max_x - min_x}, Height={max_y - min_y}")

# The screen is usually a certain percentage of the frame.
# For a standard iMac mockup: 
# vertical bezel is about 4-5%, top bezel is 5-6%, chin is about 20%
# Let's print out the colors along the vertical center axis to see where the screen starts and ends.
center_x = min_x + (max_x - min_x) // 2
colors = []
for y in range(min_y, max_y + 1, 10):
    colors.append((y, pixels[center_x, y]))

print("Colors along center Y axis:", colors)

# Let's also print along the horizontal center axis of the top half
center_y = min_y + (max_y - min_y) // 3
row_colors = []
for x in range(min_x, max_x + 1, 10):
    row_colors.append((x, pixels[x, center_y]))

print("Colors along center X axis:", row_colors)
