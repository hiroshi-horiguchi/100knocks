import nltk

strings = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
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



ngram(strings,7,True)
ngram(strings,3,False)

print(ngramlist)
print(ngram_wordlist)