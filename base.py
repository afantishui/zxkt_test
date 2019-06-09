# -*- coding:utf-8 -*- 
import urllib.request
import subprocess
import time
import os
import win32api, win32gui,win32con,win32com.client
# 键码
keycode = { 
		'BackSpace':"8", "Tab":"9", "Clear":"12", "Enter":"13", "Shift_L" : "16",
		"Ctrl":"17", "Alt_L":"18", "Pause":"19", "Caps_Lock":"20", "Esc":"27",
		"space":"32", "Prior":"33", "Next":"34", "End":"35", "Home":"36",
		"Left":"37", "Up":"38", "Right":"39", "Down":"40",
		"Select":"41", "Print":"42", "Execute":"43", "Insert":"45", "Delete":"46", "Help":"47",
		"a":"65", "b":"66", "c":"67", "d":"68", "e":"69", "f":"70", "g":"71", "h":"72", "i":"73",
		"j":"74", "k":"75", "l":"76", "m":"77", "n":"78", "o":"79", "p":"80", "q":"81", "r":"82",
		"s":"83", "t":"84", "u":"85", "v":"86", "w":"87", "x":"88", "y":"89", "z":"90",
		"0":"96", "1":"97", "2":"98", "3":"99", "4":"100", "5":"101", "6":"102", "7":"103", "8":"104", "9":"105",
		"*":"106", "+":"107", "-":"109", ".":"110", "/":"111",
		"F1":"112", "F2":"113", "F3":"114", "F4":"115", "F5":"116", "F6":"117",
		"F7":"118", "F8":"119", "F9":"120", "F10":"121", "F11":"122", "F12":"123",
}

# 下载进度初始值
downloaded = '0'
class Base():
	"""docstring for Base"""
	def __init__(self):
		self.shell = win32com.client.Dispatch("WScript.Shell")

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
		print('下载完成,用时:%s'%etime)

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


	# 启动指定目录的软件
	def launch(self,path,softname):
		# 打开安装文件
		print("打开目录:%s"%(path+softname))
		win32api.ShellExecute(0, 'open', path+softname, '','',1)
		self.wait(1)
		


	# 卸载指定目录的软件
	# def uninstall(self,path,softname):
	# 	softname = 'unins000.exe'
	# 	win32api.ShellExecute(0, 'open', path+softname, '','',1)
	# 	self.wait(0.5)


	def findwindow(self,classname):
		#获取句柄,类名与标题名,不填则用None
		hwnd = win32gui.FindWindow(classname,None)
		#获取窗口左上角和右下角坐标
		left, top, right, bottom = win32gui.GetWindowRect(hwnd)
		print(hwnd, left, top, right, bottom)
		return hwnd
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
	def click(self,p,lr):
		p = p.split(',')
		#鼠标定位到(x,y)
		win32api.SetCursorPos((int(p[0]),int(p[1])))
		# l 左击 r 右击
		if lr == 'l':	
			#执行左单键击，若需要双击则延时几毫秒再点击一次即可
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		elif lr == 'r':
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


	# 输入文本,采用字节符
	def text_en(self,msg,hwnd):
		 for x in msg:
		 	win32gui.SendMessage(hwnd,win32con.WM_CHAR,x,0)
		
	# 等待
	def wait(self,s):
		time.sleep(s)

	# 按键
	def send_key(self,key):

		if keycode[key]:
			win32api.keybd_event(int(keycode[key]),0,0,0)
			win32api.keybd_event(int(keycode[key]),0,win32con.KEYEVENTF_KEYUP,0)
		else :
			print("没有对应的键码")

	# 组合键  **kwargs 打包关键字参数成dict给函数体调用
	def com_key(*args):
		if len(args) <= 3:
			win32api.keybd_event(int(keycode[args[1]]),0,0,0)
			win32api.keybd_event(int(keycode[args[2]]),0,0,0)
			win32api.keybd_event(int(keycode[args[1]]),0,win32con.KEYEVENTF_KEYUP,0)
			win32api.keybd_event(int(keycode[args[2]]),0,win32con.KEYEVENTF_KEYUP,0)
			print('按下了%s+%s'%(args[1],args[2]))	
		# if keycode[key]:

		# else :
		# 	print("没有对应的键码")


	def get_mouse_pos():
		win32api.GetCursorPos()



if __name__ == '__main__':
	
	a = Base()
	# a.com_key('CtrlCtrl','v')
	hwnd = a.findwindow('TWizardForm')

	a.click('980,510','l')
	a.wait(2)
	a.text_en(b'123',hwnd)

	# path = "E:\\zxktsoft\\"
	# softname = 'nsb-teacher-1.0.3.0-dev.exe'
	# classname = 'TWizardForm'
	
	# a.install(path,softname,classname)
	# a.findwindow(classname,None)
	# a.download('http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe','E:\\zxkt\\')
# $client.DownloadFile('http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe','E:\\zxkt\\nsb-teacher-1.0.3.0-dev.exe')
# 'powershell "($client = new-object System.Net.WebClient) -and 
# ($client.DownloadFile("http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe", "E:\\zxkt\\nsb-teacher-1.0.3.0-dev.exe"))"'