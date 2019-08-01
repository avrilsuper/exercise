#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun


import datetime
import pymssql


sq_name = '10.0.1.113'
sq_user = 'sa'
sq_pass = '123456'

def sql_server(sql):
    conn = pymssql.connect(sq_name,sq_user,sq_pass)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def sql_dump(sql):
    conn = pymssql.connect(sq_name,sq_user,sq_pass)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(str(data)) == 9:
        dl_dump = str(data)[3:5]
    elif len(str(data)) == 10:
        dl_dump = str(data)[3:6]
    elif len(str(data)) == 11:
        dl_dump = str(data)[3:7]
    conn.close()
    return  dl_dump
    # return data

s_dump = '''SELECT dump_ele FROM test.dbo.dl_dump WHERE id='1' '''
num = str(sql_dump(s_dump))
if len(num) == 9:
    dl_dump = num[3:5]
elif len(num) == 10:
    dl_dump = num[3:6]
elif len(num) == 11:
    dl_dump = num[3:7]


def sql_sele(sql,data):
    conn = pymssql.connect(sq_name,sq_user,sq_pass)
    cursor = conn.cursor()
    cursor.execute(sql%data)
    data = cursor.fetchall()
    conn.close()
    return  data

def sql_sele2(sql,data):
    conn = pymssql.connect(sq_name,sq_user,sq_pass)
    cursor = conn.cursor()
    cursor.execute(sql%data)
    conn.close()


#选择电量剩余指数
s_dump = '''SELECT dump_ele FROM test.dbo.dl_dump WHERE id='1' '''

##查询电量剩余 电表号和子表号
sql = '''
SELECT dv1.epid,dv1.xnum FROM
(SELECT  * FROM kddz.dbo.dvcbrecords1 
WHERE ele<'%s') as dv1
GROUP BY all epid,xnum
'''
ammeter = sql_sele(sql,sql_dump(s_dump))



for i in ammeter:
    epid = i[0]
    xnum = i[1]
    ##获取电表剩余电量时间
    s_dtime = '''SELECT TOP 1 dtime FROM kddz.dbo.dvcbrecords1  WHERE epid='%s' AND xnum='%s' ORDER BY dtime DESC '''
    d_time = str(sql_sele(s_dtime,(epid,xnum)))
    d_year = d_time[20:31]
    d_hour = d_time[33:42]
    yea = d_year.replace(', ','-')
    hou = d_hour.replace(', ',':')
    ds_time = yea+ ' '+ hou
    ## 获取电表对应的userid
    s_userid='''SELECT userid FROM kddz.dbo.eptouserlist WHERE epid='%s' AND xnum='%s' '''
    userid = str(sql_sele(s_userid,(epid,xnum)))[3:9]
    # print('获取电表对应的userid')
    ##获取电表的uuid
    s_d_uuid = '''SELECT dl_uuid FROM test.dbo.dl_house_data WHERE dl_userid='%s' '''
    d_uuid = str(sql_sele(s_d_uuid,userid))[3:39]
    ##获取物业对应的UUID
    s_w_uuid = '''SELECT wu_uuid FROM test.dbo.dl_wu_uuid WHERE dl_uuid='%s' '''
    if sql_sele(s_w_uuid,d_uuid) != []:
        w_uuid =str(sql_sele(s_w_uuid,d_uuid))[3:39]
        # print('获取物业对应的UUID')
        ##获取对应物业的房间号
        s_w_house = '''SELECT wu_house_num FROM test.dbo.wu_house_data WHERE wu_uuid='%s' '''
        w_house = str(sql_sele(s_w_house,w_uuid))[3:15]
        # print('获取对应物业的房间号')
        ##获取房间对应的使用者信息
        s_w_data = '''SELECT Name,Mobile,UrgentPhone FROM JeezZKSG.dbo.jzCustomer WHERE Number='%s' '''
        w_data = sql_sele(s_w_data,w_house)
        w_user = w_data[0][0]
        w_phone = w_data[0][1]
        w_U_phone = w_data[0][2]
        # print('获取房间对应的使用者信息')
        ##查询上次是否发生信息
        sq_date = '''SELECT id FROM test.dbo.dl_ammeter_user WHERE dl_uuid='%s' AND dl_status_date='%s' '''
        if sql_sele(sq_date,(d_uuid,ds_time)) == []:
            # print('meiyou')
            ##插入信息
            sq_inse = '''INSERT INTO test.dbo.dl_ammeter_user(dl_uuid,dl_status_date,photo) VALUES('%s','%s','%s') ''' % (
            d_uuid, ds_time,w_phone)
            sql_server(sq_inse)
            ##查询电话
            # print(w_phone)
        else:
            print('存在')
    else:
        pass
#
#
#
# def main():
#     print('123')
#
#
# if __name__ =="__main__":
#     main()
#     print('23')