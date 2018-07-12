# -*- coding:utf8 -*-
from methods.database import *

def select_table(table, column, condition, value):
    sql = "select " + column + " from " + table + " where " + condition + " = '" + value + "'"
    cursor.execute(sql)
    lines = cursor.fetchall()
    return lines

def select_columns(table,column):
    sql = "select " + column + " from " + table
    cursor.execute(sql)
    lines = cursor.fetchall()
    return lines

def insert_row(table,user,pwd,email):
    value = "'" + user +"', '" + pwd + "', '" + email + "'"
    sql = "INSERT INTO " + table +"(username, password, email) VALUES (" + value + ");commit;"
    print(sql)
    data=cursor.execute(sql)
    return data


if __name__ == '__main__':
    data=insert_row(table="users", user="wangyuan5", pwd="wangyuan123", email="wangyuan@163.com")
    print(data)