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

lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=80)

index = similarities.MatrixSimilarity(lda[corpus_tfidf])

# test
if __name__ == '__main__':
    print 0, corpus[0]
    print lda[corpus_tfidf[0]]
    l = list(enumerate(index[lda[corpus_tfidf[0]]]))
    st = sorted(l, key=lambda l: -l[1])
    print st
    print len(corpus)
    print st[0][0], titles[st[0][0]]
    print st[1][0], titles[st[1][0]]
    print st[2][0], titles[st[2][0]]
    print st[3][0], titles[st[3][0]]
