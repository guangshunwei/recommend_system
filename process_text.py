# coding:utf-8
__author__ = 'guangshun'

from crawler import titles
import jieba
from gensim import corpora, models, similarities
# tokenize titles
tokenize_titles = [[word for word in jieba.cut(title)] for title in titles]

# delete the punctuation
punctuation = [',', '.', '!', '?', '，', '。', '！', '？', '、', '？']
delete_punctuation = [[word for word in t if not word.encode('utf-8') in punctuation] for t in tokenize_titles]
