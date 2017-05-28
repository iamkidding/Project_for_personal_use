# -*- coding: utf-8 -*-

import pip

def install():
	package_need_to_be_installed = input("请输入需要安装的包：")
	# 后续可加入对包的判断
	pip.main(['install', package_need_to_be_installed])
	# 判断是否要继续安装包
	conti = input("是否继续要安装包（请输入是或者否，并无其他判断条件）：")
	while True:
		if conti == "是"  or conti == '否':
			if conti == '是':
				install()
			else:
				break
		else:
			print("请输入合法字符")
			conti = input("是否继续要安装包（请输入是或者否，并无其他判断条件）：")

if __name__ == '__main__':
	install()
	input("按回车退出程序")