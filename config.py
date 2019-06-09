# -*- coding:utf-8 -*-  
import configparser
cf = configparser.ConfigParser()
cf.read("config.ini",encoding='UTF-8')

def get_path_conf():
	path = cf.get("path", "dl_path")
	path1 = cf.get("path", "d2_path")
	return path, path1

def get_url_conf():
	url = cf.get("url", "url1")
	url1 = cf.get("url", "url2")
	return url, url1

def get_classname_conf():
	c1 = cf.get("classname","c1")
	c2 = cf.get("classname","c2")
	c3 = cf.get("classname","c3")
	return c1, c2, c3

def get_position_conf():
	x1 = cf.get("position","x1")
	x2 = cf.get("position","x2")
	x3 = cf.get("position","x3")
	x4 = cf.get("position","x4")
	pos = [x1, x2, x3, x4]
	return pos

