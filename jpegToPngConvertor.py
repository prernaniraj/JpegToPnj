import sys
import os
# import Pillow
# from PIL import Image

old_folder = sys.argv[1]
new_folder = sys.argv[2]

print(old_folder,new_folder)

if not os._exists(new_folder):
    os.mkdir(new_folder)