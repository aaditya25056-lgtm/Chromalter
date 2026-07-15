# Chromalter

An OpenCV-based wall paint & wallpaper visualizer. Select a wall in a room photo
and preview it either recolored with a custom paint shade or overlaid with a
wallpaper texture — built as a B.Tech mini project.

## Features

- **Custom color fill** — pick any color by double-clicking a reference swatch,
  and flood-fill a selected wall region with it
- **Wallpaper preview** — paste a wallpaper/texture image onto a selected wall
  region, auto-resized to fit
- **Nearest color-name lookup** — matches any picked RGB value against an
  865-entry named color reference (`cdataset.csv`)

## Project structure

```
Chromalter/
├── select_ROI.py             # main entry point — run this
├── color_1.py                # color-name picker, invoked by select_ROI.py
├── cdataset.csv               # 865 named colors (name, hex, R, G, B)
├── wall1.jpg ... wall7.jpg     # sample room/wall photos
├── frame1.jpg ... frame3.jpg    # sample wallpaper/texture images
├── colorgrid.jpg               # color swatch image used for picking a fill color
├── colorgrid1.jpg               # alternate color swatch image
├── requirements.txt
└── .gitignore
```

## Setup

```bash
pip install -r requirements.txt
```

Requires Python 3 with a display (uses OpenCV `imshow` windows — won't work
headless / over SSH without X forwarding).

## Usage

Run the main script:

```bash
python select_ROI.py
```

You'll be prompted: `Choose 1 or 2:`

### Option 1 — Recolor a wall with a custom paint shade

1. A window opens showing `colorgrid.jpg`. **Double-click** anywhere on it to
   pick a color — the picked color's name and RGB values are overlaid on the
   image.
2. Press **Esc** to close this window and continue.
3. The "Original Image" window opens, showing `wall3.png`. Click into the
   window, then press **`a`** to start ROI selection.
4. Drag a box around the wall area you want to recolor, then press
   **Enter** (or **Space**) to confirm the selection.
5. The selected region is flood-filled with the color you picked in step 1.
6. Result is saved as `new_wall.jpg` in the working directory.
7. Press **`q`** to quit, or `a` again to select another region.

### Option 2 (or any number > 1) — Preview a wallpaper texture

1. The "Original Image" window opens (`wall3.png`). Press **`a`** to start
   ROI selection.
2. Drag a box around the wall area, then press **Enter**/**Space** to confirm.
3. `frame1.jpg` is resized to fit the selected region and pasted in.
4. Result is saved as `new_wall.jpg`.
5. Press **`q`** to quit.

### Standalone color-name lookup

`color_1.py` can also be run directly to test the color picker on its own:

```bash
python color_1.py
```

Double-click any pixel on `colorgrid.jpg` to see its nearest named color and
RGB values overlaid on the image. Press **Esc** to quit.

## How it works

- **ROI selection** uses OpenCV's `cv2.selectROI`, which returns the
  bounding box of a user-dragged rectangle.
- **Color naming** computes the sum of absolute differences between the
  clicked pixel's RGB and every entry in `cdataset.csv`, returning the
  closest match — a simple nearest-neighbor lookup, not perceptual color
  distance (e.g. not CIEDE2000).
- Swap in your own room photo or wallpaper by replacing `wall3.png` /
  `frame1.jpg`, or edit the filenames at the top of `select_ROI.py`.

## Known limitations

- Wall and wallpaper filenames (`wall3.png`, `frame1.jpg`) are hardcoded at
  the top of `select_ROI.py` rather than passed as arguments.
- Color distance uses simple absolute RGB difference, not a perceptual color
  space — nearest-name matches can be a bit off for close shades.
- No CLI flags — image swaps require editing the script directly.

## Tech stack

Python, OpenCV, pandas, NumPy
