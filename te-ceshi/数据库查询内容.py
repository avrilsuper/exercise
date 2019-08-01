#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
import pymssql
import pymysql
import cx_Oracle

# from config import *


# conn = cx_Oracle.connect('ststem/123456@localhost/testdb')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM STUDENT_TB")
# rows = cursor.fetchall()  # 得到所有数据集
# print(rows)
# exit()
sql_database='''SELECT name,dbid FROM  master..sysdatabases WHERE name NOT IN ( 'master', 'model', 'msdb', 'tempdb', 'northwind','pubs' )'''
mysql_database = '''show databases'''
sql_table = '''
USE %s
SELECT * FROM SYSOBJECTS WHERE TYPE='U'
'''
mysql_table = '''
select TABLE_CATALOG,table_name 
from information_schema.tables 
where table_schema='%s'
'''
host = input('请输入服务器IP')
user = input('请输入服务器账号')
pas = input('请输入服务器密码')

va1= int(input('选择数据库类型（1,sqlserver;2,mysql;3,oracle）：'))

def sql_server(sql):
    '''
    sqlserver连接处理
    :param sql:
    :return:
    '''
    conn = pymssql.connect(host, user, pas)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    # print(data)
    return data

def mysql_server(sql):
    '''
    mysql连接处理
    :param sql:
    :return:
    '''
    conn = pymysql.connect(host, user, pas)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    # print(data)
    return data

def oracle_server(sql):
    '''
    cx_Oracle连接处理
    :param sql:
    :return:
    '''
    conn = cx_Oracle.connect(host, user, pas)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    # print(data)
    return data

if va1==1:
    for i in sql_server(sql_database):
        database = (i[0])
        for x in sql_server(sql_table%database):
            table = x[0]
            sq111 = '''SELECT * FROM %s.dbo.%s '''
            for x in sql_server(sq111%(database,table)):
                print(x)
                print("数据库:%s,表:%s"%(database,table))

elif va1 == 2:
    for i in mysql_server(mysql_database):
        database = str(i)[2:len(str(i))-3]
        for x in mysql_server(mysql_table%database):
            table = x[1]
            print(table)
            sql222 = '''select * from %s.%s'''
            for z in mysql_server(sql222%(database,table)):
                print(z)
                print("数据库:%s,表:%s" % (database, table))

