import logging
import glob
import json




"""Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для 
невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

files_json = glob.glob(r'/Users/natalynazarenko/PycharmProjects/pythonProject1/lesson_05/*.json')
#Variable with path to files

def find_json_files(files_json):
    logging.basicConfig(
        filename='json_nazarenko.log',
        level=logging.ERROR,
        format='%(asctime)s - %(message)s')

    try:
        for file in files_json:
            with open(file, 'rb') as f:
                json.load(f)
                print("ok")
    except ValueError as e:
        print("Wrong file")
        logger = logging.getLogger("log_event")
        logger.error(f"Error")

find_json_files(files_json)