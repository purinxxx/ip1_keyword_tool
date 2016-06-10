#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

f = open('katati.txt', 'r')
cnt = 0


def imagetitle(raw):
	s = re.search(r'.*\/(.*)\.jpg', raw)
	if s is not None:
		return s.group(1)

for line in f:
	cnt+=1
	if cnt!=7:
		line = line.rstrip()
	if cnt==1:
		keyword=line
	elif cnt==2:
		sentence=line
	elif cnt==3:
		title=imagetitle(line)
		myurl=line
	elif cnt==4:
		firsturl=line
	elif cnt==5:
		secondurl=line
	elif cnt==6:
		thirdurl=line
	elif line=='\n':
		str='<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n<html data-livestyle-extension="available"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n\n<link rel="stylesheet" type="text/css" href="http://dipale.musabi.ac.jp/y16/ip1/ip1_simple.css">\n<title>%s</title>\n</head>\n\n<body bgcolor="#FFFFFF" text="#333333" link="#3300cc" vlink="#3300cc" alink="#3300cc">\n<div align="center">\n\n<br>\n\n<table width="650" border="0" cellpadding="0" cellspacing="10">\n	<tbody><tr>\n		<td><img src="%s" height="320" width="320" border="0"></td>\n		<td><a href="%s"><img src="%s" height="320" width="320" border="0"></a></td>\n	</tr>\n	<tr>\n		<td><a href="%s"><img src="%s" height="320" width="320" border="0"></a></td>\n		<td><a href="%s"><img src="%s" height="320" width="320" border="0"></a></td>\n	</tr>\n	<tr>\n		<td colspan="2"><span class="j14"><b>【%s】</b></span></td>\n	</tr>\n	<tr>\n		<td colspan="2">\n		<span class="j10">%s</span></td>\n	</tr>\n</tbody></table>\n</div>\n<br><br></body></html>' % (keyword, myurl, firsturl.replace('jpg', 'html'), firsturl, secondurl.replace('jpg', 'html'), secondurl, thirdurl.replace('jpg', 'html'), thirdurl, keyword, sentence)
		h = open(title+'.html', 'w')
		h.write(str)
		h.close()
		cnt=0

