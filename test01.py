# -*- coding: UTF-8 -*-
# author: liuyang
# date: 2018/5/26
# time: 下午11:35

from __future__ import print_function
import collections

f = open("train-data.dat", 'w')

enum = []
wordNum = []

for line in open('./sourceCorpus.txt', 'r', encoding='utf-8').readlines():
    enum.extend(line.strip('\n').split(' '))




word_ID = {word: i for i, word in enumerate(set(enum))}
print(len(word_ID))

for line in open('./sourceCorpus.txt', 'r', encoding='utf-8').readlines():
    word = []
    word = line.strip('\n').split(' ')
    M = len(set(word))
    f.write(str(M))
    m = collections.Counter(word)
    for i in set(word):
        print(" " + str(word_ID[i]) + ":" + str(m[i]))
        f.write(" " + str(word_ID[i]) + ":" + str(m[i]))
    print("\n")
    f.write("\n")