#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

# class Course:
#     language = 'Chinese'
#     def __init__(self,teacher,name,period,price):
#         self.teacher = teacher
#         self.name = name
#         self.period = period
#         self.price = price
#
# python = Course('egon','python','6 months',2000)
# linux = Course('oldboy','linux','6 mouths',2000)
#
# # print(python.language)
# # print(linux.language)
# python.language = 'english'
# print(Course.language)
# print(python.language)
# print(linux.language)



import re
import pymssql
import uuid
name ="dsgdl"

namespace = uuid.NAMESPACE_URL

uid = (uuid.uuid5(namespace,"%s" % (name)))



serverName = "10.0.1.113"
userName = "sa"
passWod = "123456"
conn = pymssql.connect(serverName,userName,passWod)
def runsql(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data

sql = """
INSERT INTO test.dbo.dl_ammeter_date(dl_uuid) VALUES(123)
"""

print(runsql(sql))



