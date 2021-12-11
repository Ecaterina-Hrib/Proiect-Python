import psycopg2
import os

folder = "D:\\_ user ecaaa\\Documents\\GitHub\\Proiect-Python\\Expenses"
username_db = 'ecaterina'
password_db = '1234'
db_name = 'mydb'


def initialise_database(path_directory):
    path_directory = ''


if __name__ == '__main__':
    try:
        while True:
            try:
                connection = psycopg2.connect(
                    host="localhost",
                    database=db_name,
                    user=username_db,
                    password=password_db,
                    port='5432')
                print(connection)
                cursor = connection.cursor()
                # print('PostgreSQL database version:')
                # cursor.execute('SELECT version()')
                # db_version = cursor.fetchone()
                # print(db_version)
                # cursor.close()

                # if connection is not None:
                #     print("exit connection")
                #     connection.close()

            except Exception as e:
                print(e)

    except KeyboardInterrupt:
        print("you closed the connection")
