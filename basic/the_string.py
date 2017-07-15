#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Life is short, you need python.")
print("中文测试正常")
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))