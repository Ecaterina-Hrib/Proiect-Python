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
        values_query = (file, data_file_dict['category'].lower(), data_file_dict['price'], epoch)
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
        sql_select = "select * from expenses where id_file=%s "
        cursor.execute(sql_select, (file_path,))
        records = cursor.fetchone()
        if records is not None:
            print("The file ", file_path, " already exists")
            return True

    except (Exception, psycopg2.Error) as e:
        print("error: ", e)
    print("File is NOT in records")
    return False


def run_verify_expenses():
    try:
        conn, cursor = connect_to_db()
        sql_select = "select * from expenses"
        cursor.execute(sql_select)
        records = cursor.fetchall()
        cursor.close()
        return records

    except Exception as e:
        print(e)


def delete_from_db(file):
    try:
        conn, cursor = connect_to_db()
        sql_delete = """DELETE FROM expenses where id_file = %s"""
        cursor.execute(sql_delete, (file,))
        conn.commit()
        cursor.close()
    except Exception as e:
        print(e)


def update_db_expense(file_path, timestamp):
    try:
        conn, cursor = connect_to_db()
        data_file_dict = json_to_dict(file_path)
        file_list = file_path.split("/")
        file = file_list[6]
        sql_update = """Update expenses set price=%s, category= %s, last_modification = %s where id_file = %s"""
        cursor.execute(sql_update, (data_file_dict['price'], data_file_dict['category'].lower(), timestamp, file))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
