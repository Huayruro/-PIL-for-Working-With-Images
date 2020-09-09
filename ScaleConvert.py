#!/usr/bin/env python3
import os
from PIL import Image
# Images are stored on image directory
orig = 'images'
# The images received are in the wrong format:
# .tiff format
# Image resolution 192x192 pixel (too large)
#	Rotated 90° anti-clockwise
# The images would be in this format:
#	.jpeg format
#	Image resolution 128x128 pixel
#	Should be straight

desti = '/opt/icons'
# Create dir
if not os.path.exists(desti):
    os.makedirs(desti)
    
# Get list of files in image dir

files = os.listdir(orig)

for file in files:
    if os.path.isfile(os.path.join(orig,file)):
        f, e = os.path.splitext(file)
        #if you want to add extension to new file use outfile when saving
        outfile = f + ".jpg"
        # if file is not an image file print message with filename
        if file != outfile:
            try:
                with Image.open(os.path.join(orig,file)) as im:
                    im.rotate(-90).resize((128,128)).convert('RGB').save(os.path.join(desti,file) , 'JPEG')

            except OSError:
                print("cannot convert", file)
