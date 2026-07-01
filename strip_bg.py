#!/usr/bin/env python3
"""Strip the baked-in dark checkerboard background from fruits.png.

The sprite sheet is a 3x3 grid; each cell has the fruit centered on a dark
checkerboard. We flood-fill inward from every cell corner, clearing pixels
that are close to the background (dark + low-saturation). Flood connectivity
means interior dark pixels (dynamite body, watermelon seeds, grape shadows)
are preserved because they are enclosed by bright fruit and never reached
from the corners.
"""
import numpy as np
from PIL import Image
from collections import deque

SRC = "fruits.png"
OUT = "fruits.png"

img = Image.open(SRC).convert("RGBA")
arr = np.array(img)                       # (H, W, 4)
H, W = arr.shape[:2]
rgb = arr[:, :, :3].astype(np.int32)

# background test: dark AND low saturation (max-min channel small)
mx = rgb.max(axis=2)
mn = rgb.min(axis=2)
sat = mx - mn
is_bg = (mx < 60) & (sat < 40)            # tuned to the near-black checkerboard

cw, ch = W // 3, H // 3
visited = np.zeros((H, W), dtype=bool)
cleared = np.zeros((H, W), dtype=bool)

def flood(seeds):
    dq = deque()
    for (sx, sy) in seeds:
        if 0 <= sx < W and 0 <= sy < H and is_bg[sy, sx] and not visited[sy, sx]:
            visited[sy, sx] = True
            dq.append((sx, sy))
    while dq:
        x, y = dq.popleft()
        cleared[y, x] = True
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and not visited[ny, nx] and is_bg[ny, nx]:
                visited[ny, nx] = True
                dq.append((nx, ny))

# seed a ring of pixels along each cell's border (robust vs. exact corners)
for row in range(3):
    for col in range(3):
        x0, y0 = col * cw, row * ch
        x1, y1 = x0 + cw - 1, y0 + ch - 1
        seeds = []
        for x in range(x0, x1 + 1):
            seeds.append((x, y0)); seeds.append((x, y1))
        for y in range(y0, y1 + 1):
            seeds.append((x0, y)); seeds.append((x1, y))
        flood(seeds)

# clear alpha where flooded
arr[:, :, 3][cleared] = 0

# feather: soften the 1px edge so fruits don't have a hard dark rim
out = Image.fromarray(arr, "RGBA")
out.save(OUT)

pct = 100.0 * cleared.sum() / (H * W)
print(f"Cleared {pct:.1f}% of pixels to transparent. Saved {OUT} ({W}x{H}).")
