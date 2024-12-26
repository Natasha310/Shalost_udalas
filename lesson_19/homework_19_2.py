import os.path
import sys
import requests
from asgiref.timeout import timeout
from requests import HTTPError
from flask import request
import json

"""Враховуючи документацiю яку наведено нижче вам потрiбно написати код який використовуючи модуль
request зробить через POST upload якогось зображення на сервер, за допомогою GET отримає посилання
на цей файл и потiм за допомогою DELETE зробить видалення файлу з сервера"""

url = "http://127.0.0.1:8080"
image = "/Users/natalynazarenko/PycharmProjects/pythonProject1/lesson_19/uploads/44.png"


def post_image(url, image, timeout):
     if not os.path.exists(image):
         print("Not found")

     try:
        with open(image, 'rb') as file:
                file.read()
                files = {'image': file}
                response = requests.post(f'{url}/upload', files= files, timeout=timeout)
                response.raise_for_status()
                content = response.json().get("image")
                #print(content)
                if response.status_code == 201:
                     print(f'Image loaded')

                try:
                    requests.delete(f'{url}/upload', files= files, timeout=timeout)
                    response.raise_for_status()
                    response.json().get("image")


                    if response.status_code == 201:
                        print("Image deleted")
                except:
                    raise Exception('Could not delete image')
     except HTTPError as http_err:
        print(f"Error exists: {http_err}")


print(post_image(url, image, timeout=30))
