# coding:utf-8

str1 = "パトカー"
str2 = "タクシー"
newstr = ""
for i in range(4):
    str = str1[i] + str2[i]
    newstr = newstr + str

print(newstr)