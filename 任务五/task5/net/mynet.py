#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
----------------------------------------------
@File    :   mynet.py    
@Contact :   shinezzm@foxmail.com
@Modify Time : 2019-08-22 10:09
@Author : ZHANG
@Version : 1.0 
@Desciption : None
----------------------------------------------
'''
import torch
import torch.nn as nn
import config


class NET_RNN(nn.Module):
    def __init__(self):
        super(NET_RNN, self).__init__()
        self.embedding = nn.Sequential(
            nn.Embedding(num_embeddings=2514, embedding_dim=300)
        )
        self.lstm = nn.Sequential(
            nn.LSTM(300, 300, num_layers=2, batch_first=True)
        )
        self.output = nn.Sequential(
            nn.Linear(300, 2514),
        )

    def forward(self, x):
        x = self.embedding(x)
        out, (_, _) = self.lstm(x)
        x = self.output(out)
        x = x.view(-1, x.size()[-1])
        return x
 
