#!-*-coding:utf-8-*-
# !@Date: 2018/9/18 20:07
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
视图模块
"""
from flask import render_template, flash, redirect, session, url_for, g, request
from app import app, db, lm, oid  # 导入Flask实例等
from .forms import LoginForm  # 导入表单类
from .models import User


@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Tommy'}
	posts = [
		{
			'author': {'nickname': 'John'},
			'body': 'Look nice.'
		},
		{
			'author': {'nickname': 'Tom'},
			'body': 'I like it.'
		}
	]

	return render_template(
		'index.html',
		title='Home',
		user=user,
		posts=posts
	)


# @app.route('/login', methods=['post', 'get'])
# def login():
# 	form = LoginForm()  # 表单实例
# 	"""
# 	如果 validate_on_submit 在表单提交请求中被调用，它将会收集所有的数据，对字段进行验证，
# 	如果所有的事情都通过的话，它将会返回 True，表示数据都是合法的。说明数据是安全的，并且被应用程序给接受了
# 	"""
# 	if form.validate_on_submit():
# 		"""
# 		flash 函数是一种快速的方式下呈现给用户的页面上显示一个消息,可以用来调试.需要添加到模板文件中.
# 		"""
# 		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
# 		return redirect('/index')
# 	return render_template(
# 		'login.html',
# 		title='Sign In',
# 		form=form,
# 		providers=app.config['OPENID_PROVIDERS'])


# 添加数据库之后的login函数更新
@app.route('/login', methods=['post', 'get'])
@oid.loginhandler  # 该装饰器告诉Flask-OpenID这是登录视图函数
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
	return render_template(
		'login.html',
		title='Sign In',
		form=form,
		providers=app.config['OPENID_PROVIDERS']
	)


# user_loader回调,用于从数据库加载用户,该函数会被Flask-Login使用
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
