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
	app.wait(3)


# 安装客户端
def install_teacher(path,softname,classname,path1):
		# 启动安装文件
		app.launch(path,softname)
		app.wait(3)
		# 获取安装窗口句柄
		hwnd = app.findwindow(classname)

		if hwnd > 0 :
			app.wait(0.5)
			app.send_key('BackSpace')
			app.wait(1)
			app.text_en(b'D:\\Program Files (x86)\\NiushibangPCT',hwnd)
			app.wait(1)
			app.send_key('Enter')
			# app.wait(2)
			# app.send_key('Enter')
			# app.wait(10)
			# app.send_key('Enter')
			# app.wait(2)
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

# 登录教师,账号密码续作参数化
def login(classname,pos):
	a = True
	while a:
	
		a = False
		hwnd = app.findwindow(classname)
		# 输入账号
		app.click(pos[1],'l')
		app.wait(0.5)
		app.text_en(b'13432688452',hwnd)
		app.wait(0.5)
		# 输入密码
		app.send_key('Enter')
		app.wait(0.5)
		app.text_en(b'13432688452',hwnd)
		app.wait(0.5)
		# 点确定
		app.send_key('Enter')
		print('ok')

# 设备检测
def s_device(classname,title):
	hwnd_d = app.findwindow1(classname,title)
	if hwnd_d > 0:
		print('设备检测窗口正常打开')
		# 设备检测窗口关闭按钮坐标
		app.click(1340,290)
	else:
		print('没有检测到设备检测窗口')

# 课表
def s_course():
	pass
# 我的
def s_myself():
	pass

# 调试
def test():
	app.send_key('Enter')