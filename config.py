# -*- coding:utf-8 -*-  
import configparser

def get_path_conf():
	cf = configparser.ConfigParser()
	cf.read("config.ini",encoding='UTF-8')
	path = cf.get("path", "dl_path")
	path1 = cf.get("path", "d2_path")
	
	c1 = cf.get("classname","c1")
	c2 = cf.get("classname","c2")
	c3 = cf.get("classname","c3")
	return path, path1, url, url1,c1, c2, c3

def get_url_conf():
	url = cf.get("url", "url1")
	url1 = cf.get("url", "url2")
	return url, url1

def get_classname_conf():
c1 = cf.get("classname","c1")
	c2 = cf.get("classname","c2")
	c3 = cf.get("classname","c3")