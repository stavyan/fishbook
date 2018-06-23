# coding: utf-8
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 导入私密配置文件
    app.config.from_object('app.setting')  # 导入私密配置文件
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


# 注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
