import json
import os
import stat
import time


def json_to_dict(file_path):
    expense_dict = json.load(open(file_path))
    return expense_dict


def last_modification_file(file_path):
    file_status = os.stat(file_path)
    last_modification = time.ctime(file_status[stat.ST_MTIME])
    return last_modification, file_status[stat.ST_MTIME]


def current_date():
    str_date = time.ctime()
    epoch = time.time()
    return str_date, epoch


def compare_file_date_to_db_date(file_path):
    last_modif_str, epoch_file = last_modification_file(file_path)
    # contnuie with loading information from the database




