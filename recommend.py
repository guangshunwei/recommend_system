# coding:utf-8
__author__ = 'guangshun'
import process_text

# lsi_model
# =======================================================================
import lsi_model

for i in range(len(process_text.titles)):
    print i, process_text.titles[i]

print u'请选择一篇自己感兴趣的文章：'

title_id = input()

query_lsi = lsi_model.lsi[lsi_model.corpus[title_id]]
sims = lsi_model.index[query_lsi]
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1]) # increase

print u'你可能喜欢的文章：'
print sort_sims
for i in range(4):
    print sort_sims[i][0], process_text.titles[sort_sims[i][0]]
# =======================================================================
