"""Module test tasks"""


from homework_10 import log_event
import logging
from datetime import date
from venv import logger

"""Check if two arguments were provided"""

def test_two_strings_provided():

    try:
        func_loging = log_event("tester")
    except TypeError as miss_type:
        print("Missing positional argument")


#test_two_strings_provided()

#Test Data
name = "test"
name_1 = "test1"
status_s = "success"
status_e = "expired"
status_f = "failed"

info = logging.info("20")
warn = logging.warning("30")
err = logging.error("40")

logger_data = open('login_system.log', 'r')
data = logger_data.read()

"""Could find only one level of logs"""

def test_logger_level():
    get_logger_code = logger.getEffectiveLevel()

    if get_logger_code == 30 or 20:
        print("Warning or Info")
    else:
        print("Error")


# test_logger_level()
"""Check if status failed in logger"""

def test_logger_status():
    if status_s and status_e in data:
        print("Status ok")
    elif status_f:
        print("Status failed")


test_logger_status()

"""Check was tested at current date"""

def test_logger_date():
    current_date = date.today()
    if str(current_date) in data:
        print("Shown current date")

# test_logger_date()

















