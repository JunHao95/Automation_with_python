#! /usr/bin/env python3
import os
import requests
import json

def jsonData(url,Description_path):
    for textfile in os.listdir(Description_path):
        fruit = {}
        textfile_path = Description_path + textfile
        with open(textfile_path) as filehandle:
            content = filehandle.readlines()
            Description = content[2].strip('\n')
            fruit['description'] = Description
            fruit['weight'] = int(content[1].strip('\n').strip('lbs'))
            fruit['name'] = content[0].strip('\n')
            fruit['image_name'] = textfile.strip('.txt') + '.jpeg'
            print("Fruit dict is {}".format(fruit))
            if url != "":
                response = requests.post(url,json=fruit)
                print("Staus is {} while request is {}".format(response.status_code,response.request.url))



def main():
    username = os.getenv('USER')
    url = 'http://localhost/fruits/'
    Description_path = '/home/{}/supplier-data/descriptions/'.format(username)
    jsonData(url,Description_path)


main()
