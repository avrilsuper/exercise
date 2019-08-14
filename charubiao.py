#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

from modules import *
from config import *
#dump_ele 表插入电量剩余选项
ins_dump = '''INSERT INTO test.dump_ele(dump_ele) VALUES('%s')'''
ele = [(50),(100),(200),(500),(1000)]
for i in ele:
    dump = '''SELECT id FROM test.dump_ele WHERE dump_ele='%s' '''%i
    if my_server(dump) == ():
        my_insert(ins_dump, i)
    else:
        print("dunm_ele已存在")


# #获取电表userid插入数据库
sql_userid = '''SELECT userid,homenum FROM kddz.dbo.eptouserlist WHERE userid is not NULL'''
ins_dluuid = '''INSERT INTO test.dl_house_data(dl_user,dl_uuid) VALUES('%s','%s') '''
for i in  sql_server(sql_userid):
    dl_user = i[0]
    uid = str(uuid.uuid5(namespace, dl_user)).replace('-', '')
    user ='''SELECT dl_user FROM test.dl_house_data WHERE dl_user='%s' '''%dl_user
    if my_server(user) == ():
        my_insert(ins_dluuid,(dl_user,uid))
    else:
        print("dl_user已存在")


##获取物业房间插入数据库
sql_Number = '''SELECT Number,ID FROM JeezZKSG.dbo.jzCustomer  '''
ins_wyuuid = '''INSERT INTO test.wu_house_data(wu_house_num,wu_uuid) VALUES('%s','%s') '''
for i in sql_server2(sql_Number):
    num = i[0]
    uid = str(uuid.uuid5(namespace, num)).replace('-', '')
    wu_house_num = '''SELECT wu_house_num FROM test.wu_house_data WHERE wu_house_num='%s' '''%num
    if my_server(wu_house_num) == ():
        my_insert(ins_wyuuid,(num,uid))
    else:
        print("wu_house_num已存在")



sl_uu = '''SELECT dl_user,dl_uuid FROM test.dl_house_data'''
in_uu = ''' INSERT INTO test.dl_house_uuid(dl_user,dl_uuid) VALUES('%s','%s')'''
for i in my_server(sl_uu):
    dl_user=i[0]
    dl_uuid=i[1]
    sl_hu_user = '''SELECT id FROM test.dl_house_uuid WHERE dl_user='%s' '''%dl_user
    if my_server(sl_hu_user) ==():
        my_insert(in_uu,(dl_user,dl_uuid))
    else:
        print("已存在")



dl_us = '''SELECT id,dl_user FROM test.dl_house_uuid'''
for i in my_server(dl_us):
    user = i[1]
    sl_in = '''SELECT id,name FROM kddz.dbo.userlist WHERE id='%s' '''%user
    for x in sql_server(sl_in):
        house = x[1]
        dl_name = x[1].split("-")
        lltt = {'L': '0101', 'A01': '01', 'A04': '02', 'A14': '03', 'A13': '04', 'A12': '05', 'A03': '06', 'A02': '07',
                'A05': '08', 'A08': '09', 'A11': '10', 'A10': '11', 'A09': '12', 'A07': '13', 'A06': '14'}
        if len(dl_name) == 3:
            xm = dl_name[0]
            lh = dl_name[1]
            fjh = dl_name[2][0:4]
            dl_lh = lltt[xm] + lltt[lh] + fjh
            dl_house = '''UPDATE test.dl_house_uuid SET dl_house='%s' WHERE dl_user='%s' '''
            my_commit(dl_house%(dl_lh,user))

wu_hu = '''SELECT wu_house_num,wu_uuid FROM test.wu_house_data '''
for i in my_server(wu_hu):
    house=i[0].split("-")
    wu_uuid=i[1]
    uui='''SELECT dl_uuid FROM test.dl_wu_uuid WHERE wu_uuid='%s' '''%wu_uuid
    if my_server(uui) == ():
        if len(house) == 3:
            wu_lh = house[0] + house[1] + house[2]
            uu = '''SELECT id,dl_uuid FROM test.dl_house_uuid WHERE dl_house='%s' '''%wu_lh
            for x in my_server(uu):
                dl_uuid=x[1]
                in_uu = '''INSERT INTO test.dl_wu_uuid(dl_uuid,wu_uuid) VALUES('%s','%s') '''
                my_insert(in_uu,(dl_uuid,wu_uuid))
    else:
        print("dl_wu_uuid存在")



