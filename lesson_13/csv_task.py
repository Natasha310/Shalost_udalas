import os
import csv

"""Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv"""


file_path1 = r'/lesson_10/work_with_csv/r-m-c.csv'
file_path2 = r'/lesson_10/work_with_csv/random.csv'

def check_duplictes(file_path1, file_path2):
    with open (file_path1, 'rb') as duple:
        content = duple.read()
        print("content")
    with open(file_path2, 'rb') as f_csv:
        content2 = f_csv.read()
        print("content2")
        if content == content2:
            with open('result_nazarenko.csv', 'w') as file_csv:
                csv.writer(file_csv).writerow(f'Duplicate is found')
                os.remove(file_path2)
        else:
            with open('result_nazarenko.csv', 'w') as file_csv:
                csv.writer(file_csv).writerow(f'No duplicates')


check_duplictes(file_path1, file_path2)