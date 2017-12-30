# coding:utf-8
#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def sentencemake(x,y,z):
    strings = ""
    strings = str(x) + "時の" + y + "は" + str(z)
    print(strings)

sentencemake(12,"気温",22.4)