#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun

from modules import *


se_dump = '''select dump_ele from test.dump_ele where id='1' '''
# print(len(str(my_server(se_dump))))

def s_dump(x):
    '''
    获取电力剩余指标
    :param x:
    :return:
    '''
    num = str(my_server(x))
    if len(num) == 10:
        dl_dump = num[3:5]
    elif len(num) == 11:
        dl_dump = num[3:6]
    elif len(num) == 12:
        dl_dump = num[3:7]
    return dl_dump
dump = s_dump(se_dump)



