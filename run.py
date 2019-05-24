# coding: utf-8
import os
from base import Base
from config import *
# 实例化Base
app = Base()
# 读取配置 下载路径 下载链接
path,path1, url, url1 = getpath()
url2 ='http://niubo.oss-cn-shenzhen.aliyuncs.com/live/client/nsb-teacher-1.0.3.0-dev.exe'
# 获取文件名
filename = app.get_name(url)
print(filename)
# 1.下载文件
if app.search_file(filename):
	print('文件名：%s 已存在' % filename)
	
else:
	print('找不到文件,开始下载%s'%filename)
	app.download(url1, path1,filename)
# 2.安装文件

