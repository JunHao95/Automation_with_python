#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
username = os.getenv('USER')
images_path = '/home/{}/supplier-data/images/'.format(username)

images = os.listdir(images_path)
for image in images:
    if 'jpeg' in image:
        image_path = images_path + image
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
