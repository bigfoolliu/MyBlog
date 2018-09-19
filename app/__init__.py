#!-*-coding:utf-8-*-
# !@Date: 2018/9/18 20:07
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
app的初始化
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# 使用配置文件,注意此处是使用导入对象
app.config.from_object('config')
# 初始化数据库
db = SQLAlchemy(app)

from app import views  # 导入视图
from app import models  # 导入模型


# 用于与数据库相连接的相关库
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir


lm = LoginManager()
lm.init_app(app)

# Flask-OpenID 扩展需要一个存储文件的临时文件夹的路径。对此，我们提供了一个 tmp 文件夹的路径。
oid = OpenID(app, os.path.join(basedir, 'tmp'))
