#!/usr/bin/env python3
"""Simple EXIF Data Scrubber
This is a simple Python script used to scrub exif data from photos before
you send them out.

"""
import os
import sys
from PIL import Image

# Define supported file types
SUPPORTED_TYPES = ('.jpg')

def scrub_image(filename):
    print("[Info]\tScrubbing Image:   {}".format(filename))
    image  = Image.open(filename)
    data = list(image.getdata())
    safe_image = Image.new(image.mode, image.size)
    safe_image.putdata(data)
    safe_filename = "safe_{}".format(filename) 
    safe_image.save(safe_filename)
    print("[INFO]\tExif data removed, saved as:   {}".format(safe_filename))

def check_file(filename):
    '''A helper function to make sure the argument passed in is a 
    valid image file.
    '''
    is_file = os.path.isfile(filename)
    is_image = filename.endswith(SUPPORTED_TYPES)
    return is_file and is_image

def help():
    '''Displays the basic help information.'''
    # TODO(John): Need to add help

if __name__ == "__main__":
    if sys.argv != 2:
        help()
        exit(1)
    image_file = sys.argv[1]
    if check_file(image_file):
        scrub_image(sys.argv)
    else:
        print("[ERROR]\tInvalid File!")
