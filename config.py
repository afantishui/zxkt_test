# -*- coding:utf-8 -*-  
import configparser

def getpath():
	cf = configparser.ConfigParser()
	cf.read("config.ini")
	path = cf.get("path", "dl_path")
	path1 = cf.get("path", "d2_path")
	url = cf.get("url", "url1")
	url1 = cf.get("url", "url2")
	return path, path1, url, url1
