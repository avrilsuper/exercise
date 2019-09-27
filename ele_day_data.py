#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
from datetime import datetime
from config import *
from modules import *


all_ammeter=sql_server('''SELECT distinct epid,xnum FROM kddz.dbo.dvcbrecords1''')
'''获取所有的电表epid和xnum'''
for i in all_ammeter:
    epid=i[0]
    xnum=i[1]
    print(epid)
    print(xnum)
#     cz_date=sql_server('''SELECT
# 	ele,
# 	dtime
# FROM
# 	kddz.dbo.sellelerecords
# WHERE
# 	epid = '%s'
# AND xnum = '%s'
# AND dtime > CAST(GETDATE()-1 as date)
# AND dtime < CAST(GETDATE() as date) '''%(epid,xnum))
    cz_date = sql_server('''SELECT
    	ele,
    	dtime
    FROM
    	kddz.dbo.sellelerecords
    WHERE
    	epid = '%s'
    AND xnum = '%s'
    AND dtime > '2019-06-20'
    AND dtime < '2019-06-21' ''' % (epid, xnum))
    print('cz_data')

#     sy_date=sql_server('''SELECT
# 	ele,
# 	dtime
# FROM
# 	kddz.dbo.dvcbrecords1
# WHERE
# 	epid = '%s'
# AND xnum = '%s'
# AND dtime < CAST (GETDATE() AS DATE)
#  AND dtime > CAST(GETDATE()-1 as date) '''%(epid,xnum))
    sy_date = sql_server('''SELECT
    	ele,
    	dtime
    FROM
    	kddz.dbo.dvcbrecords1
    WHERE
    	epid = '%s'
    AND xnum = '%s'
    AND dtime < '2019-06-21'
     AND dtime > '2019-06-20' ''' % (epid, xnum))
    for e in sy_date:
        ele=e[0]
        ele_time=e[1]
        ele_jc=my_server('''SELECT
	id
FROM
	test.ele_data
WHERE
	epid = '%s'
AND xnum = '%s'
AND ele = '%s'
AND dtime = '%s' '''%(epid,xnum,ele,ele_time))
        ele_ins = '''INSERT INTO test.ele_data (
                	use_type,
                	epid,
                	xnum,
                	ele,
                	dtime,
                	check_time
                )
                VALUES
                	(
                		'1',
                		'%s',
                		'%s',
                		'%s',
                		'%s',
                		NOW()
                	) ''' % (epid, xnum, ele, ele_time)
        if ele_jc == ():
            my_commit(ele_ins)
        else:
            print('ele已记录')
            print(epid,xnum,ele,ele_time)
    print('aaaa')
    for c in cz_date:
        print('充值信息')
        print(c)
        print('1111')
        cz=c[0]
        cz_time=c[1]
        cz_jc=my_server('''SELECT
	id
FROM
	test.ele_data
WHERE
	epid = '%s'
AND xnum = '%s'
AND used = '%s'
AND dtime = '%s' '''%(epid,xnum,cz,cz_time))

        cz_ins = '''INSERT INTO test.ele_data (
        	use_type,
        	epid,
        	xnum,
        	used,
        	dtime,
        	check_time
        )
        VALUES
        	(
        		'2',
        		'%s',
        		'%s',
        		'%s',
        		'%s',
        		NOW()
        	) ''' % (epid, xnum, cz, cz_time)
        if cz_jc == ():
            my_commit(cz_ins)
        else:
            print('cz已记录')
    jl=my_server('''SELECT
    	use_type,
    	used,
    	ele
    FROM
    	test.ele_data
    WHERE
    	epid = '%s'
    AND xnum = '%s'
    AND dtime > date_sub(curdate(),interval 1 day)
    AND dtime < curdate()
    ORDER BY
    	dtime '''%(epid,xnum))
    sy = my_server('''SELECT
	id
FROM
	test.ele_data_day
WHERE
	epid = '%s' and  xnum = '%s' and check_time > date_sub(curdate(),interval 1 day) and check_time<CURDATE() '''%(epid,xnum))
    '''查询上次剩余'''
    ele = 0
    if sy == ():
    #     e = sql_server('''SELECT
    #     TOP 1 ele
    # FROM
    #     kddz.dbo.dvcbrecords1
    # WHERE
    #     epid = '%s'
    # AND xnum = '%s'
    # AND dtime > CAST(GETDATE()-1 as date)
    # AND dtime < CAST(GETDATE() as date)
    # ORDER BY
    #     dtime DESC '''%(epid,xnum))
        e = sql_server('''SELECT
        TOP 1 ele
    FROM
        kddz.dbo.dvcbrecords1
    WHERE
        epid = '%s'
    AND xnum = '%s'
    AND dtime > '2019-06-20'
    AND dtime < '2019-06-21'
    ORDER BY
        dtime DESC '''%(epid,xnum))
        if e ==[]:
#             ele = sql_server('''SELECT
# 	TOP 1 ele
# FROM
# 	kddz.dbo.dvcbrecords1
# WHERE
# 	epid = '%s'
# AND xnum = '%s'
# AND dtime > CAST (GETDATE() - 2 AS DATE)
# AND dtime < CAST (GETDATE() - 1 AS DATE)
# ORDER BY
# 	dtime DESC '''%(epid,xnum))[0][0]
                ele = sql_server('''SELECT
        	TOP 1 ele
        FROM
        	kddz.dbo.dvcbrecords1
        WHERE
        	epid = '%s'
        AND xnum = '%s'
        AND dtime > '2019-06-20'
        AND dtime < '2019-06-21'
        ORDER BY
        	dtime DESC ''' % (epid, xnum))[0][0]
        else:
            ele=e[0][0]
        '''查询昨日最后一次电量'''
    else:
#         ele = my_server('''SELECT
# 	ele
# FROM
# 	test.ele_data_day
# WHERE
# 	epid = '%s'
# AND xnum = '%s'
# AND check_time > date_sub(curdate(),interval 1 day)
# AND check_time < curdate() '''%(epid,xnum))[0][0]
        ele = my_server('''SELECT
	ele
FROM
	test.ele_data_day
WHERE
	epid = '%s'
AND xnum = '%s'
AND check_time > '2019-06-20'
AND check_time < '2019-06-21' '''%(epid,xnum))[0][0]
        '''查询上次剩余'''
#     abc = my_server('''SELECT
# 	use_type,
# 	used,
# 	ele
# FROM
# 	test.ele_data
# WHERE
# 	epid = '%s'
# AND xnum = '%s'
# AND dtime > date_sub(curdate(),interval 1 day)
# AND dtime < curdate() '''%(epid,xnum))
    abc = my_server('''SELECT
    	use_type,
    	used,
    	ele
    FROM
    	test.ele_data
    WHERE
    	epid = '%s'
    AND xnum = '%s'
    AND dtime > '2019-06-20'
    AND dtime < '2019-06-21' ''' % (epid, xnum))
    shiyong = 0
    shengyu = 0
    z = 0
    for i in abc:
        print(i)
        type_id = i[0]
        if z == 0:
            if type_id == 1:
                shiyong = ele - i[2]
                shengyu = i[2]
                z = z+1
                tx = '''z=0, 
                shiyong = ele :'%s' - '%s'
                shengyu = '%s' 
                        '''
            elif type_id == 2:
                shengyu = shiyong
                shiyong = ele + i[1]
                z = z + 1
        if z >0:
            if type_id == 1:
                shiyong = shengyu -  i[2]
                shengyu = i[2]
                z = z+1
            elif type_id == 2:
                shengyu = shengyu
                shiyong = shiyong +i[1]
                z = z + 1
    print("剩余")
    print(shengyu)
    print("使用")
    print(shiyong)
#     ins_jc = my_server('''SELECT
# 	id
# FROM
# 	test.ele_data_day
# WHERE
# 	epid = '%s'
# AND xnum = '%s'
# AND check_time > CURDATE()
# AND check_time < date_sub(curdate(),interval -1 day)'''%(epid,xnum))
    ins_jc = my_server('''SELECT
    	id
    FROM
    	test.ele_data_day
    WHERE
    	epid = '%s'
    AND xnum = '%s'
    AND check_time > '2019-06-20'
    AND check_time < '2019-06-21' ''' % (epid, xnum))
    if ins_jc ==():
        ins_ele =my_commit( '''INSERT INTO test.ele_data_day (
	epid,
	xnum,
	used,
	ele,
	check_time
)
VALUES
	('%s', '%s', '%s', '%s', NOW()) '''%(epid,xnum,shiyong,shengyu))
    else:
        print('已记录')


