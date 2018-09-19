#!-*-coding:utf-8-*-
# !@Date: 2018/9/19 10:25
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
用于数据库的降低至旧的版本(很少这么干)的脚本
"""


from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_DATABASE_URI


v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('Current database version: ', str(v))

