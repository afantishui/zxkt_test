# coding: utf-8
import os
from base import Base
from config import *
# 实例化Base
app = Base()
# 读取配置 p下载路径 u下载链接 c 窗口类名
path,path1, url, url1, c1, c2= getpath()

# 获取文件名
filename = app.get_name(url)
print(path1+filename)
# # 1.下载文件
# if app.search_file(filename):
# 	print('文件名：%s 已存在' % filename)
	
# else:
# 	print('找不到文件,开始下载%s'%filename)
# 	app.download(url1, path1,filename)
# 2.安装文件
app.install(path1,filename,c1)
# 3.登录
