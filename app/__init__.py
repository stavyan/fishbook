# coding: utf-8
from flask import Flask
from flask_login import LoginManager
from app.models.book import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 导入私密配置文件
    app.config.from_object('app.setting')  # 导入私密配置文件
    register_blueprint(app)

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册！'

    with app.app_context():
        db.create_all()
    return app


# 注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
