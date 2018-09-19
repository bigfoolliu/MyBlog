#!-*-coding:utf-8-*-
# !@Date: 2018/9/18 20:53
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
配置
"""
# 激活跨站点请求伪造保护
CSRF_ENABLED = True
# SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。
# 当你编写自己的应用程序的时候，请务必设置很难被猜测到密钥。
SECRET_KEY = 'you_can_not_guess_the_key'

# 定义一个OpenID提供者的列表
OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


# 用于数据库(sqlite数据库)的相关配置
import os
basedir = os.path.abspath(os.path.dirname(__file__))  # __file__是获得模块所在的路径的,可能得到的是一个相对路径

# 数据库的地址
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# 数据库的迁移地址
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

