
import xml.etree.ElementTree as ET
import logging


"""Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення 
значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

xml_file = '/lesson_13/numbers.xml'
#Variable with path to xml

def find_value_in_tree(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    try:

        console_out = logging.StreamHandler()
        file_log = logging.FileHandler('../lesson_10/Log.log')
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
