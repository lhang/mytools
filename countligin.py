#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
����ͳ��ͼ��ݸ�������˵�����
'''
import re
#����m_people���Ըı�ͳ�Ƶ��꼶
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
print '����',num_all
print 'ͼ�������',num_lib
print 'content.txt����',line_count_all
print 'ͼ�����Ϣ����',line_count_lib
num = num_all-num_lib
print '�����������',num