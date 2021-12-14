from database_functions_expense import *
from database_function_target import *


def count_per_needs(category):
    try:
        conn, cursor = connect_to_db()
        if category =='others':
            sql_select = "SELECT SUM(price) from expenses where category = %s or category=''"
            cursor.execute(sql_select, (category,))
        else:
            sql_select = "SELECT SUM(price) from expenses where category = %s"
            cursor.execute(sql_select, (category,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    except Exception as e:
        print(e)


def select_price_and_category():
    try:
        conn, cursor = connect_to_db()
        sql_select = "SELECT category,price from target"
        cursor.execute(sql_select)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as e:
        print(e)
