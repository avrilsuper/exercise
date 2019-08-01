#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun


from config import *
import pymysql
import pymssql
import uuid


def my_server(sql):
    '''
    mysql 连接处理
    :param sql:
    :return:
    '''
    conn = pymysql.connect(mySqlName,myUser,myPass)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data


sql = '''SELECT * FROM test.wu_house_data'''

def wu():
    wu_Dict = {}
    for i in my_server(sql):
        wu_Dict[i[0]]=i[1]
        print(wu_Dict)
wu()