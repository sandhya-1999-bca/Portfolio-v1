from PIL import Image

v = Image.open('public/images/verveo-hero-mockup.png')
print("Verveo mockup:", v.size)

n = Image.open('public/images/nf-solutions-home.jpg')
print("NF Solutions home:", n.size)

# I can also print the center pixel's color in Verveo just to see
pixels = v.load()
w, h = v.size
print("Center pixel:", pixels[w//2, h//2])
