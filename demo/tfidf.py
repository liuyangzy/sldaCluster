# -*- coding: UTF-8 -*-
# author: liuyang
# date: 2018/5/18
# time: 下午8:44

from __future__ import print_function

from __future__ import print_function
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise        import cosine_similarity
from nltk.stem.lancaster             import LancasterStemmer
from sklearn.cluster import KMeans
import numpy as np

st = LancasterStemmer()

def stemList(lin):
    lout = list()
    for item in lin:
        lout.append(st.stem(is_ascii(item)))
    return lout

def is_ascii(s):
    if all(ord(c) < 128 for c in s):
        return s
    else:
        return "a"

def applyStemming(arg):
    stemmed = list()
    for item in arg:
        stemmed.append(" ".join(stemList(item.split())))
    return stemmed

np.set_printoptions(threshold=np.inf)

def tfidfcluster(corpus_path):
    docNum = 0
    with open(corpus_path) as file:
        train_set = list()
        for line in file:
            train_set.append(line.lower())
            docNum=docNum+1

    train_set_stemmed = applyStemming(train_set)

    vectorizer = CountVectorizer(stop_words='english')
    document_term_matrix = vectorizer.fit_transform(train_set_stemmed)

    tfidf = TfidfTransformer()
    tfidf.fit(document_term_matrix)

    tf_idf_matrix = tfidf.transform(document_term_matrix)

    co_sim_matrix = cosine_similarity(tf_idf_matrix, tf_idf_matrix)

    def runKMeans(num_clusters):
        kmeans_result = KMeans(n_clusters=num_clusters, init='k-means++').fit_predict(co_sim_matrix)
        return kmeans_result

    kmeans_result = runKMeans(20)

    fk = open('train-label.dat', 'w')
    for item in kmeans_result:
        # print(item)
        fk.write(str(item) + "\n")

    fk.close()