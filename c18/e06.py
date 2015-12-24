#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：举出三种以上函数和调用者能够交流结果的方法
答： 可以利用return语句返回数据，传入可变参数或是利用全局变量等方法；全局变量除了很特殊的情况如多线程编程等外一般很少应用，因为这会让代码难以理解和使用，return语句通常是最好的选择。除此之外，也可以令函数和系统组件进行通信，例如文件和套接字。
'''