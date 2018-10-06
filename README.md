# Python+Flask+Mysql 开发赠送书籍平台

## 预览

[预览地址](http://132.232.19.246:5000)

## 实现的功能

- 蓝图注册视图函数

- WTForms参数验证

- 编写viewModel处理原始数据

- Jinja2模板引擎

- 基于SQLAlchemy的CRUD

- 使用with的上下文特性自动开启事务

- flask-login处理登陆逻辑

- 使用多线程异步发送邮件

- 简单，开箱即用


> Python的运行环境要求3.6以上。


## 安装所需依赖

| 依赖 | 说明 |
| -------- | -------- |
| Python| `>= 3.6` |
| Flask| `>= 1.0.2` |
| cymysql| `>= 0.9.10` |
| Flask-Login |`>= 0.4.1`|
| Flask-Mail |`>= 0.9.1`|
| Flask-SQLAlchemy  |`>= 2.3.2`|
| itsdangerous |`>= 0.24`|
| Jinja2 |`>= 2.10`|
| requests |`>= 2.18.4`|
| SQLAlchemy  |`>= 1.2.8`|
| urllib3 |`>= 1.22`|
| Werkzeug |`>= 0.14.1`|
| WTForms |`>= 2.2`|


## 注意

> 数据库在运行fisher.py自动生成。

## 安装运行

- 点击下载安装或者复制地址使用git clone命令下载

```
git clone git@github.com:<你的用户名>/flask-yushu.git
```

- 在app目录下创建secure.py文件（用来管理私密设置信息）
```
DEBUG=True  #是否开启Dubug
HOST='0.0.0.0' #0.0.0.0表示访问权限为全网
PORT=80 #访问端口号

# mysql连接，比如 SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:root@localhost:3306/fisher'
SQLALCHEMY_DATABASE_URI='mysql+cymysql://用户名:用户名@ip地址:mysql端口号/数据库名'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# 设置key，比如 SECRET_KEY='guaosi'
SECRET_KEY=''
# Email 配置
MAIL_SERVER = ''
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'admin@guaosi.com'
MAIL_PASSWORD = '' #密码
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <admin@guaosi.com>'
```

- 相关依赖

最好在venv的虚拟环境中安装，避免全局污染

- 运行

```Python
python fisher.py
```

## 在项目中使用事务

已经使用with和yield对事务做了上下文处理，当进行数据库处理时，请在with下操作，发生错误时自动回滚
```
with db.auto_commit():
    # orm逻辑
    db.session.add(模型实例)
```

## 在项目中使用filter_by
已经重写filter_by方法，默认加入条件 status=1.
```
Gift.query.filter_by(id=gid).first_or_404()
#相当于
Gift.query.filter_by(id=gid,status=1).first_or_404()
```

## 在项目中构建ViewModel
推荐在渲染模板之前，创建ViewModel文件,将原始数据进行处理,具体参考 app/view_models/book.py 文件

## 在项目中发送邮件
直接调用发送邮件方法，已经默认多线程异步发送邮件
```
send_mail() #直接调用即可多线程异步发送邮件
```

### 交流

笔者热爱新技术学习、热衷分享。

- QQ：617946852
- Email：stavyan@qq.com
- WeChat stav_yan


### 最后
> 欢迎进入笔者的私人空间---[斯塔夫部落格](https://stavtop.club)