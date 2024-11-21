
import glob
import logging
import os
from pathlib import Path
import xml.etree.ElementTree as ET
import json
import csv
from csv import writer
import logging

"""Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv"""

directory = Path('/Users/natalynazarenko/PycharmProjects/pythonProject1/lesson_05')
#Variable with path to directory


# def find_duplicate(directory):
#     duplic = []
#     files = sorted(os.listdir(directory))
#     for file_name in files:
#         duplic.append(str(file_name))
#         if duplic.count(file_name) > 1:
#             with open('result_nazarenko.csv', 'w') as file_csv:
#                 csv.writer(file_csv).writerows(duplic)
#                 os.remove(file_name)
#
#         else:
#             print("No Duplicate")
#
# find_duplicate(directory)


"""Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для 
невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

files_json = glob.glob(r'/Users/natalynazarenko/PycharmProjects/pythonProject1/lesson_05/*.json')
#Variable with path to files

# def find_json_files(files_json):
#     logging.basicConfig(
#         filename='json_nazarenko.log',
#         level=logging.ERROR,
#         format='%(asctime)s - %(message)s')
#
#     try:
#         for file in files_json:
#             with open(file, 'rb') as f:
#                 json.load(f)
#                 print("ok")
#     except ValueError as e:
#         print("Wrong file")
#         logger = logging.getLogger("log_event")
#         logger.error(f"Error")

#find_json_files(files_json)

"""Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення 
значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

xml_file = '/Users/natalynazarenko/PycharmProjects/pythonProject1/lesson_05/numbers.xml'
#Variable with path to xml

def find_value_in_tree(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    try:

        console_out = logging.StreamHandler()
        file_log = logging.FileHandler('Log.log')
        logging.basicConfig(handlers=(file_log, console_out),
                             format='[%(asctime)s | %(levelname)s]: %(message)s',
                             datefmt='%m.%d.%Y %H:%M:%S',
                             level=logging.INFO)
        with open(xml_file, 'r') as xml:
            xml.read()
            #number_value = root.find('.//incoming')

        for tag in root.iter():
            #print(tag)
            if tag.tag == 'incoming':
                value = tag.text
                #print(value)
                logging.info(value)

    except ValueError as e:
        print("Wrong tag")


find_value_in_tree(xml_file)



