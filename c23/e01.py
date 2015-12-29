#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：模块包目录内的__init__.py文件有何用途？
答：__init__.py文件是用于声明和初始化模块包的。
    1、在进程中第一次导入某目录时，Python会自动运行这个文件中的代码。
    2、其中赋值的变量会变成对应于该目录在内存中所创建的模块对象的属性。
    3、它是必须包含的：如果一个目录中没有包含这个文件，则无法通过包语法导入目录。
'''
