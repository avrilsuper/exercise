#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

from modules import *
from dl_dump import *


dl_base = '''SELECT dl_uuid,dump_id FROM test.dl_base'''
base = my_server(dl_base)

for i in base:
    uuid = i[0]
    dl_dump = '''SELECT id,dump_ele FROM test.dump_ele WHERE id='%s' '''%i[1]
    for i in my_server(dl_dump):
        dump=i[1]
    dl_user = '''SELECT dl_user FROM test.dl_house_data WHERE dl_uuid='%s' '''
    user = str(my_server(dl_user%uuid))[3:9]
    dl_epid = '''SELECT epid,xnum FROM kddz.dbo.eptouserlist WHERE userid='%s' '''
    d_epid = sql_server(dl_epid%user)
    for x in d_epid:
        epid = x[0]
        xnum = x[1]
        # sql_jc = '''SELECT epid,xnum FROM kddz.dbo.dvcbrecords1 WHERE epid='%s' AND xnum='%s' AND ele<'%s' GROUP BY epid,xnum'''
        sql_jc = '''
        SELECT top 1 epid,xnum,ele,dtime FROM kddz.dbo.dvcbrecords1 WHERE epid='%s' AND xnum='%s' ORDER BY dtime DESC 
        '''
        my = sql_server(sql_jc%(epid,xnum))
        for z in my:
            my_epid = z[0]
            my_xnum = z[1]
            my_ele = z[2]
            my_dtime = z[3]
            if int(dump)>my_ele:
                sql_cz = '''SELECT top 1 epid,xnum,ele,dtime FROM kddz.dbo.sellelerecords WHERE epid='%s' AND xnum='%s' ORDER BY dtime DESC '''
                cz = sql_server(sql_jc%(my_epid,my_xnum))
                for x in cz:
                    cz_epid = x[0]
                    cz_xnum = x[1]
                    cz_ele = x[2]
                    cz_dtime = x[3]
                    print(cz_dtime)
                    pd = '''SELECT id FROM test.dl_ammeter_user WHERE dl_uuid='%s' AND dl_status_date='%s' '''
                    pd_sy = my_server(pd%(uuid,cz_dtime))
                    if pd_sy ==():
                        wy_phone = '''SELECT id,phone FROM test.dl_base WHERE dl_uuid='%s' '''
                        w_phone = my_server(wy_phone%uuid)
                        for c in w_phone:
                            phone = c[1]
                            ins_amm = '''INSERT INTO test.dl_ammeter_user(dl_uuid,dl_status_date,phone,check_time,ele) VALUES('%s','%s','%s',curdate(),'%s')'''
                            amm = my_insert(ins_amm,(uuid,cz_dtime,phone,my_ele))
                            if len(phone) == 0:
                                print('发送邮件','电量剩余：',my_ele)
                            elif len(phone) == 11:
                                print(phone,'电量剩余：',my_ele)
                                # dl_sms(phone,my_ele)
                            elif len(phone) > 11:
                                print(phone[0:11],'电量剩余：',my_ele)
                    else:
                        print('已发送')
            else:
                print("电量充足")