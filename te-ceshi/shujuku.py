#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
import re
import pymssql
import uuid
name ="dsgdl"

namespace = uuid.NAMESPACE_URL
# servername = '192.168.31.167'
servername = '10.0.1.113'
username = 'sa'
password = '123456'
conn = pymssql.connect(servername,username,password)
cursor = conn.cursor()
#创建dl_data表
cursor.execute('''
SELECT top 10 name FROM kddz.dbo.userlist
''')
data = cursor.fetchall()
print(type(data))
print(data)
cursor.close()
tmpData = str(data).split("-")
# tm = re.split('[)(-]',str(data))
# tmD = str(data).partition('-')
#print(tmpData)
lltt = {'L':'010','A01':'01','A04':'02','A14':'03','A13':'04','A12':'05','A03':'06','A02':'07','A05':'08','A08':'09','A11':'10','A10':'11','A09':'12','A07':'13','A06':'14'}
ll = tmpData[0][3]
nn = tmpData[1]
mm = tmpData[2][0:4]
#print(mm)
print(lltt[ll]+lltt[nn]+mm)
print(type(tmpData))
zfc = "".join(tmpData)
print(zfc)
print(zfc[3:11])
print(zfc[18:26])
# ll1=tmpData[3][3]
# nn1 = tmpData[4]
# mm1 = tmpData[5][0:4]
# print(lltt[ll1]+lltt[nn1]+mm1)


#print(tmpData[0][3])
# if len(tmp.findall(tmp[2])[0]) == 3:
#    pass
# print(tmpData)
# ll=tmpData[0]
# print(ll)