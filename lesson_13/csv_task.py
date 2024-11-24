
import logging
import os
from pathlib import Path
import csv
from csv import writer

"""Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv"""

file_path = Path('/Users/natalynazarenko/PycharmProjects/pythonProject1/lesson_05')
#Variable with path to directory


def find_duplicate(file_path):
    duplic = []
    files = sorted(os.listdir(file_path))
    for file_name in files:
        duplic.append(str(file_name))
        if duplic.count(file_name) > 1:
            with open('result_nazarenko.csv', 'w') as file_csv:
                csv.writer(file_csv).writerows(duplic)
                os.remove(file_name)

        else:
            print("No Duplicate")

find_duplicate(file_path)







