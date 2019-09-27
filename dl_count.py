from config import *
from modules import *
import time

# uid = my_server('''SELECT dl_user,dl_uuid FROM test.dl_house_data
# ''')
# for i in uid:
#     user,dl_uuid=i
#     yes_db = my_server('''SELECT ele,ele_time,cz,cz_time FROM  test.ele_day_data where uuid='%s' and check_time>'2019-08-23' and check_time< '2019-08-25' '''%dl_uuid)
#     for x in yes_db:
#         yes_ele=x[0]
#         yes_ele_time=x[1]
#         yes_cz=x[2]
#         yes_cz_time=x[3]
#         tod_db=my_server('''SELECT ele,ele_time,cz,cz_time FROM  test.ele_day_data where uuid='%s' and check_time>'2019-08-25' and check_time< '2019-08-27' '''%dl_uuid)
#         for z in tod_db:
#             tod_ele=z[0]
#             tod_ele_time=z[1]
#             if yes_cz is None:
#                 ele = float(yes_ele) - float(tod_ele)
#
#             else:
#                 ele = float(yes_ele)+float(yes_cz)-float(tod_ele)
#
#             ins_ele = '''INSERT into test.ele_day(uuid,use_ele,check_time) VALUES('%s','%s',curdate())'''
#             my_insert(ins_ele,(dl_uuid,ele))
#
# sq = '''SELECT cz,id,cz_time FROM test.ele_day_data WHERE check_time>curdate() GROUP BY cz DESC'''
# x = 0
# for i in  my_server(sq):
#     if i[0] is None:
#         pass
#     else:
#         a = i[0]
#         x = x+int(a)
#
# jc =my_server('''SELECT id FROM test.dl_count WHERE date>curdate() ''')
# ins = ''''''
# if jc == ():
#     print(x)
# else:
#     print("已记录")
##########################################################################################
# x = 0
# sql = '''SELECT id,ele,cz,ele_time,cz_time FROM test.ele_day_data WHERE cz_time>'2019-08-19 00:00:00' AND cz_time<'2019-08-19 23:59:59' '''
# for i in my_server(sql):
#     cz = i[2]
#
#     x = x + int(cz)
# print(x)
#
#
# jc =my_server('''SELECT id FROM test.dl_count WHERE date>'2019-08-19 00:00:00' and date<'2019-08-19 23:59:59' ''')
# if jc ==():
#     ins = ''' INSERT INTO test.dl_count(date,sell,use) VALUES('%s','%s','0')'''
# tim = '2019-08-01','2019-08-02','2019-08-03'
# print(tim)
#----------------------------------------------------------------------------------------------------------------
# for a in range(1,30+1):
#     tim = '2019-06-%s '%a
#
#     cz_data = sql_server('''SELECT epid,xnum,ele FROM kddz.dbo.sellelerecords WHERE dtime>'%s 00:00:00' AND dtime<'%s 23:59:59' '''%(tim,tim))
#     cz_num = 0
#     for i in cz_data:
#         epid,xnum,ele=i
#         cz_num = cz_num+int(ele)
#     print(cz_num)
#     ins_jc = ('''SELECT id FROM test.dl_count WHERE dete>'%s00:00:00' AND dete<'%s23:59:59' ''' % (tim, tim))
#     print(ins_jc)
#     exit()
#     if my_server(ins_jc) is None:
#         ins_cz = my_commit('''INSERT INTO test.dl_count(date,sell) VALUES('%s','%s') '''%(tim+'00:00:01',cz_num))
#     else:
#         print("已插入")

cz_data = sql_server('''SELECT
        se.dd,
        SUM (ele)
    FROM
        (
            SELECT
                ele,
                CONVERT (DATE, dtime) AS dd
            FROM
                kddz.dbo.sellelerecords
        ) AS se
    GROUP BY
        se.dd''')
##每日充值电力

sy_data = my_server('''SELECT
	SUM(ele),
	CAST(check_time AS DATE) AS dd
FROM
	test.ele_data
GROUP BY
	dd ''')
##每日使用电力

for a in range(30, 0, -1):
    '''获取最近30天'''
    ti = time.strftime('%Y-%m-%d', time.localtime(time.time() - 3600 * 24 * a))
    jc = my_server('''SELECT id FROM test.dl_count WHERE cdate='%s' ''' % ti)
    ins_init = '''INSERT INTO test.dl_count(cdate) VALUES('%s')'''
    if jc ==():
        my_insert(ins_init, ti)
    else:
        print("已插入")
    for cz in cz_data:
        tim,cz_ele=cz
        if tim == ti:
            up_cz_data = '''UPDATE test.dl_count SET sell='%s' WHERE cdate='%s' '''%(cz_ele,ti)
            my_commit(up_cz_data)
    for sy in sy_data:
        sy_ele,tim = sy
        if tim == ti:
            up_sy_data= '''UPDATE test.dl_count SET used='%s' WHERE cdate='%s' '''%(sy_ele,ti)
            my_commit(up_sy_data)




