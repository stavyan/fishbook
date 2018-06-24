# coding: utf-8
from flask import jsonify, request, render_template, flash
import json
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from . import web

from app.forms.book import SearchForm


# 蓝图 blueprint 蓝本


@web.route('/book/search')
def search():
    """
       q: 普通关键字 isbn
       page
       ?q=金庸&page=1
    """
    # Request Response
    # HTTP 的请求信息 查询参数 POST参数 remote ip

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)

        else:
            yushu_book.search_by_keyword(q, page)
            # result = YuShuBook.search_by_keyword(q, page)
            # result = BookViewModel.package_collection(result, q)

        # return jsonify(result)  # return json.dumps(result), 200, {'content-type': 'application/json'}
        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字！')

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.books[0])
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {
        'name': 'stav',
        'age': 18
    }
    r1 = {

    }
    flash('hello, qiyue!', category='error')
    flash('hello, stav!', category='warning')
    # 模版 html
    return render_template('test.html', data=r, data1=r1)


def __validate():
    pass
