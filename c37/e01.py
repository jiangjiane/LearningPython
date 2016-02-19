#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：__getattr__和 __getattribute__有何区别？
答：1、__getattr__方法只针对未定义属性的获取运行，即那些没有在一个实例上显示以及没有从它的任何类继承的属性
   2、__getattribute__方法针对所有的属性获取运行，不管属性是否定义了。
   3、如果某属性已被定义，__getattr__中的代码可以自由地获取它； 而__getattribute__需要针对所有这样的属性获取使用特定代码以避免循环（它必须把获取指向一个超类以跳过自身）。
'''