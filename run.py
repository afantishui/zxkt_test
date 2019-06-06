# coding: utf-8
import os
from operation import*
from config import *

# 读取配置 p下载路径 u下载链接 c 窗口类名
path, path1, url, url1,c1, c2, c3= getpath()

# 获取文件名
filename = app.get_name(url)
print(path1+filename)
# # 1.下载文件
# download_client(url1, path1,filename)
# 2.安装文件
# install_teacher(path1,filename,c1)
# 3.登录


