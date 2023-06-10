import os
import cairosvg
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt user for folders
Tk().withdraw()
svg_folder = askdirectory(title='Select folder with svg images:')
jpg_folder = askdirectory(title='Select folder to save converted jpg images:')

# check if folders exist, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the svg folder
for file_name in os.listdir(svg_folder):
    if file_name.endswith('.svg') or file_name.endswith('.SVG'):
        # open svg image and convert to jpg
        svg_file_path = os.path.join(svg_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        cairosvg.svg2png(url=svg_file_path, write_to=jpg_file_path)
        jpg_image = Image.open(jpg_file_path)

        # save jpg image with maximum quality
        jpg_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All svg images in {svg_folder} converted to jpg and saved in {jpg_folder}.')

#softy_plug