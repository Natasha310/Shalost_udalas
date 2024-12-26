import time
from datetime import datetime
from time import gmtime, strftime
import logging
import re

"""Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt
#відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
3.Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.
Обов’язково включіть результат роботи — файл hb_test.log в PR."""

def find_timestamps(text_doc):
    logging.basicConfig(
            filename='hb_test.log',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    list_1 = []

    with open(text_doc, 'r') as file:
            files = file.readlines()
            #print(files)
            list1 = [f for f in files if "TSTFEED0300|7E3E|0400" in f]
            #print(list1)
            for itm in list1:
                #print(itm)
                if "Timestamp " in itm:
                    not_bare = [itm[53:61]]
                    list_1.append(itm[53:61].replace(":", ""))
                    #print(len(list_1))
                #print(not_bare)

                res = [int(list_1[i]) - int(list_1[i + 1]) for i in range(0, len(list_1) - 1, 2)]
                #print(res)

                result = {}
                for key in not_bare:
                    for value in res:
                        result[key] = value
                        res.remove(value)
                    for i in res:
                        if 33 > i > 31:  # in WARNING в файл hb_test.log
                            logging.warning(f"Heartbeat delay: {result} seconds.")
                            #print(i)
                        elif i >= 33:  # ERROR в файл hb_test.log
                             logging.error(f"Heartbeat delay: {result} seconds.")
                             print(result)

print(find_timestamps('hblog.txt'))