#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
----------------------------------------------
@File    :   config.py.py    
@Contact :   shinezzm@foxmail.com
@Modify Time : 2019-08-22 10:05
@Author : ZHANG
@Version : 1.0 
@Desciption : None
----------------------------------------------
'''

# train
EPOCH = 5
BATCH_SIZE = 1
LR = 0.01  # 学习率
LOG_BATCH_NUM = 5  # 日志打印频率

# test
MODEL_PATH_RNN = './model/RNN_005.pth'  # rnn模型位置
