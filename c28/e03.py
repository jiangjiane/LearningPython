#! /usr/bin/python3
# -*- coding:utf8 -*-

﻿'''
问：类为什么可能会需要手动调用超类中的__init__方法？
答：如果类定义了自身的__init__构造函数，但是也必须启动超类的__init__构建其代码，就可能会需要手动调用超类的__init__方法（通过这种嵌套的方式可以减少代码冗余性，比直接复制粘贴超类中构造函数的主体更利于日后的维护）。Python本身只会自动执行一个构造函数，即最底层的那个。超类的构造函数是通过类名称来调用，手动传入self实例：Superclass.__init__(self,...)。
'''
