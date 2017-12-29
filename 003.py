import nltk

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

tokens = nltk.word_tokenize(str)
list = []

for word in tokens:
    list.append(word[0])

print(list)