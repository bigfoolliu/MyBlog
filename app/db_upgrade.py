#!-*-coding:utf-8-*-
# !@Date: 2018/9/19 10:18
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
用于将数据库升级到最新的版本
"""


from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_DATABASE_URI


api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('Current database version: ' + str(v))
