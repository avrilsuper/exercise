#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
import  pymysql
import traceback

my_houst = '10.0.0.201'
my_user = 'root'
my_pass = '123'
sql = '''
use test
show tables;
'''
data = '''
CREATE TABLE test.dl_wu_uuid (
    id INT,
    dl_uuid nvarchar(40),
    wu_uuid nvarchar(40),
    INDEX INDEX_dl_uuid_wu_uuid (dl_uuid,wu_uuid)
);
'''
# def my_mysql(sql):
#     conn = pymysql.connect(my_houst,my_user,my_pass)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     print(data)
#     conn.close()
# my_mysql(sql)

class my_sql():
    def __init__(self,*args):
        self.conn = pymysql.connect(my_houst, my_user, my_pass)
        self.cursor = self.conn.cursor()

    def sel(self,sql):
        cur = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            data = self.cursor.fetchall()
            print(data)
        except:
            print('错误')
        finally:
            self.conn.close()

    def insert_sql(self,data):
        cur = self.conn.cursor()
        try:
            cur.execute(data)
            self.conn.commit()
        except:
            print('插入失败')
            self.conn.rollback()
            traceback.print_exc()
        finally:
            self.conn.close()


if __name__=='__main__':
    temp ='''INSERT INTO test.dbo.dl_ammeter_user(dl_uuid,dl_status_date) VALUES(%s,%s)'''
    data = (1),(2)
    sq = my_sql()
    # sq.sel(sql)
    sq.insert_sql(temp,data)





















