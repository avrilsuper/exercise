#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

from modules import *
from config import *
#dump_ele 表插入电量剩余选项
ins_dump = '''INSERT INTO test.dump_ele(dump_ele) VALUES('%s')'''
ele = [(50),(100),(200),(500),(1000)]
for i in ele:
    my_insert(ins_dump,i)

#
# #获取电表userid插入数据库
sql_userid = '''SELECT userid FROM kddz.dbo.eptouserlist WHERE userid is not NULL'''
def userid(x):
    tp = []
    for i in sql_server(x):
        i_str = str(i)
        userid = i_str[2:8]
        tp.append(userid)
    return tp
ins_dluuid = '''INSERT INTO test.dl_house_data(dl_user,dl_uuid) VALUES('%s','%s') '''
for i in userid(sql_userid):
    uid = str(uuid.uuid5(namespace,i)).replace('-','')
    my_insert(ins_dluuid,(i,uid))




##获取物业房间插入数据库
sql_Number = '''SELECT Number FROM JeezZKSG.dbo.jzCustomer  '''
#
def Number(x):
    tp =[]
    for i in sql_server2(x):
        i_str = str(i)
        if len(i_str) == 17:
            num = i_str[2:14]
            tp.append(num)
    return tp

# ins_wyuuid = '''INSERT INTO test.wu_house_data(wu_house_num,wu_uuid) VALUES('%s',uuid().replace('-', '')) '''
ins_wyuuid = '''INSERT INTO test.wu_house_data(wu_house_num,wu_uuid) VALUES('%s','%s') '''
for i in Number(sql_Number):
    uid = str(uuid.uuid5(namespace, i)).replace('-', '')
    my_insert(ins_wyuuid,(i,uid))




sl_uu = '''SELECT * FROM test.dl_house_data'''
def uu(x):
    '''
    获取电力系统 userid和uuid
    :param x:
    :return:
    '''
    dl_Dict = {}
    for i in my_server(x):
        dl_user = i[0]
        dl_uuid = i[1]
        dl_Dict[dl_user] = dl_uuid
    return dl_Dict


sl_in = '''SELECT id,name FROM kddz.dbo.userlist'''
def dl_FGF(x):
    '''
    获取电力系统userid和房间号
    :param x:
    :return:
    '''
    dl_Dict = {}
    for i in sql_server(x):
        dl_user = i[0]
        dl_name = i[1].split("-")
        lltt = {'L': '0101', 'A01': '01', 'A04': '02', 'A14': '03', 'A13': '04', 'A12': '05', 'A03': '06', 'A02': '07',
                'A05': '08', 'A08': '09', 'A11': '10', 'A10': '11', 'A09': '12', 'A07': '13', 'A06': '14'}
        if len(dl_name) == 3:
            xm = dl_name[0]
            lh = dl_name[1]
            fjh = dl_name[2][0:4]
            dl_lh = lltt[xm] + lltt[lh] + fjh
            dl_Dict[dl_user] = dl_lh
    return dl_Dict

def uuhouse():
    '''
    获取dl房间号和对应的UUID
    :return:
    '''
    dl_Dict = {}
    for i in dl_FGF(sl_in).keys():
        if i in uu(sl_uu).keys():
            dl_Dict[dl_FGF(sl_in)[i]] = uu(sl_uu)[i]
    return dl_Dict


sl_wuhous = '''SELECT wu_house_num,wu_uuid FROM test.wu_house_data'''

def wu_houuu(x):
    '''
    获取物业房间号对应的uuid
    :param x:
    :return:
    '''
    wu_Dict = {}
    for i in my_server(x):

        wu_house = i[0].split("-")
        wu_uuid = i[1]
        if len(wu_house) ==3:
            wu_lh = wu_house[0] + wu_house[1] + wu_house[2]
            wu_Dict[wu_lh] = wu_uuid
    return wu_Dict



wu = wu_houuu(sl_wuhous)
dl = uuhouse()

def dictt():
    '''
    取电力系统和物业系统 房间号->uuid 的交集
    :return:
    '''
    wy_dl = {}
    for i in wu.keys():
        if i in dl.keys():
            wy_dl[wu[i]] =dl[i]
    for x in dl.keys():
        if dl[x] not in wu.values() and x in wu.keys():
            wy_dl[wu[x]] = dl[x]
    return wy_dl
for i in dictt():
    ins_uuid = '''INSERT INTO test.dl_wu_uuid(wu_uuid,dl_uuid) VALUES('%s','%s') '''
    my_insert(ins_uuid,(i,dictt()[i]))
