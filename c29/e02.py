#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：哪两种运算符重载方法处理打印，并且在何种环境下处理？
答：__str__和__repr__方法实现对象打印显示。
    二者都由print和str内置函数调用，不同的是后者是在没有__str__的情况下才被调用。__str__通常用于用户友好显示，而__repr__显示对象的编码形式。
'''
