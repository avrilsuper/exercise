#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

from modules import *
from dl_dump import *

dump_id = '1'

dl_wu_uuid = '''SELECT dl_uuid,wu_uuid FROM test.dl_wu_uuid'''
uuid = my_server(dl_wu_uuid)
for i in uuid:
    dl_uuid = i[0]
    wu_uuid = i[1]
    dl_id = '''SELECT id,dl_uuid FROM test.dl_base WHERE dl_uuid='%s' '''%dl_uuid
    if my_server(dl_id) == ():
        dl_user = '''SELECT dl_user,dl_uuid FROM test.dl_house_data WHERE dl_uuid='%s' '''
        for x in my_server(dl_user%dl_uuid):
            user=x[0]
            wu_house_num = '''SELECT wu_house_num,wu_uuid FROM test.wu_house_data WHERE wu_uuid='%s' '''
            for z in my_server(wu_house_num%wu_uuid):
                house = z[0]
                wu_phone = '''SELECT name,Mobile FROM JeezZKSG.dbo.jzCustomer WHERE Number='%s' '''
                w_phone = sql_server2(wu_phone%house)
                for c in w_phone:
                    name = c[0]
                    phone = c[1]
                    ins_base = '''INSERT INTO test.dl_base(dl_uuid,phone,dump_id) VALUES('%s','%s','%s')'''
                    my_insert(ins_base, (dl_uuid, phone, dump_id))

    else:
        print("已存在")