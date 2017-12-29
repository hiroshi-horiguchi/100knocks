import nltk

strings = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."


ngramlist = []
def ngram(str,n):
    str = str.replace('.', '')
    tokens = nltk.word_tokenize(str)
    str = str.replace(' ', '')
    for i in range(len(str)):
        if i + n <= len(str):
            ngramlist.append(str[i:i + n])

ngram(strings,7)

print(ngramlist)