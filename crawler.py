# -*- coding: utf-8 -*-
__author__ = 'guangshun'


import requests
from bs4 import BeautifulSoup as bs

titles = []
contents = []

def getSoup(url):
    r = requests.get(url)
    return bs(r.text, 'html.parser')


def getTitle(soup):
    for h2 in soup.find_all('h2'):
        titles.append(h2.a['title'])


for index in range(2, 10):
    url = "http://www.zhihujingxuan.com/index-p%s.html" % index
    soup = getSoup(url)
    getTitle(soup)

if __name__ == '__main__':
    for i in range(len(titles)):
        print i, titles[i]
