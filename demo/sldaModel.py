# -*- coding: UTF-8 -*-
# author: liuyang
# date: 2018/5/18
# time: 下午8:47

from __future__ import print_function
import os

data = "train-data.dat"
label = "train-label.dat"
settings = "./demo/profile/settings.txt"
model_path = "./model"

def sldaModel(alpha, clusterNum):
    os.system(r'./demo/profile/slda '
              + "est"
              + r' '
              + data
              + r' '
              + label
              + r' '
              + settings
              + r' '
              + str(alpha)
              + r' '
              + str(clusterNum)
              + r' '
              + "random"
              + r' '
              + model_path)

