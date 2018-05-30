# sldaCluster
An Ensemble Clustering Tool Based on Classified Model



When you use the this library, the precautions is as follows:

1. the first thing is to call the dataProcess() function,
   and the parameter is the text that you are going to process.

2. then if you want to use the word2vec method as the precluster method,
   just call the function w2v_slda, and the parameter is:
    * the vectors.bin of your source data
    * the path of your source text
    * the number of clusters
    * the alpha of the slda model

3. if you want to use the tfidf method as the precluster method,
    just call the function tfidf_slda, and the parameter is:
    * the path of your source text
    * the number of clusters
    * the alpha of the slda model


There is an example as follows:
```
if __name__ == '__main__':
    sldaCluster = Util()
    Util.dataProcess('./data/sourceCorpus.txt')
    clusterMethod = input("word2vec or tfidf?")
    if clusterMethod == 'word2vec':
        Util.w2v_slda('./data/vectors.bin', "./data/sourceCorpus.txt", 20, 0.5)
    elif clusterMethod == 'tfidf':
        Util.tfidf_slda("./data/sourceCorpus.txt", 20, 0.5)
```

The installation process of the library is as follows(in terminal)：
* cd into directory which contains setup.py file, execute build command
```
python setup.py build
```
* After the build, execute the package command
```
python setup.py sdist
```
* install (local) library
  * extract the compressed package in sdist
  * cd into the decompressed library
  * Execute the installation command：
  (in linux)
  ```
  sudo python setup.py install --record log
  ```
  (in windows)
  ```
  python setup.py install
  ```
  
  
  
