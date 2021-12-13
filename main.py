import psycopg2
import os
from helping_functions import *
from database_functions import *

default_folder = "D:/_ user ecaaa/Documents/GitHub/Proiect-Python/Expenses/"
username_db = 'ecaterina'
password_db = '1234'
db_name = 'mydb'


def load_expenses_directory(directory_path):
    list_of_files = os.listdir(directory_path)
    for file in list_of_files:
        print(file)
        absolute_path = default_folder + file

        if "target.json" == file and file.endswith(".json"):
            exists = verify_if_exists(file)
            if exists is False:
                print("loading file", file, " to database")
                create_expense(absolute_path)
            else:
                # timestamp and epocs yay
                timpestamp = 1


def load_target(file):
    json_ceva = 1


if __name__ == '__main__':
    connection, cur = connect_to_db()
    run_verify()
    load_expenses_directory(default_folder)
    # while True:
    #     try:
    #
    #
    #
    #     except KeyboardInterrupt:
    #         print("you closed the connection")
    disconnect_to_db(connection, cur)
