# -*- coding:utf-8 -*- 
import urllib.request
from selen import *
import subprocess
import time
import os
import win32api, win32gui,win32con

# 下载进度初始值
downloaded = '0'
class Base():
	"""docstring for Base"""
	

	# 截取软件名
	def get_name(self,url):
		# http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe
		# 以/进行分割 取最后一个
		fn = url.split('/')
		# print(fn)
		fn1 = fn[-1]
		filename = fn1[:-1]
		print(filename)
		return filename

	# 下载文件到指定目录
	def download(self,url,path,filename):
		stime = time.time() # 记录开始时间
		response = urllib.request.urlretrieve(url, path + filename, self.download_listener)
		etime = time.time()-stime # 记录结束时间
		print('用时:%s'%etime)

	# 下载监听进度
	def download_listener(self,a, b, c):
		per = 100.0 * a * b / c
		if per > 100:
			per = 100
		new_downloaded = '%.1f' % per
		global downloaded

		if new_downloaded != downloaded:
			downloaded = new_downloaded
			print ('download %s%%  %s/%s' % (downloaded, a * b, c))


	# 查找指定文件 filename文件名 path查找路径,找到返回True否则返回False
	def search_file(self,filename):
		flag = False
		for filenames in os.walk('E:\\zxktsoft\\',  followlinks=True):
			for i in filenames:
				if filename in i:
					# print('文件名：%s 已存在' % filename)
					flag = True
					break
		return flag


	# 安装指定目录的软件
	def install(self,path,softname):
		# 打开安装文件
		win32api.ShellExecute(0, 'open', path+softname, '','',1)
		self.wait(2)
		self.send_key('enter')
		self.wait(2)
		self.send_key('enter')
		self.wait(20)
		self.send_key('enter')


	# 卸载指定目录的软件
	def uninstall(self,path,softname):
		pass

	def findwindow(self,classname,titlename):
		#获取句柄
		hwnd = win32gui.FindWindow(classname, titlename)
		#获取窗口左上角和右下角坐标
		left, top, right, bottom = win32gui.GetWindowRect(hwnd)
		print(hwnd, left, top, right, bottom)
		return hwnd, left, top, right, bottom
	# 删除指定目录的软件
	def delete(self,path):
		pass

	# 启动软件
	def open(self,path,softname):
		pass

	# 关闭软件
	def close(self,path,softname):
		pass

	# 点击
	def click(self,x,y,lr):
		#鼠标定位到(x,y)
		win32api.SetCursorPos([x,y])
		# l 左击 r 右击
		if lr == 'l':	
			#执行左单键击，若需要双击则延时几毫秒再点击一次即可
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		elif lr == 'r':
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


	# 输入文本
	def text(self,msg):
		
		
	# 等待
	def wait(self,s):
		time.sleep(s)

	# 按键
	def send_key(self,key):
		# 回车键
		if key == 'enter':
			win32api.keybd_event(13,0,0,0)
			win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

	def get_mouse_pos():
		win32api.GetCursorPos()



if __name__ == '__main__':

	a = Base()
	path = "E:\\zxktsoft\\"
	softname = 'nsb-teacher-1.0.3.0-dev.exe'
	classname = 'Qt5QWindowIcon'
	title = '牛师帮教师'
	# a.install(path,softname)
	a.findwindow(classname,title)
	# a.download('http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe','E:\\zxkt\\')
# $client.DownloadFile('http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe','E:\\zxkt\\nsb-teacher-1.0.3.0-dev.exe')
# 'powershell "($client = new-object System.Net.WebClient) -and 
# ($client.DownloadFile("http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe", "E:\\zxkt\\nsb-teacher-1.0.3.0-dev.exe"))"'