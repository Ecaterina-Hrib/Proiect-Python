import psycopg2
from helping_functions import *

username_db = 'ecaterina'
password_db = '1234'
db_name = 'mydb'


def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database=db_name,
            user=username_db,
            password=password_db,
            port='5432')
        print(connection)
        cursor = connection.cursor()
        return connection, cursor
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


def disconnect_to_db(connection, cursor):
    cursor.close()
    connection.close()


def create_expense(file_path):
    try:
        conn, cursor = connect_to_db()
        data_file_dict = json_to_dict(file_path)
        file_list = file_path.split("/")
        file = file_list[6]
        str_date, epoch = last_modification_file(file_path)
        print("insert file: ", file_path)
        insert_query = """ INSERT INTO expenses (id_file, category, price,last_modification) VALUES (%s,%s,%s,%s)"""
        values_query = (file, data_file_dict['category'], data_file_dict['price'], epoch)
        cursor.execute(insert_query, values_query)
        print("Executed succesfully")
        print("New expense added")
        conn.commit()
        cursor.close()
        return True
    except (Exception, psycopg2.Error) as e:
        print("error: ", e)
    return False


def verify_if_exists(file_path):
    try:
        conn, cursor = connect_to_db()
        print("check if exist file: ", file_path)
        # data_file_dict = json_to_dict(file_path)
        # str_date, epoch = last_modification_file(file_path)
        sql_select = "select * from expenses where id_file=%s "
        cursor.execute(sql_select, file_path)
        records = cursor.fetchone()
        if records is not None:
            return True

    except (Exception, psycopg2.Error) as e:
        print("error: ", e)
    print("File is NOT in records")
    return False


def run_verify():
    try:
        conn, cursor = connect_to_db()
        sql_select = "select * from expenses"
        cursor.execute(sql_select)
        records = cursor.fetchall()
        print(records)
        cursor.close()

    except Exception as e:
        print(e)
