#!-*-coding:utf-8-*-
# !@Date: 2018/9/19 9:39
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
用于数据迁移的脚本

SQLAlchemy-migrate 迁移的方式就是比较数据库(在本例中从 app.db 中获取)与我们模型的结构(从文件 app/models.py 获取)。
两者间的不同将会被记录成一个迁移脚本(001_migration.py)存放在迁移仓库中。
迁移脚本知道如何去迁移或撤销它，所以它始终是可能用于升级或降级一个数据库。


为了让 SQLAlchemy-migrate 容易地识别出变化，不要重命名存在的字段，仅限于增加或者删除模型或者字段，或者改变已存在字段的类型。

不应该在没有备份下去尝试迁移数据库。当然也不能在生产环境下直接运行迁移脚本，必须在开发环境下确保迁移运转正常。
"""


import imp
# import importlib
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO


v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v + 1))

tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)

script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)

open(migration, 'wt').write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('New migration saved as ' + migration)
print('Current database version: ' + str(v))
