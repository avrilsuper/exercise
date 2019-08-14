#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
from config import *
from modules import *
check_time = '''UPDATE test.dl_house_data
SET check_time = curdate()
WHERE
	dl_uuid = '%s' '''


uid = '''SELECT dl_user,dl_uuid FROM test.dl_house_data'''

for z in my_server(uid):
    uuid = z[1]
    ti = '''select curdate()'''
    for x in my_server(ti):
        ##获取数据库当前时间
        checktime = x[0]
        ele_data = '''SELECT id FROM test.ele_day WHERE uuid='%s' AND check_time='%s' '''
        ele_day = my_server(ele_data % (uuid,checktime))
        if ele_day == ():
            yesterday = '''SELECT uuid,ele,ele_time,cz,cz_time FROM test.ele_day_data WHERE uuid ='%s'and check_time=curdate()-1 '''%uuid
            print("yesterday:%s"%yesterday)
            for i in my_server(yesterday):
                yes_ele = float(i[1])
                yes_ele_time = i[2]
                yes_cz = float(i[3])
                yes_cz_time = i[4]
                today = '''SELECT uuid,ele,cz FROM test.ele_day_data WHERE uuid ='%s'and check_time=curdate() '''%uuid
                # print(today)
                for x in my_server(today):
                    tod_ele = float(x[1])
                    if yes_cz_time > yes_ele_time:
                        use_ele = (yes_ele+yes_cz) - (tod_ele+yes_cz)
                        print("tod_ele:%s"%tod_ele)
                        print("yes_cz:%s"%yes_cz)
                        print("yes_ele:%s"%yes_ele)
                        ins_ele = '''INSERT into test.ele_day(uuid,use_ele,check_time) VALUES('%s','%s',curdate())'''
                        my_insert(ins_ele,(uuid,use_ele))
                        my_commit(check_time%uuid)
                    elif yes_cz_time<yes_ele_time:
                        use_ele = yes_ele - tod_ele
                        print("tod_ele:%s"% tod_ele)
                        print("yes_ele:%s"%yes_ele)
                        ins_ele = '''INSERT into test.ele_day(uuid,use_ele,check_time) VALUES('%s','%s',curdate())'''
                        my_insert(ins_ele,(uuid, use_ele))
                        my_commit(check_time%uuid)
        else:
            print('已记录')

print("==========================================")