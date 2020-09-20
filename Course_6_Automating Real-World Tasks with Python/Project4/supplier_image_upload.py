#!/usr/bin/env python3
import requests, os
# The URL to upload the images
url = "http://localhost/upload/"
# To get the username from environment variable
USER = os.getenv('USER')
# The directory which contains all the images.
image_directory = '/home/{}/supplier-data/images/'.format(USER)
# Listing all the files in images directory
files = os.listdir(image_directory)
# Parsing through all the images
for image_name in files:
    # Accepting files that has jpeg extension and ignoring hidden files
    if not image_name.startswith('.') and 'jpeg' in image_name:
        # creating absolute path for each image
        image_path = image_directory + image_name
        # uploading jpeg files
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
