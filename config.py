# -*- coding:utf-8 -*-  
import configparser

def getpath():
	cf = configparser.ConfigParser()
	cf.read("config.ini",encoding='UTF-8')
	path = cf.get("path", "dl_path")
	path1 = cf.get("path", "d2_path")
	url = cf.get("url", "url1")
	url1 = cf.get("url", "url2")
	c1 = cf.get("classname","c1")
	c2 = cf.get("classname","c2")
	return path, path1, url, url1,c1, c2
