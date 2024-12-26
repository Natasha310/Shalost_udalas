from requests import HTTPError
import requests



"""Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi
ровером “Curiosity” на Марсi. Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за
допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg .
Завдання потрiбно зробити використовуючи модуль requests"""


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
#dict1 = {'photos': [{'id': 102693, 'sol': 1000, 'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG', 'earth_date': '2015-05-30', 'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active', 'max_sol': 4102, 'max_date': '2024-02-19', 'total_photos': 695670, 'cameras': [{'name': 'FHAZ', 'full_name': 'Front Hazard Avoidance Camera'}, {'name': 'NAVCAM', 'full_name': 'Navigation Camera'}, {'name': 'MAST', 'full_name': 'Mast Camera'}, {'name': 'CHEMCAM', 'full_name': 'Chemistry and Camera Complex'}, {'name': 'MAHLI', 'full_name': 'Mars Hand Lens Imager'}, {'name': 'MARDI', 'full_name': 'Mars Descent Imager'}, {'name': 'RHAZ', 'full_name': 'Rear Hazard Avoidance Camera'}]}}, {'id': 102694, 'sol': 1000, 'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG', 'earth_date': '2015-05-30', 'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active', 'max_sol': 4102, 'max_date': '2024-02-19', 'total_photos': 695670, 'cameras': [{'name': 'FHAZ', 'full_name': 'Front Hazard Avoidance Camera'}, {'name': 'NAVCAM', 'full_name': 'Navigation Camera'}, {'name': 'MAST', 'full_name': 'Mast Camera'}, {'name': 'CHEMCAM', 'full_name': 'Chemistry and Camera Complex'}, {'name': 'MAHLI', 'full_name': 'Mars Hand Lens Imager'}, {'name': 'MARDI', 'full_name': 'Mars Descent Imager'}, {'name': 'RHAZ', 'full_name': 'Rear Hazard Avoidance Camera'}]}}]}

def find_and_parse(*args, **kwargs):
    try:
        response = requests.get(url, params=params)
        data = response.json()
        print(data)
        list1 = [photo['img_src'] for photo in data['photos']]
        print(list1)
        for link in list1:
            image_response = requests.get(link)
            #print("ok")
            if image_response.status_code == 200:
                with open("../uploads/mars_photo1.jpg", "wb") as file:
                    file.write(image_response.content)
                    print(f"Photo loaded")
                with open("../lesson_19/mars_photo2.jpg", "wb") as files:
                    files.write(image_response.content)
                    print(f"Photo loaded")
    except HTTPError as http_err:
        print(f"Error exists: {http_err}")


find_and_parse()