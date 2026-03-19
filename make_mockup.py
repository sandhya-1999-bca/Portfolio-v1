import sys
from PIL import Image

def create_mockup():
    bg = Image.open('public/images/verveo-hero-mockup.png').convert('RGBA')
    fg = Image.open('public/images/nf-solutions-home.jpg').convert('RGBA')
    
    # Target screen coordinates based on our analysis
    left, top, right, bottom = 95, 145, 545, 415
    target_width = right - left
    target_height = bottom - top
    
    # Resize the fg image to fit the screen. 
    # We should probably resize and crop to preserve aspect ratio, 
    # or just resize to fit exactly. 
    # Let's resize and crop.
    fg_ratio = fg.width / fg.height
    target_ratio = target_width / target_height
    
    if fg_ratio > target_ratio:
        # fg is wider, scale by height
        new_h = target_height
        new_w = int(new_h * fg_ratio)
        fg_resized = fg.resize((new_w, new_h), Image.Resampling.LANCZOS)
        # crop left/right
        offset = (new_w - target_width) // 2
        fg_cropped = fg_resized.crop((offset, 0, offset + target_width, target_height))
    else:
        # fg is taller, scale by width
        new_w = target_width
        new_h = int(new_w / fg_ratio)
        fg_resized = fg.resize((new_w, new_h), Image.Resampling.LANCZOS)
        # crop bottom usually for websites (keep top)
        fg_cropped = fg_resized.crop((0, 0, target_width, target_height))
        
    # Paste onto the background
    # Since the screen edges might not be perfectly straight (they might have border radius or anti-aliased edges),
    # let's just paste it directly. It should look fine since the border is black.
    bg.paste(fg_cropped, (left, top))
    
    bg.save('public/images/nf-solutions-hero-mockup.png', format='PNG')
    print("Created public/images/nf-solutions-hero-mockup.png successfully.")

if __name__ == "__main__":
    create_mockup()
