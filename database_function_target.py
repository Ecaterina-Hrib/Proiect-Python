from database_functions_expense import *


def load_target(file_path):
    try:
        conn, cursor = connect_to_db()
        data_file_dict = json_to_dict(file_path)
        str_date, epoch = last_modification_file(file_path)
        print("insert file: ", file_path)
        for key, value in data_file_dict.items():
            insert_query = """ INSERT INTO target ( category, price,last_modification) VALUES (%s,%s,%s)"""
            values_query = (key.lower(), value.lower(), epoch)
            cursor.execute(insert_query, values_query)
            print("Executed successfully")
            print("New expense added")
            conn.commit()
        cursor.close()
        conn.close()
        return True
    except (Exception, psycopg2.Error) as e:
        print("error: ", e)
    return False


def update_target(file_path):
    try:
        conn, cursor = connect_to_db()
        data_file_dict = json_to_dict(file_path)
        str_date, epoch = last_modification_file(file_path)
        for key, value in data_file_dict.items():
            sql_update = "Update target set price=%s, last_modification = %s where category= %s"
            cursor.execute(sql_update, (value, epoch, key.lower()))
            conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(e)


def run_verify_target():
    try:
        conn, cursor = connect_to_db()
        sql_select = "select * from target"
        cursor.execute(sql_select)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records

    except Exception as e:
        print(e)
