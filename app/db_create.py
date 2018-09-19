#!-*-coding:utf-8-*-
# !@Date: 2018/9/19 9:24
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
创建数据库的脚本
通过运行该脚本,在MyBlog的目录下,创建了一个新的目录db_repository和一个文件app.db
"""
from migrate.versioning import api
# 导入数据库配置的两个常数
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path


db.create_all()
# 如果该数据仓库不存在
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
	api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
