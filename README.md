# STARFRUIT ⚔️

A premium katana-slash survival game. Slash glowing fruit in deep space with a
white-hot cyan blade — but **one dynamite ends everything.** One life, rising
tension, an inevitable dramatic end.

Built with **vanilla JavaScript + HTML5 Canvas** — no frameworks, no build step.

## Features
- 🗡️ **Hero katana trail** — tapering white-hot core with electric-cyan glow, fading afterimage.
- 🍉 **Juicy slicing** — fruit splits into two spinning halves with matched-color juice bursts, splatter, and gold `+N` popups.
- 🔥 **Combos** — chain cuts in one swipe for bonus points, a cyan flash + brief slow-mo on 3+.
- 💣 **One life** — a single dynamite triggers a cinematic explosion: white flash, shockwave ring, ember + smoke burst, screen shake, desaturation, then GAME OVER.
- 🌌 **Twinkling parallax starfield** over a deep-space gradient.
- ⏫ **Survival ramp** — every 20s spawns get faster and more dynamite-heavy.
- 🏆 **Global leaderboard** — top-10 via Supabase.
- 📱 Fully mobile-responsive; mouse-drag on desktop, finger-swipe on touch.

## Run locally
Just serve the folder (any static server) and open `index.html`:
```bash
python3 -m http.server 8000
```

## Assets
`fruits.png` is a 3×3 sprite sheet (8 fruits + dynamite). `strip_bg.py` was used
once to flood-fill the baked-in checkerboard background to true transparency.
If `fruits.png` is missing, the game falls back to drawing glossy vector fruit.
