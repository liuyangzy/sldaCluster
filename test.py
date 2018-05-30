# -*- coding: UTF-8 -*-
# author: liuyang
# date: 2018/5/26
# time: 下午8:14

from __future__ import print_function
from demo.Main import Util

if __name__ == '__main__':
    demo = Util()
    Util.dataProcess('./data/sourceCorpus.txt')
    # Util.dataProcess('./testData/corpusTest.txt')
    clusterMethod = input("word2vec or tfidf?")
    if clusterMethod == 'word2vec':
        Util.w2v_slda('./data/vectors.bin', "./data/sourceCorpus.txt", 20, 0.5)
        # Util.w2v_slda('./testData/vectorsTest.bin', "./testData/corpusTest.txt", 20, 0.5)
    elif clusterMethod == 'tfidf':
        Util.tfidf_slda("./data/sourceCorpus.txt", 20, 0.5)
        # Util.tfidf_slda("./testData/corpusTest.txt", 20, 0.5)