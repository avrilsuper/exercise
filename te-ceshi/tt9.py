#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Author  : sun

import pymssql
import re

sq_name = '10.0.1.113'
sq_user = 'sa'
sq_pass = '123456'

def sql_server(sql):
    conn = pymssql.connect(sq_name,sq_user,sq_pass)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data

##查询电量剩余小于50 时间.>2019-06-06的 电表号和子表号
sql = '''
SELECT dv1.epid,dv1.xnum FROM
(SELECT  * FROM kddz.dbo.dvcbrecords1 
WHERE ele<'50' and dtime>'2019-06-06') as dv1
GROUP BY all epid,xnum
'''
##判断状态表是否充值时间和电表UUID
for i in sql_server(sql):


##判断电量剩余时间  和电量充足时间
def pd():
    tmp = []
    for i in sql_server(sql):
        sql_ch = '''SELECT TOP 1 dtime FROM kddz.dbo.sellelerecords WHERE epid='%s' AND xnum='%s'ORDER BY dtime DESC '''%(i[0],i[1])
        cz = (sql_server(sql_ch))
        sql_sy = '''SELECT TOP 1 dtime FROM kddz.dbo.dvcbrecords1 WHERE epid='%s' AND xnum='%s' ORDER BY dtime DESC'''%(i[0],i[1])
        sy = (sql_server(sql_sy))
        if sy>cz:
            tmp.append(i)
    print('电量剩余时间')
    return tmp




##查找电表号对应的房间userid
def select_userid(sql):
    tmp = []
    for i in sql:
        conn = pymssql.connect(sq_name,sq_user,sq_pass)
        cursorr = conn.cursor()
        sql2 = '''SELECT userid FROM kddz.dbo.eptouserlist WHERE epid='%s' AND xnum='%s' '''%(i[0],i[1])
        cursorr.execute(sql2)
        data = cursorr.fetchall()
        conn.close()
        tmp.append(data)
    print('房间uuid')
    return tmp


##获取电量房间对应的uuid
def dl_uuid(x):
    tmp = []
    for i in x:
        a = str(i)
        conn = pymssql.connect(sq_name,sq_user,sq_pass)
        cursorr = conn.cursor()
        sql3 = '''SELECT dl_uuid FROM test.dbo.dl_house_data WHERE dl_userid='%s' '''%a[3:9]
        cursorr.execute(sql3)
        data = cursorr.fetchall()
        conn.close()
        tmp.append(data)
    print('电量uuid')
    return tmp



##获取物业对应电力的UUID
def wy_uuid(x):
    tmp = []
    for i in x:
        a = str(i)
        conn = pymssql.connect(sq_name,sq_user,sq_pass)
        cursorr = conn.cursor()
        sql = '''SELECT wu_uuid FROM test.dbo.dl_wu_uuid WHERE dl_uuid='%s' '''%a[3:39]
        cursorr.execute(sql)
        data = cursorr.fetchall()
        conn.close()
        tmp.append(data)
    print('电力uuid')
    return tmp

##获取物业房间号
def wu_house(x):
    tmp = []
    for i in x:
        if i !=[]:
            a = str(i)
            conn = pymssql.connect(sq_name, sq_user, sq_pass)
            cursorr = conn.cursor()
            sql = '''SELECT wu_house_num FROM test.dbo.wu_house_data WHERE wu_uuid='%s' '''%a[3:39]
            cursorr.execute(sql)
            data = cursorr.fetchall()
            conn.close()
            tmp.append(data)
    print('物业房间号')
    return tmp

def wu_data(x):
    tmp = []
    for i in x:
        a = str(i)
        conn = pymssql.connect(sq_name, sq_user, sq_pass)
        cursorr = conn.cursor()
        sql = '''SELECT name,Number,Mobile,urgentphone FROM JeezZKSG.dbo.jzCustomer WHERE Number='%s' '''%a[3:15]
        cursorr.execute(sql)
        data = cursorr.fetchall()
        conn.close()
        tmp.append(data)
    print('用户')
    return tmp


for i in wu_data(wu_house(wy_uuid(dl_uuid(select_userid(pd()))))):
    name = i[0][0]
    house_num = i[0][1]
    phone = i[0][2]
    jj_phone = i[0][3]
    sql = '''INSERT INTO test.dbo.dl_ammeter_user(dl_status_date,photo) VALUES(GETDATE(),'%s') '''%phone
    print(sql)
    conn = pymssql.connect(sq_name, sq_user, sq_pass)
    cursorr = conn.cursor()
    cursorr.execute(sql)
    conn.commit()
    conn.close()


