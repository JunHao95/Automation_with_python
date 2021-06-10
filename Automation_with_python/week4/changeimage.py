#!/usr/bin/env python3

import os
import sys
from PIL import Image


username = os.getenv('USER')
path = '/home/{}/supplier-data/images/'.format(username)


image_list = os.listdir(path)
for images in image_list:
    if 'tiff' in images: #match file name
        images_path = path + images
        image_path = os.path.splitext(images_path)[0]
        print("image_path is ",image_path)
        im=Image.open(images_path)
        new_image_path = '{}.jpeg'.format(image_path)
        im.convert('RGB').resize((600,400)).save(new_image_path,"JPEG")
