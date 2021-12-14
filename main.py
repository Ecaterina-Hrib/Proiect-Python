from calcules import *
from database_functions_expense import *
from database_function_target import *
from win10toast import ToastNotifier
import os

default_folder = "D:/_ user ecaaa/Documents/GitHub/Proiect-Python/Expenses/"
username_db = 'ecaterina'
password_db = '1234'
db_name = 'mydb'


def load_expenses_directory(directory_path):
    list_of_files = os.listdir(directory_path)

    for file in list_of_files:

        print(file)
        absolute_path = default_folder + file

        if "target.json" != file and file.endswith(".json"):

            exists = verify_if_exists(file)
            if exists is False:
                print("loading file", file, " to database")
                create_expense(absolute_path)
                calculate_financial_status()

            else:
                all_records = run_verify_expenses()

                for record in all_records:
                    if record[0] not in list_of_files:

                        print("delete file ", record[0])
                        delete_from_db(record[0])

                    else:

                        str_date, epoch = last_modification_file(absolute_path)

                        if epoch > record[len(record) - 1]:
                            print("Update the file ", record[0])
                            update_db_expense(absolute_path, epoch)
                            calculate_financial_status()

        else:
            print(" load file target.json")
            if 'target' in absolute_path:
                exists = run_verify_target()
                if exists is not None:
                    str_date, epoch = last_modification_file(absolute_path)
                    for record in exists:
                        if epoch > record[len(record) - 1]:
                            print("Update the file ", file)
                            update_target(absolute_path)

                else:
                    load_target(absolute_path)


def calculate_financial_status():
    toast = ToastNotifier()
    all_records = select_price_and_category()
    for category_target in all_records:
        print(category_target)
        result = count_per_needs(category_target[0])
        print(result)
        if result is not None:
            if category_target[1] < result:
                toast.show_toast("ALERT EXPENSES", "you excedded over the limit ", duration=20,
                                 icon_path="D:\\_ user ecaaa\\Documents\\GitHub\\Proiect-Python\\download.png")



if __name__ == '__main__':
    run_verify_expenses()
    load_expenses_directory(default_folder)
    categories_list = ["utilities", "economics", "other", "fun"]
    calculate_financial_status()
    # while True:
    #     try:
    #
    #
    #
    #     except KeyboardInterrupt:
    #         print("you closed the connection")
