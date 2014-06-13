#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
这是统计图书馆改密码的人的数量
'''
import re
#更改m_people可以改变统计的年级
m_people = (r'[A-Z]11[0-9]+')

f_all = open('content.txt','r')
f_lib = open('people.txt','r')
num_all = 0
num_lib = 0
line_count_all = 0
line_count_lib = 0
while 1:
	line1 = f_all.readline()
	if line1.strip() == 'END':break
	line_count_all += 1
	if re.search(m_people,line1):
		num_all += 1
for line2 in f_lib:
	line_count_lib += 1
	if re.search(m_people,line2):
		num_lib += 1
print '总数',num_all
print '图书馆数量',num_lib
print 'content.txt行数',line_count_all
print '图书馆信息行数',line_count_lib
num = num_all-num_lib
print '改密码的数量',num