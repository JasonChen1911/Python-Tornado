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



if __name__ == '__main__':
    data = select_table(table="users", column="*", condition="username", value="chenyj")
    print(data)