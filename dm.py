import win32com.client
print('12')
#调用大漠插件前需要把插件注册到系统
dm = win32com.client.Dispatch('dm.dmsoft') # 调用大漠插件
print(dm.ver()) # 输出版本号
# 鼠键方法正常
# dm.MoveTo(10,20)
# print(dm.GetCursorPos())
# 文字识别
base_path = dm.GetBasePath()
dm_ret = dm.SetPath(base_path)
dm_ret = dm.SetDict(0,"ys.txt")
s = dm.Ocr(835,529,925,553,"903a00-3a003a|003a90-b6ffff|000000-000000",0.8)

if s is None:
 	print('没有识别到内容')
else:
 	print('识别到:'+s)
# 启动应用方法调试不成功
# dm.RunApp('notepad',1)