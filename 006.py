
# coding:utf-8

# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を
#  XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gram
# がXおよびYに含まれるかどうかを調べよ．

import nltk
str1 = "paraparaparadise"
str2 = "paragraph"

ngram_wordlist = []
ngramlist = []

def ngram(str,n,moji):
    str = str.replace('.', '')
    tokens = nltk.word_tokenize(str)
    str = str.replace(' ', '')
    if moji == True:
        for i in range(len(str)):
            if i + n <= len(str):
                ngramlist.append(str[i:i + n])
        else:
            None
    else:

        for i in range(len(tokens) - n + 1):
            unitlist = []
            for j in  range(n):
                unitlist.append(tokens[i+j])
            ngram_wordlist.append(unitlist)
        return ngram_wordlist

ngram(str1,2,True)
print(ngramlist)
x_ = ngramlist

X = set(x_)


ngramlist = []

ngram(str2,2,True)
y_ = ngramlist

Y = set(y_)

print(X | Y)
print(X ^ Y)
print(X - Y)