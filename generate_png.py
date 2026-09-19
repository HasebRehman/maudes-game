from PIL import Image, ImageDraw

def render_favicon(size, rx_ratio=14/64):
    scale = 4
    high_res = size * scale
    img = Image.new("RGBA", (high_res, high_res), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background rounded rect
    rx = int(high_res * rx_ratio)
    draw.rounded_rectangle([0, 0, high_res, high_res], radius=rx, fill="#05070b")
    
    # Coordinates scaled from 64x64 SVG path
    s = high_res / 64.0
    points = [
        (10 * s, 45 * s),
        (10 * s, 18 * s),
        (18 * s, 18 * s),
        (32 * s, 33 * s),
        (46 * s, 18 * s),
        (54 * s, 18 * s),
        (54 * s, 45 * s),
        (44 * s, 45 * s),
        (44 * s, 32 * s),
        (32 * s, 45 * s),
        (20 * s, 32 * s),
        (20 * s, 45 * s)
    ]
    
    draw.polygon(points, fill="#ffae00")
    
    # Downsample with Lanczos anti-aliasing
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    return final_img

if __name__ == "__main__":
    # WordPress recommended 512x512 PNG
    render_favicon(512).save("favicon.png", "PNG")
    render_favicon(512).save("favicon-512x512.png", "PNG")
    render_favicon(192).save("favicon-192x192.png", "PNG")
    print("Favicon PNG files generated successfully.")
