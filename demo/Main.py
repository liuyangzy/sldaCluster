# -*- coding: UTF-8 -*-
# author: liuyang
# date: 2018/5/27
# time: 下午2:58

from __future__ import print_function

from word2vec import w2vcluster
from tfidf import tfidfcluster
from sldaModel import sldaModel
import collections
import os
import shutil

class Util:
    def dataProcess(corpus_path):
        f = open("train-data.dat", 'w')
        # corpus_path = './data/sourceCorpus.txt'
        enum = []

        for line in open(corpus_path, 'r', encoding='utf-8').readlines():
            enum.extend(line.strip('\n').split(' '))

        word_ID = {word: i for i, word in enumerate(set(enum))}
        # print(len(word_ID))

        for line in open(corpus_path, 'r', encoding='utf-8').readlines():
            word = []
            word = line.strip('\n').split(' ')
            M = len(set(word))
            f.write(str(M))
            m = collections.Counter(word)
            for i in set(word):
                # print(" " + str(word_ID[i]) + ":" + str(m[i]))
                f.write(" " + str(word_ID[i]) + ":" + str(m[i]))
            # print("\n")
            f.write("\n")

    def w2v_slda(w2v_model_path, corpus_path, clusterNum, alpha):
        w2vcluster(w2v_model_path, corpus_path, clusterNum)
        sldaModel(alpha, clusterNum)
        shutil.copy("train-data.dat", "test-data.dat")
        shutil.copy("train-label.dat", "test-label.dat")
        testdata = "test-data.dat"
        testlabel = "test-label.dat"
        settings = "./demo/profile/settings.txt"

        testmodel_path = "./model/final.model"
        directory = ".//test_out"

        os.system(r'./demo/profile/slda '
                  + "inf"
                  + r' '
                  + testdata
                  + r' '
                  + testlabel
                  + r' '
                  + settings
                  + r' '
                  + testmodel_path
                  + r' '
                  + directory)


    def tfidf_slda(corpus_path, clusterNum, alpha):
        tfidfcluster(corpus_path)
        sldaModel(alpha, clusterNum)
        shutil.copy("train-data.dat", "test-data.dat")
        shutil.copy("train-label.dat", "test-label.dat")
        testdata = "test-data.dat"
        testlabel = "test-label.dat"
        settings = "./demo/profile/settings.txt"

        testmodel_path = "./model/final.model"
        directory = "./test_out"

        os.system(r'./demo/profile/slda '
                  + "inf"
                  + r' '
                  + testdata
                  + r' '
                  + testlabel
                  + r' '
                  + settings
                  + r' '
                  + testmodel_path
                  + r' '
                  + directory)









