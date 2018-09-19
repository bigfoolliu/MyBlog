#!-*-coding:utf-8-*-
# !@Date: 2018/9/18 21:14
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
表单文件
"""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	"""继承Form的登录表单"""
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)
