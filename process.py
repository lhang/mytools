#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
����ͳ��ͼ���ͼ���������ĳ���
'''
import re
f = open('list.txt','r')
m_num = re.compile(r' ([0-9]+?)���')
max_num = 0
dict = {}
for line in f:
	if line.find(' -- ') != -1:
		num = re.search(m_num, line)
		num = int(num.group(1))
		if max_num < num:
			max_num = num
	else:
		if line.strip() not in dict:
			dict[line.strip()] = 0
		else:
			dict[line.strip()] += 1
print '����������'+max_num
for j in range(1,max_num+1):
	for i in dict:
		if dict[i] == j:
			print i+':'+str(dict[i])