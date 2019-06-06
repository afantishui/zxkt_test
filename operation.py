# -*- coding:utf-8 -*- 
from base import Base

app = Base()


# 下载客户端
def download_client(url,path,filename):
	if app.search_file(filename):
		print('文件名：%s 已存在' % filename)
	
	else:
		print('找不到文件,开始下载%s'%filename)
	app.download(url, path,filename)


# 安装客户端
def install_teacher(path,softname,classname):
		# 启动安装文件
		app.launch(path,softname)
		app.wait(3)
		# 获取安装窗口句柄
		hwnd = app.findwindow(classname)

		if hwnd > 0 :
			app.wait(2)
			app.send_key('Enter')
			app.wait(2)
			app.send_key('Enter')
			app.wait(10)
			app.send_key('Enter')
			app.wait(2)
			try:
				hwnd = app.findwindow(classname)
				print("关闭安装窗口后句柄")
			except:
				print('安装完成')
		else:
			print('没有启动安装程序')

# 卸载客户端
def uninstall(path,softname):
		# softname = 'unins000.exe'
		app.launch(path,softname)
		# 获取安装窗口句柄
		hwnd = app.findwindow(classname)
		if hwnd > 0 :
			app.wait(1)
			app.send_key('Enter')
			app.wait(2)
			app.send_key('Enter')
			app.wait(10)
			app.send_key('Enter')
			app.wait(2)
			try:
				hwnd = app.findwindow(classname)
				print("关闭安装窗口后句柄")
			except:
				print('安装完成')
		else:
			print('没有启动安装程序')


def login(classname):
	hwnd = app.findwindow(classname)
	# 输入账号
	app.click(x,y,l)
	app.wait(0.5)
	app.text_en()
	app.wait(0.5)
	# 输入密码
	app.click(x,y,l)
	app.wait(0.5)
	app.text_en()
	app.wait(0.5)
	# 点确定
	app.click(x,y,l)
# 调试
def test():
	app.send_key('Enter')