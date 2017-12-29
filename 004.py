# coding:utf-8
"""1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．"""

import nltk
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.replace('.', '')
tokens = nltk.word_tokenize(str)
dict = {}

for i, j in enumerate(tokens):
    if {i} == 0 or 4 or 5 or 6 or 7 or 8 or 14 or 15 or 18:
        dict[j] = j[0]
    else:
        dict[j] = j[1]

dict_new = []

for word in tokens:
    val = dict[word]
    dict_one = {
        word:val
    }
    dict_new.append(dict_one)

print(dict_new)