# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:50:40 2019

@author: manav
"""

import nltk

import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
print (html)


from bs4 import BeautifulSoup

import urllib.request 
response = urllib.request.urlopen('http://php.net/') 
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
print(text)
tokens = [t for t in text.split()] 
print (tokens)

freq = nltk.FreqDist(tokens) 
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))
    
freq.plot(20, cumulative=False)

from nltk.corpus import stopwords
stopwords.words('english')
clean_tokens = tokens[:] 
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
        
freq = nltk.FreqDist(clean_tokens) 
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))
    

freq.plot(20,cumulative=False)