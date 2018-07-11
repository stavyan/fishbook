from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.helper import is_isbn_or_key
from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

from flask_login import UserMixin
from app import login_manager
from app.models.gift import Gift
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    # __tablename = 'user1'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Integer, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不予许一个用户同时赠送多本相同的图书
        # 一个用户不可能同时成为赠送者和索要者

        # 既不在赠送清单也不在心愿清单才能添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        wishing = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        if not gifting and not wishing:
            return True
        else:
            return False

    # def get_id(self):
    #     return self.id


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
