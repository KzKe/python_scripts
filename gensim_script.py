#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gensim_script.py
# @Time      :2020/9/16 10:55 上午
# @Author    :Kangke

'''
https://www.cnblogs.com/pinard/p/7278324.html
'''

from gensim.models import Word2Vec
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

def w2v(dfs,f,L=128):
    '''
    转换序列为w2v
    :param dfs: dataframes
    :param f: 指定的column
    :param L: 序列长度
    :return: 保存训练好的w2v
    '''
    print("w2v",f)
    sentences=[]
    for df in dfs:
        for line in df[f].values:
            sentences.append(line.split())
    print("Sentence Num {}".format(len(sentences)))
    w2v=Word2Vec(sentences,size=L, window=8,min_count=1,sg=1,workers=32,iter=10)
    print("save w2v to {}".format(os.path.join('data',f+".{}d".format(L))))
    pickle.dump(w2v,open(os.path.join('data',f+".{}d".format(L)),'wb'))

if __name__ == "__main__":
    # 每个user的信息已经被转换为序列，可以直接使用
    train_df=pd.read_pickle('data/train_user.pkl')
    test_df=pd.read_pickle('data/test_user.pkl')
    #训练word2vector，维度为128
    w2v([train_df,test_df],'sequence_text_user_id_ad_id',L=128)