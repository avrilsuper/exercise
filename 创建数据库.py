#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

#-*- coding:utf-8 -*-




from modules import *


##创建数据库
sql_databa ='''
CREATE DATABASE
IF NOT EXISTS test charset utf8;
'''
##创建电量剩余标准表
dump_ele = '''
CREATE TABLE
IF NOT EXISTS test.dump_ele (
	id INT PRIMARY KEY auto_increment,
	dump_ele nvarchar (10)
)
'''
##创建 电表物业uuid对应表 dl_wu_uuid表
dl_wu_uuid = '''
CREATE TABLE
IF NOT EXISTS test.dl_wu_uuid (
	dl_uuid nvarchar (40),
	wu_uuid nvarchar (40)
)
'''
##创建物业房子UUID对应表
wu_house_data = '''
CREATE TABLE
IF NOT EXISTS test.wu_house_data (
	wu_house_num nvarchar (40),
	wu_uuid nvarchar (40)
)
'''
##电力房子对应UUID
dl_house_data = '''
 CREATE TABLE
IF NOT EXISTS test.dl_house_data (
	dl_user nvarchar (40),
	dl_uuid nvarchar (40),
	check_time datetime default   '2001-01-01 01:01:01'  ,
	ele_state nvarchar (10) default '1'
)
 '''
##创建信息表
dl_ammeter_user = '''
CREATE TABLE
IF NOT EXISTS test.dl_ammeter_user (
	id INT PRIMARY KEY auto_increment,
	dl_uuid nvarchar (40),
	dl_status_date datetime,
	phone nvarchar (40),
	sms_status nvarchar (40),
	sms_date datetime,
	ele nvarchar (10),
	check_time datetime
)
'''
dl_base ='''
CREATE TABLE
IF NOT EXISTS test.dl_base (
	id INT PRIMARY KEY auto_increment,
	dl_uuid nvarchar (40),
	phone nvarchar (40),
	phone_sms_status nvarchar (40),
	email nvarchar (40),
	email_status nvarchar (40),
	dump_id INT (11)
)
'''

ele_day = '''
CREATE TABLE
IF NOT EXISTS test.ele_day (
	id INT PRIMARY KEY auto_increment,
	uuid VARCHAR (40),
	use_ele VARCHAR (40),
	check_time datetime
)
'''


ele_day_date ='''
CREATE TABLE
IF NOT EXISTS test.ele_day_data (
	id INT PRIMARY KEY auto_increment,
	uuid VARCHAR (40),
	ele VARCHAR (40),
	ele_time datetime,
	cz VARCHAR (40),
	cz_time datetime,
	check_time datetime
)
'''
dl_house_uuid ='''
CREATE TABLE
IF NOT EXISTS test.dl_house_uuid (
	id INT PRIMARY KEY auto_increment,
	dl_user varchar (40),
	dl_uuid varchar (40),
	dl_house varchar (40)
	)
'''
##创建用户发送状态表

# my_commit(sql_databa)
# my_commit(dl_wu_uuid)
# my_commit(dump_ele)
# my_commit(wu_house_data)
# my_commit(dl_house_data)
# my_commit(dl_ammeter_user)
# my_commit(dl_base)
my_commit(ele_day)
# my_commit(ele_day_date )
# my_commit(dl_house_uuid)

