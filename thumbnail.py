import sys
import os
imageDir = sys.argv[1]
thumbDir = sys.argv[2]
imageFiles = [f for f in os.listdir(imageDir) if os.path.isfile(os.path.join(imageDir, f))]
for imageFile in imageFiles:
    if not os.path.exists(os.path.join(thumbDir, imageFile)):
        os.system("convert " + os.path.join(imageDir, imageFile) + " -strip -interlace Plane -resize 65536@ " + os.path.join(thumbDir, imageFile))
