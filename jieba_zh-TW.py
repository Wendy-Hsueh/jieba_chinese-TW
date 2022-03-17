#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Library
import jieba
import pandas as pd
import numpy as np
from collections import defaultdict
import os, io, re


# In[2]:


# read file
df =  pd.read_csv('./data_20211014.csv', index_col = None, encoding = 'utf-8-sig')
df


# In[3]:


# read specified field
texts = list(df.content)
# calculate word frequency
frequency = defaultdict(int)
seg_list = [[],[],]
texts_list = []
stopWords = []
cnt = 0
# read dictionary and stopwords
jieba.load_userdict('./jieba_dict/userDict.txt')
with open('./jieba_dict/stopwords.txt', encoding = 'UTF-8') as f:
    stop_words = f.read().splitlines()
    stopWords.append(stop_words)
for text in texts:
    # remove english and numbers
    text = re.sub("[A-Za-z0-9\,\。]", "", text)
    if type(text) != float:
        texts_list.append(text)
for text in texts_list:
    text = jieba.cut(text, cut_all=False)
    for token in text:
        frequency[token]+=1
        if token in stopWords[0]:
            pass
        else:
            if len(token) >= 2 and frequency[token] >= 2 :
                seg_list[cnt].append(token)
                
            else:
                pass
       
    seg_list.append([])
    cnt+=1 

print(len(seg_list))
print(seg_list)

