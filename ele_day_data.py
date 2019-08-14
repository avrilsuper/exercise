#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

from config import *
from modules import *

dl_data = '''SELECT dl_user,dl_uuid,check_time FROM test.dl_house_data'''
ti = '''select curdate()'''
for z in my_server(ti):
    ##获取数据库当前时间
    checktime = z[0]
    for i in my_server(dl_data):
        dl_user = i[0]
        dl_uuid = i[1]
        check_time = i[2]
        if check_time == checktime:
            #检测 此数据是否更新
            print("等于")
            print(dl_uuid)
        else:
            ele_data = '''SELECT id FROM test.ele_day_data WHERE uuid='%s' AND check_time='%s' '''
            ele_day_data = my_server(ele_data%(dl_uuid,checktime))
            if ele_day_data ==():
                dl_epid_xnum = '''SELECT epid,xnum FROM kddz.dbo.eptouserlist WHERE userid='%s' '''%dl_user
                for x in sql_server(dl_epid_xnum):
                    #获取电表号码
                    epid = x[0]
                    xnum = x[1]
                    dl_cz = '''SELECT top 1 ele,dtime FROM kddz.dbo.sellelerecords WHERE epid='%s' AND xnum='%s'ORDER BY dtime DESC'''
                    for c in sql_server(dl_cz%(epid,xnum)):
                        ##获取充值情况
                        cz = c[0]
                        cz_time = c[1]
                        dl_ele = '''SELECT top 1 ele,dtime FROM kddz.dbo.dvcbrecords1 WHERE epid='%s' AND xnum='%s' ORDER BY dtime DESC '''
                        ##获取电表剩余情况
                        for z in sql_server(dl_ele%(epid,xnum)):
                            ele = z[0]
                            ele_time = z[1]
                            print(ele)
                            ##写入电表的剩余和充值
                            ins_day = '''INSERT INTO test.ele_day_data(uuid,ele,ele_time,cz,cz_time,check_time) VALUES('%s','%s','%s','%s','%s',curdate())'''
                            my_insert(ins_day,(dl_uuid,ele,ele_time,cz,cz_time))
            else:
                print('已记录')

