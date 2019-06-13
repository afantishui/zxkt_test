# coding: utf-8
import os
from operation import*
from config import *

# 读取配置 p下载路径 u下载链接 c 窗口类名 pos坐标
path, path1 = get_path_conf()
url, url1 = get_url_conf()
c1, c2, c3 = get_classname_conf()
t1, t2, t3, t4 = get_title_conf()
pos = get_position_conf()
filename = app.get_name(url)
print(path1+filename)
# # 1.下载文件
# download_client(url1, path1,filename)
# 2.安装文件
install_teacher(path1,filename,c1, path)
# 3.登录
# login(c2,pos)
# 设备检测
s_device(c2, t4)

