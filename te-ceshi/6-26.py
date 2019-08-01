#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
import re
import pymssql
import uuid
name ="dsgdl"

namespace = uuid.NAMESPACE_URL
print(uuid.uuid5(namespace,"%s" % (name)))

lltt = {'A12':'09','A14':'00'}


aa= "L-A14-078(105北京鹤安长泰大药房有限公司）"
tmpData = aa.split('-')
ll = tmpData[1]
nn = tmpData[2][:4]
print(tmpData[2])
print('0101-'+lltt[ll])
tmp = re.compile(r'\d+')
print(tmpData[2])
if len(tmp.findall(tmpData[2])[0]) == 3:
   pass

# serverName = "10.0.1.113"
# userName = "sa"
# passWod = "123456"
# sql='''
# INSERT INTO dl_ammeter_date(dl)
# VALUES (uuid.uuid5(namespace,name))
# '''
#
# conn = pymssql.connect(serverName,userName,passWod,'my_tets')
# cursor = conn.cursor()
# cursor.execute(sql)
# data = cursor.fetchall()
# print(data)
# cursor.close()
