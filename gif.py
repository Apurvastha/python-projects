import imageio.v3 as iio
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

# Hide the root window
Tk().withdraw()

# Ask the user to select image files
filenames = askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

# Check if the user selected any files
if not filenames:
    print("No files selected.")
else:
    images = []

    # Read each selected image file
    for filename in filenames:
        images.append(iio.imread(filename))
        
    # Set the file name
    output_filename = input("Save as: ") + '.gif'

    # Save the images as a GIF
    iio.imwrite(output_filename, images, duration=500, loop=0)
    print(f"GIF saved as {output_filename}")