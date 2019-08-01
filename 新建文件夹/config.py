#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
import uuid
##电力系统
sqlSerName = '10.0.1.113'
sqlUser = 'sa'
sqlPass = '123456'
# sqlSerName = '192.168.1.84'
# sqlUser = 'dlor'
# sqlPass = 'dlora76bv798'


##物业系统
sqlSerName2 = '10.0.1.113'
sqlUser2 = 'sa'
sqlPass2 = '123456'
# sqlSerName2 = '192.168.1.249'
# sqlUser2 = 'xrwyor'
# sqlPass2 = 'xrwy8u66tr567a'
##数据库
mySqlName = '10.0.0.201'
myUser = 'root'
myPass = '123'

#uuid名称
namespace = uuid.NAMESPACE_URL

#电量系统房间号对应
dl_sql='''select name, id from kddz.dbo.userlist '''

dl_house = '''select dl_uuid, dl_userid from test.dbo.dl_house_data'''

