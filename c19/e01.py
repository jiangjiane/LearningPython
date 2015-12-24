#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：lambda表达式和def语句有什么关系？
答：lambda和def都是用来创建函数对象的，但是lambda是表达式，会返回一个函数对象；而def是语句，会直接将函数对象赋值给函数名。因为lambda是表达式，可以嵌入函数定义中def语法无法出现的地方。从语法上来讲，lambda只允许单个的返回值表达式，因为它不支持语句代码块，因此，不适用于较大的函数。
'''