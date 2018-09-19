#!-*-coding:utf-8-*-
# !@Date: 2018/9/19 9:09
# !@Author: Liu Rui
# !@github: bigfoolliu


from app import db


class User(db.Model):
	"""用户模型,继承于db的Model"""
	id = db.Column(db.Integer, primary_key=True)  # 创建id字段,且作为主键
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.RelationshipProperty('Post', backref='author', lazy='dynamic')

	@property
	def is_authenticated(self):
		"""用户被认证"""
		return True

	@property
	def is_active(self):
		"""用户是活动的"""
		return True

	@property
	def is_anonymous(self):
		"""用户是匿名的"""
		return False

	def get_id(self):
		"""获取用户id"""
		return str(self.id)

	def __repr__(self):
		"""在命令行输入User的实例时可以直接输出return的信息"""
		return '<User %r>' % self.nickname


class Post(db.Model):
	"""用户写的博客模型"""
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % self.body


