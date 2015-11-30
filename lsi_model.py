__author__ = 'guangshun'
from crawler import titles
from process_text import delete_punctuation
from gensim import corpora, models, similarities

# bag of words
dictionary = corpora.Dictionary(delete_punctuation)
# use id instead of word
corpus = [dictionary.doc2bow(text) for text in delete_punctuation]

# calculate tf-idf
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

# get lsi
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=4)
# get index
index = similarities.MatrixSimilarity(lsi[corpus])


# test
# if __name__ == '__main__':
#     print corpus[0]
#     print lsi[corpus[0]]
#     l = list(enumerate(index[lsi[corpus[0]]]))
#     print l
#     # sim = index[lsi[corpus[0]]]
#     # print sim
#     print len(corpus)
#     print titles[l[0][0]]
#     print titles[l[19][0]]
#     print titles[l[5][0]]
