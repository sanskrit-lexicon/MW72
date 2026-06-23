import sys, os
sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
from PIL import Image
# usage: python crop.py <scan.png> <nbands>  -> writes _crops/b0..bN at 2x native if small
scan = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
im = Image.open(os.path.join('scans', scan))
W, H = im.size
os.makedirs('_crops', exist_ok=True)
# crop margins lightly, split into n overlapping vertical bands; scale so longest side ~1800
band = H / n
ov = int(band * 0.06)
for i in range(n):
    y0 = max(0, int(i*band) - ov)
    y1 = min(H, int((i+1)*band) + ov)
    c = im.crop((0, y0, W, y1))
    # scale up to ~1800 wide for legibility without exceeding 2000
    scale = min(1900 / c.width, 1900 / c.height, 2.6)
    if scale > 1:
        c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
    c.save(f'_crops/b{i}.png')
    print(f'b{i}.png', c.size)
