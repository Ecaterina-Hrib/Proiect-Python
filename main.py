from database_functions_expense import *
from database_function_target import *

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

        else:
            print(" load file target.json")
            if 'target' in absolute_path:
                exists = run_verify_target()
                if exists is not None:
                    str_date, epoch = last_modification_file(absolute_path)
                    for record in exists:
                        if epoch > record[len(record) - 1]:
                            print("Update the file ", file)
                            update_target(absolute_path, epoch)

                else:
                    load_target(absolute_path)


if __name__ == '__main__':
    connection, cur = connect_to_db()
    run_verify_expenses()
    load_expenses_directory(default_folder)
    categories_list = ["utilities", "economics", "other", "fun"]
    # while True:
    #     try:
    #
    #
    #
    #     except KeyboardInterrupt:
    #         print("you closed the connection")
    disconnect_to_db(connection, cur)
