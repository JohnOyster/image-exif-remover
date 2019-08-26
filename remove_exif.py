#!/usr/bin/env python3
"""Simple EXIF Data Scrubber.

This is a simple Python script used to scrub exif data from photos before
you send them out.

"""
import os
import sys
from PIL import Image

# Define supported file types
SUPPORTED_TYPES = ('.jpg')


def scrub_image(image_file):
    """Scrub all the exif data from an image."""
    print("[Info]\tScrubbing Image:   {}".format(image_file))
    image = Image.open(image_file)
    data = list(image.getdata())
    safe_image = Image.new(image.mode, image.size)
    safe_image.putdata(data)
    safe_filename = get_safe_name(image_file)
    print(safe_filename)
    safe_image.save(safe_filename)
    print("[INFO]\tExif data removed, saved as:   {}".format(safe_filename))


def check_file(filename):
    """Make sure the argument passed in is a valid image file."""
    is_file = os.path.isfile(filename)
    is_image = filename.endswith(SUPPORTED_TYPES)
    return is_file and is_image


def get_safe_name(image_file):
    """Check to get file name appended with 'safe_'."""
    path, filename = os.path.split(image_file)
    new_filename = "safe_{}".format(filename)
    return os.path.join(path, new_filename)


def file_help():
    """Display the basic help information."""
    print("remove_exif.py <image filename>")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        file_help()
        exit(1)
    IMAGE_FILE = sys.argv[1]
    if check_file(IMAGE_FILE):
        scrub_image(IMAGE_FILE)
    else:
        print("[ERROR]\tInvalid File!")
