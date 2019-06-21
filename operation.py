# -*- coding:utf-8 -*- 
from base import Base
import win32com.client
#调用大漠插件前需要把插件注册到系统
dm = win32com.client.Dispatch('dm.dmsoft') # 调用大漠插件
base_path = dm.GetBasePath()
dm_ret = dm.SetPath(base_path)
dm_ret = dm.SetDict(0,"ys.txt")
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

# 启动应用
def start_app():
	softname = 'nsb-teacher.exe'
	print('启动应用路径:'+"D:\\Program Files (x86)\\NiushibangPCT\\"+softname)
	app.launch("D:\\Program Files (x86)\\NiushibangPCT\\", softname)
	app.wait(3)



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
def login(classname,pos,name,psd):
	a = True

	while a:
		a = False
		hwnd = app.findwindow(classname)
		s = dm.Ocr(827,527,955,556,"903a00-3a003a|003a90-b6ffff|000000-000000",0.9)
		if s is None:
			print('没有识别到账号,输入账号密码')
			# 输入账号
			app.click(pos[1],'l')
			app.wait(0.5)
			app.text_en(name,hwnd)
			app.wait(0.5)
			# 输入密码
			app.send_key('Enter')
			app.wait(0.5)
			app.text_en(psd,hwnd)
			app.wait(0.5)
			# 点确定
			app.send_key('Enter')
		else:
			print('识别到:'+s,'直接登录')
			app.wait(0.5)
			app.click(pos[0],'l')
			
		
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