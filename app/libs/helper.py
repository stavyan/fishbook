# coding:utf-8

def is_isbn_or_key(word):
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9的数字组成 含 ' - '

    # 以下代码是用来判断q是isbn还是关键字
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
