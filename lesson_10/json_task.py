import logging
import glob
import json
from fileinput import filename
from pathlib import Path

"""Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для 
невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

files_json = glob.glob(r'/Users/natalynazarenko/PycharmProjects/pythonProject1/lesson_13/work_with_json/*.json')
#Variable with path to files


def find_json_files(files_json):
    logging.basicConfig(
        filename='../lesson_10/json_nazarenko.log',
        level=logging.ERROR,
        format='%(asctime)s - %(message)s')

    try:
        for file in files_json:
            with open(file, 'rb') as f:
                json.load(f)
            #print("ok")
    except ValueError as e:
        #print("Wrong file")
        logger = logging.getLogger("log_event")
        logger.error(f"Error appeared when validate files{Path.name}")

find_json_files(files_json)


