
import nltk
import random
"""
def angouka(sentence):
    tokens = nltk.word_tokenize(sentence)
    newtokens = ""
    newword = ""
    for word in tokens:

        print(newword)
        for i in range(len(word)):
            if i == 0 or len(word):
                first_character = word[0]
                last_character = word[len(word) -1]
                newword = newword + first_character
                newword = newword + last_character
            else:
                slicedword = word[1:len(word)-1]
                slicedwordlist = []
                for i in range(len(slicedword)):
                    slicedwordlist.append(slicedword[i])
                    random.shuffle(slicedwordlist)
                    return slicedwordlist
                for character in slicedwordlist:
                    newword2 = newword2 + character
                    return newword2
                newword = newword + neword2
        return newword
    newtokens = newtokens + newword
    print(newtokens)

angouka("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
)
"""
