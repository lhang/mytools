#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
这是一个从命令行输入文件，统计文件行数的工具
'''
import sys
count = 0
for block in sys.stdin:
	count += 1
print '行数',count