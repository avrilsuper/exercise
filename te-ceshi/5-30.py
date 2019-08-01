#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sun
#dict
# d = {'k':'v'} #对象
# print(dict)   #类
# print(d)

# ##自定义类（）
# class 类名():
#     pass
#
# class 类名:
#     属性 = 'a'
# print(类名.属性)
# #类名的作用就是操作属性，查看属性

#
#
# class Person:
#     def __init__(self,*args):
#         self.name = args[0]
#         self.hp = args[1]
#         self.aggr = args[2]
#         self.sex = args[3]
#     def walk(self):
#         print("%s走走走"%self.name)
#
# alex = Person('狗剩',100,1,'不详')
# print(alex.__dict__)
# Person.walk(alex) #调用方法 类名.方法名（对象名）
# alex.walk()#对象.方法名
# #对象 = 类名()
#过程：
    #类名() 首先会创造一个对象，创建一个self变量
    #调用init方法，类名括号里的参数会被这里介绍
    #执行init方法
    #返回self
#对象能做的事：
    #查看属性
    #调用方法
    #__dict__对应对象的增删改查可以通过字典的语法进行
#类名能做的事：
    #实例化
    #调用方法：需要自己传递self参数
    #调用类中的属性，也就是静态属性
    #__dict__对于类中的名字只能看不能操作


# class Person:            #类名
#     country = 'China'    #创造了一个只要这个类就一定有的属性
#                          #类属性，静态属性
#     def __init__(self,*args):   ##初始化方法，self是对象，是一个必须传的参数
#         self.name = args[0]
#         self.hp = args[1]
#         self.aggr = args[2]
#         self.sex = args[3]
#     def walk(self):   #方法，一般情况下必须传self参数，且必须卸载第一个
#                      #后面还可以传其他参数
#         print("%s走走走"%self.name)
# print(Person.country)   #类名，可以查看类中的属性，不需要实例化就可以查看
#
# class Person:
#     def __init__(self,*args):
#         self.name = args[0]
#         self.hp = args[1]
#         self.aggr = args[2]
#         self.sex = args[3]
#     def walk(self):
#         print("%s走走走"%self.name)
#
# alex = Person('狗剩',100,1,'不详')
# print(alex.__dict__)
# print(alex.__dict__['name'])
# alex.__dict__['name'] = '二狗'
# print(alex.__dict__['name'])
# print(alex.name)
# #一般用下边方式
# alex.name = '狗剩'
# print(alex.name)
# print(alex.__dict__['name'])


string = "good"  # 类型为字符串
print("string=%s" % string)  # 输出的打印结果为 string=good
