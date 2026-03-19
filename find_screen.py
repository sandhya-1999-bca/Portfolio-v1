from PIL import Image

def find_inner_bounds(image_path):
    img = Image.open(image_path).convert('RGB')
    w, h = img.size
    cx, cy = w // 2, h // 2
    
    # We assume the screen has some content, but the frame is black/dark gray.
    # Let's just find the continuous non-dark area in the center.
    # Actually, the iMac frame in mockups is usually black (#000000 to #111111).
    # Let's search from center outwards for dark black pixels.
    
    pixels = img.load()
    
    def is_frame(x, y):
        r, g, b = pixels[x, y]
        return r < 40 and g < 40 and b < 40  # typical iMac border is dark

    # find top
    top = cy
    while top > 0 and not is_frame(cx, top):
        top -= 1
        
    # find bottom
    bottom = cy
    while bottom < h - 1 and not is_frame(cx, bottom):
        bottom += 1

    # find left
    left = cx
    while left > 0 and not is_frame(left, cy):
        left -= 1
        
    # find right
    right = cx
    while right < w - 1 and not is_frame(right, cy):
        right += 1

    print(f"Detected screen bounds: Left={left}, Top={top}, Right={right}, Bottom={bottom}")
    print(f"Screen width: {right - left}, Screen height: {bottom - top}")

find_inner_bounds('public/images/verveo-hero-mockup.png')
