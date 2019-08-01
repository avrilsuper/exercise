#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
import pymssql

servername = '10.0.1.113'
username = 'sa'
password = '123456'

##数据库
def sql_server(sql):
    conn = pymssql.connect(servername, username, password,'test')
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data

#获取电力系统房间号
# dl_sql ='''
# select dad.dl_house_num,dhd.dl_uuid from
# (select dl_house_num, userid from dl_ammeter_date) as dad,
# (select dl_uuid, dl_userid from dl_house_data) as dhd
# where dad.userid=dhd.dl_userid'''
dl_sql='''
select usl.name,dhd.dl_uuid from 
(select name, id from kddz.dbo.userlist) as usl,
(select dl_uuid, dl_userid from dl_house_data) as dhd
where usl.id=dhd.dl_userid
'''
##获取物业系统房间号
wu_sql ='''SELECT wu_house_num,wu_uuid FROM test.dbo.wu_house_data'''
##电力系统分隔符
def dl_FGF(x):
    dlDict = {}
    for i in x:
        dl_data = i[0].split("-")
        lltt = {'L': '0101', 'A01': '01', 'A04': '02', 'A14': '03', 'A13': '04', 'A12': '05', 'A03': '06', 'A02': '07',
                'A05': '08', 'A08': '09', 'A11': '10', 'A10': '11', 'A09': '12', 'A07': '13', 'A06': '14'}
        if len(dl_data) == 3:
            xm = dl_data[0]
            lh = dl_data[1]
            fjh = dl_data[2][0:4]
            dl_lh = lltt[xm]+lltt[lh]+fjh
            dlDict[dl_lh] = i[1]
    return dlDict
##物业系统分隔符
def wu_FGF(x):
    wuDict = {}
    for i in x:
        wu_data = (i[0].split("-"))
        if len(wu_data) == 3:
            wu_lh = wu_data[0]+wu_data[1]+wu_data[2]
            wuDict[wu_lh] = i[1]
    return wuDict

wu = wu_FGF(sql_server(wu_sql))
dl = dl_FGF(sql_server(dl_sql))
print(wu)

##取电力系统和物业系统 房间号->uuid 的交集
def dictt():
    wy_dl = {}
    for i in wu.keys():
        if i in dl.keys():
            wy_dl[wu[i]] = dl[i]
    for x in dl.keys():
        if dl[x] not in wy_dl.values() and x in wu.keys():
            wy_dl[wu[x]] = dl[x]
    return  wy_dl

# sql = """INSERT INTO test.dbo.dl_wu_uuid(wu_uuid) VALUES('%s')"""%s
# sql3= '''INSERT INTO test.dbo.dl_wu_uuid(wu_uuid) SELECT('%s')'''
# conn = pymssql.connect(servername, username, password)
# cursor = conn.cursor()
#
# for i in JJ():
#     print(i)
#     values = i
#     cursor.execute(sql,values)
# conn.close()
##将电力系统和物业系统的UUID写入中间表
def sql2(data):
    for i in data:
        conn = pymssql.connect(servername, username, password)
        cursorr = conn.cursor()
        tsql = """INSERT INTO test.dbo.dl_wu_uuid(wu_uuid,dl_uuid) VALUES('%s','%s')"""% (i,data[i])
        #print(tsql)
        cursorr.execute(tsql)
        conn.commit()
        conn.close()
sql2(dictt())


