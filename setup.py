# -*- coding: UTF-8 -*-
# author: liuyang
# date: 2018/5/26
# time: 下午5:09

from __future__ import print_function
#coding=utf-8
from distutils.core import setup
# 库名 / 版本 / 描述 / 项目地址 / 作者 / 作者邮箱 / 协议 / 关键词 / 模块列表
setup(name="sldaCluster",
      version="1.0.1",
      description="my python",
      url='',
      author="liuyang",
      author_email='1716401503@qq.com',
      license='MIT',
      keywords='python',
      packages = ['demo'],
      package_dir = {'demo':'demo'},
      package_data = {'demo':['profile/*']},
      py_modules=['demo.tfidf', 'demo.word2vec', 'demo.sldaModel', 'demo.Main']
      )