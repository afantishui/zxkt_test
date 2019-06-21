import win32com.client
print('12')
#调用大漠插件前需要把插件注册到系统
dm = win32com.client.Dispatch('dm.dmsoft') # 调用大漠插件
print(dm.ver()) # 输出版本号
# 鼠键方法正常
dm.MoveTo(10,20)
print(dm.GetCursorPos())
# 启动应用方法调试不成功
dm.RunApp('notepad',1)