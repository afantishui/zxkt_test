import win32com.client

dm = win32com.client.Dispatch('dm.ll') # 调用大漠插件
print(dm.ver()) # 输出版本号