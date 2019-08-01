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
dl_sql='''
SELECT dwu.dl_uuid,whd.wu_house_num,esl.epid,esl.xnum,jzt.name FROM
(SELECT wu_uuid,dl_uuid FROM test.dbo.dl_wu_uuid) as dwu,
(SELECT wu_house_num,wu_uuid FROM test.dbo.wu_house_data) as whd,
(SELECT dl_uuid,dl_userid FROM test.dbo.dl_house_data) as dhd,
(SELECT epid,xnum,userid FROM kddz.dbo.eptouserlist) as esl,
(SELECT name,number FROM JeezZKSG.dbo.jzcustomer) as jzt
WHERE dwu.wu_uuid=whd.wu_uuid and dwu.dl_uuid=dhd.dl_uuid and dhd.dl_userid=esl.userid and jzt.number=whd.wu_house_num 
'''

# def xh(x):
#     for i in x:
#         dl_uuid = i[0]
#         wu_house = i[1]
#         dl_biao = str(i[2])
#         dl_zbiao = str(i[3])
#         wu_name = i[4]
#
#         print(dl_uuid,wu_house,dl_biao+'-'+dl_zbiao,wu_name)
# xh(sql_server(dl_sql))
sql2='''
SELECT usl.name,dhd.dl_uuid,epl.epid,epl.xnum FROM
(SELECT dl_uuid,dl_userid FROM test.dbo.dl_house_data) as dhd,
(SELECT id,name FROM kddz.dbo.userlist) as usl,
(SELECT userid,epid,xnum FROM kddz.dbo.eptouserlist) as epl
WHERE dhd.dl_userid=usl.id and epl.userid=dhd.dl_userid
'''
def xh(x):
    for i in x:
        name = i[0]
        uuid = i[1]
        epid = str(i[2])
        zepid= str(i[3])


        print(name,uuid,epid+'-'+zepid)
xh(sql_server(sql2))