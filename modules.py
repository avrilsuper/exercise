#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
from config import *
import pymysql
import pymssql
from pymysql import *
import time
tim = time.strftime("%Y-%m-%d %H:%M:%S")

def sql_server(sql):
    '''
    sqlserver连接处理
    :param sql:
    :return:
    '''
    try:
        conn = pymssql.connect(sqlSerName, sqlUser, sqlPass)
        cursor = conn.cursor()
        cursor.execute(sql)
    except InternalError:
        rizhi('sql问题:'+sql)
    except OperationalError:
        rizhi('连接问题，账号'+sqlSerName)
    else:
        data = cursor.fetchall()
        conn.close()
        # print(data)
        return data
def sql_server2(sql):
    '''
    sqlserver连接处理
    :param sql:
    :return:
    '''
    try:
        conn = pymssql.connect(sqlSerName2, sqlUser2, sqlPass2)
        cursor = conn.cursor()
        cursor.execute(sql)
    except InternalError:
        rizhi('sql问题：'+sql)
    except OperationalError:
        rizhi('连接问题，账号:'+sqlSerName2)
    else:
        data = cursor.fetchall()
        conn.close()
        # print(data)
        return data

def my_server(sql):
    '''
    mysql 连接处理
    :param sql:
    :return:
    '''
    try:
        conn = pymysql.connect(mySqlName,myUser,myPass)
        cursor = conn.cursor()
        cursor.execute(sql)
    except InternalError:
        rizhi('sql问题'+sql)
    except OperationalError:
        rizhi('连接问题,账号：'+mySqlName )
    else:
        data = cursor.fetchall()
        conn.close()
        return data

def my_commit(sql):
    '''
    mysql 数据提交
    :param sql:
    :return:
    '''
    try:
        conn = pymysql.connect(mySqlName,myUser,myPass)
        cursor = conn.cursor()
        cursor.execute(sql)
    except InternalError:
        rizhi('sql问题'+sql)
    except OperationalError:
        print('连接问题,账号：'+mySqlName)
    else:
        conn.commit()
        conn.close()

def my_insert(sql,data):
    '''
    mysql数据插入
    :param sql:
    :param data:
    :return:
    '''
    try:
        conn = pymysql.connect(mySqlName,myUser,myPass)
        cursor = conn.cursor()
        cursor.execute(sql%data)
    except InternalError:
        rizhi('sql问题：'+sql)
    except OperationalError:
        rizhi('连接问题,账号：'+mySqlName)
    else:
        conn.commit()
        conn.close()


def dictt(x,y):
    '''
    取电力系统和物业系统 房间号-uuid 的交集  wu=x dl=y
    :param x:
    :param y:
    :return:
    '''
    wy_dl = {}
    for i in x.keys():
        if i in y.keys():
            wy_dl[x[i]] = y[i]
    for x in y.keys():
        if y[x] not in wy_dl.values() and x in x.keys():
            wy_dl[x[x]] = y[x]
    return  wy_dl


def rizhi(x):
    f = open(r'日志.txt','a+')
    f.write(tim+x+'\n')
    f.close()







import requests
import urllib.request


def dl_sms(phone,ele):
    smsUrl = 'http://send.xiangrenwuye.com/alidayu'
    #smsUrl = ' http://send.simonzhang.net:58000/alidayu'
    # data = requests.get(val(phone,ele))
    # req = requests.post(smsUrl, data)
    # response = requests.get(req)
    returnStatus = requests.post(url=smsUrl, data=val(phone,ele), headers={'Content-Type': 'application/x-www-form-urlencoded'})
    # returnStatus = response.read()
    print(returnStatus)

# dl_sms('18310144977','100')

