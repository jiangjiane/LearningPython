#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
在管理类方面，类装饰器如何与元类重叠？

答：两者都是在class语句的末尾自动触发，都可用于管理类。
    区别在于，装饰器直接扩展并返回最初的类对象，元类在创建一个类之后扩展它。
"""