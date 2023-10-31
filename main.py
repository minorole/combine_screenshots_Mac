import os
import re
from PIL import Image

# Functions to find screenshots and combine them
def find_screenshots_on_desktop():
    desktop_path = os.path.expanduser('~/Desktop')
    files = os.listdir(desktop_path)
    screenshots = [os.path.join(desktop_path, f) for f in files if is_screenshot_name(f)]
    # Sort screenshots based on the time part in the filename
    screenshots.sort(key=lambda f: extract_time_from_filename(os.path.basename(f)))
    return screenshots

def extract_time_from_filename(filename):
    # Extract the time part using regex
    match = re.search(r'at (\d{2}\.\d{2}\.\d{2})\.png$', filename)
    if match:
        return match.group(1)
    return ""

def is_screenshot_name(filename):
    return filename.startswith("Screenshot 2023-10-31") and filename.endswith(".png")

def combine_images_to_pdf(filenames, output_filename):
    with Image.open(filenames[0]) as im:
        im_list = [Image.open(f) for f in filenames[1:]]
        im.save(output_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list)

def combine_screenshots():
    screenshots = find_screenshots_on_desktop()
    if screenshots:
        combine_images_to_pdf(screenshots, os.path.expanduser('~/Desktop/combined.pdf'))
        print("Success: Screenshots combined into combined.pdf on your Desktop!")
    else:
        print("No screenshots found with the specified naming pattern.")

# Run the function
combine_screenshots()
