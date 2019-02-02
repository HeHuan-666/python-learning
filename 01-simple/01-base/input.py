#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/2/2 14:00
# @Author: lishengdong

name = input("Please input your name:")
# 打印输出有下面三种方法，最常用的是第一种
print('hello {0}'.format(name))
print("hello " + name)
print("hello %s" %name)