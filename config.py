#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
import uuid
##电力系统
sqlSerName = '10.0.1.144'
sqlUser = 'sa'
sqlPass = '123456'
# # sqlSerName = '169.253.1.162'
# # sqlSerName = '192.168.1.238'
# sqlSerName = '192.168.1.84'
# sqlUser = 'dlor'
# sqlPass = 'dlora76bv7981'


##物业系统
sqlSerName2 = '10.0.1.144'
sqlUser2 = 'sa'
sqlPass2 = '123456'
# # sqlSerName2 = '169.253.1.162'
# # sqlSerName2 = '192.168.1.238'
# sqlSerName2 = '192.168.1.249'
# sqlUser2 = 'xrwyor'
# sqlPass2 = 'xrwy8u66tr567a'
##数据库
# mySqlName = '10.0.0.201'
# myUser = 'root'
# myPass = '123'
mySqlName = '47.105.102.236'
myUser = 'xrwyDl'
myPass = 'f3i4j6s8f3'

#uuid名称
namespace = uuid.NAMESPACE_URL
##电量系统发送短信
def val(phone,ele):
    values = {'smsType': '翔仁物业', 'smsContext': '{"name":"用户","code":%s}'%ele, \
          'smsNum': phone, 'smsMod': 'SMS_169111985'}
    return values



#电量系统房间号对应
dl_sql='''select name, id from kddz.dbo.userlist '''

dl_house = '''select dl_uuid, dl_userid from test.dbo.dl_house_data'''

