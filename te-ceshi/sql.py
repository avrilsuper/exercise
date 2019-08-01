#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

import pymssql
import uuid

namespace = uuid.NAMESPACE_URL


serverName = "192.168.31.167"
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
INSERT INTO my_tets.dbo.dl_user(dl_uuid) 
VALUES(SELECT name FROM kddz.dbo.userlist)
"""

print(runsql(sql))















