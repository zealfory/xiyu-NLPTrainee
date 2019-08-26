#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
----------------------------------------------
@File    :   creat_data.py    
@Contact :   shinezzm@foxmail.com
@Modify Time : 2019-08-22 09:54
@Author : ZHANG
@Version : 1.0 
@Desciption : None
----------------------------------------------
'''
import os
import pickle
import re


# 原始text数据转pkl
def creat_data():
    DIR = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists('%s/data/Tang_Poetry.pkl' % DIR):
        print('Data has been created!')
    else:
        print('Data has not been created, start creating data!')
        #path = '%s/data/Tang_Poetry' % DIR
        path = '%s/data' % DIR
        #files = os.listdir(path)
        file = 'poetryFromTang.txt'
        end = 'e'
        texts = []
        # for file in files:
        #     with open(path + '/' + file, mode='r') as f:
        #         text = f.readlines()
        #         if text:
        #             text = text[0]
        #             text = re.sub(pattern='[_（）《》 ]', repl='', string=text)
        #             texts.append(text + end)
        #         else:
        #             continue
        with open(path + os.sep + file, mode = 'r') as f:
            text = f.read()
            for t in text.split('\n\n'):
            #for t in text.split('。'):
                t = t.replace('\n', '')
                t = re.sub(pattern='[_（）《》]', repl='', string=t)
                print(t)
                texts.append(t + end)


        with open('%s/data/Tang_Poetry.pkl' % DIR, mode='wb') as f:
            pickle.dump(texts, f)

        print('Finish creating data!')


if __name__ == '__main__':
    creat_data()
 
