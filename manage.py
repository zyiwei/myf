#!usr/bin/env python
#coding=utf-8 
import os

COV=None
if os.environ.get('FLASK_COVERAGE'):
	import coverage
	COV=coverage.coverage(branch=True,include='app/*')
	COV.start()

if os.path.exists('.env'):
	print('Importing environment from .env')
	for line in open('.env'):
		var=line.strip().split('=')
		if len(var)==2:
			os.environ[var[0]]=var[1]

from app import create_app,db
from app.models import User,Role,Post,Permission,Comment,Follow,FollowComments
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
	return dict(app=app,db=db,User=User,Role=Role,Post=Post,Permission=Permission,Comment=Comment,Follow=Follow,FollowComments=FollowComments)
	
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)


@manager.command
def test(coverage=False):      
	"""Run the unit tests./运行单元测试"""
	if coverage and not os.environ.get('FLASK_COVERAGE'):
		import sys
		os.environ['FLASK_COVERAGE']='1'
		os.execvp(sys.executable,[sys.executable]+sys.argv)

	import unittest
	tests=unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)
	if COV:
		COV.stop()
		COV.save()
		print('Coverage Summary:')
		COV.report()
		basedir=os.path.abspath(os.path.dirname(__file__))
		covdir=os.path.join(basedir,'tmp/coverage')
		COV.html_report(directory=covdir)
		print('HTML version: file://%s/index.html'%covdir)
		COV.erase()

@manager.command
def profile(length=25,profile_dir=None):
	"""Start the application under the code profiler./开启源码分析器"""
	from werkzeug.contrib.profiler import ProfilerMiddleware
	app.wsgi_app=ProfilerMiddleware(app.wsgi_app,restrictions=[length],profile_dir=profile_dir)
	app.run()


if __name__=='__main__':
	app.run(debug=True)

'''
if __name__=='__main__':
	manager.run()
'''