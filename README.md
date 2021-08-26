# Playnite Library Minifier

This is a Python script that re-encodes all library related images (screenshots, covers, etc.) to JPEG quality = 90, in order to reduce disk usage.

## Usage

* Install the `pillow` package using pip, e.g. `pip install pillow`
* Run the script, e.g. `python playnite-minifier.py`

There are two constants that can be manipulated:
* `VERBOSE` will output more information to console.
* `JPG_QUALITY` will adjust JPEG quality. Use 95 to make it as lossless as possible for JPEG.

## Warnings

The script re-encodes all images, so every time it is run, the images will lose a bit of quality. JPEG headers do not include a quality param, so it isn't that simple to store encoding quality. Do not run this excessively.