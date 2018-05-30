# sldaCluster
An Ensemble Clustering Tool Based on Classified Model



When you use the this library, the precautions is as follows:

1. the first thing is to call the dataProcess() function,
   and the parameter is the text that you are going to process.

2. then if you want to use the word2vec method as the precluster method,
   just call the function w2v_slda, and the parameter is:
    (1)the vectors.bin of your source data
    (2)the path of your source text
    (3)the number of clusters
    (4)the alpha of the slda model

3. if you want to use the tfidf method as the precluster method,
    just call the function tfidf_slda, and the parameter is:
    (1)the path of your source text
    (2)the number of clusters
    (3)the alpha of the slda model


There is an example as follows:
···
if __name__ == '__main__':
    sldaCluster = Util()
    Util.dataProcess('./data/sourceCorpus.txt')
    clusterMethod = input("word2vec or tfidf?")
    if clusterMethod == 'word2vec':
        Util.w2v_slda('./data/vectors.bin', "./data/sourceCorpus.txt", 20, 0.5)
    elif clusterMethod == 'tfidf':
        Util.tfidf_slda("./data/sourceCorpus.txt", 20, 0.5)
···
