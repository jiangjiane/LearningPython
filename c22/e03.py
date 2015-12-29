#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：reload函数和导入有什么关系？
答：默认情况下模块的导入是每个进程只导入一次，而reload函数会强制模块重新被导入。
    重新加载（reload）包括最初导入模块时应用的分析过程和初始化过程，这样就允许在不退出解释器的情况下重新加载已更改的Python模块。有reload调用时，模块应该使用import语句导入。
'''