# coding:utf-8

"""
chr(i)¶(原文)
Unicode コードポイントが整数 i である文字を表す文字列を返します。例えば chr(97)
は文字列 'a' を、 chr(8364) は文字列 '€' を返します。 ord() の逆です。

引数の有効な範囲は 0 から 1,114,111 (16 進数で 0x10FFFF) です。 i が範囲外の場合 ValueError が送出されます。
"""

"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．

"""

def cipher(strings):
    new_strings = ""
    for unit in strings:
        if unit.islower() == True:
            new_strings = new_strings + chr(219 - ord(unit))
        else:
            new_strings = new_strings + unit
    print(new_strings)

cipher("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
)