#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
----------------------------------------------
@File    :   mytest.py    
@Contact :   shinezzm@foxmail.com
@Modify Time : 2019-08-22 10:40
@Author : ZHANG
@Version : 1.0 
@Desciption : None
----------------------------------------------
'''

import pickle
with open('./data/Tang_Poetry.pkl', 'rb') as f:
    s = pickle.load(f)

print(s)
print(len(s))
