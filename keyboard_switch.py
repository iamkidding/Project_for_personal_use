# -*- coding: utf-8 -*-
import os, time


def switch():
	command = input('请选择关闭or开启笔记本键盘：')
	if command == '关闭' or command == 'disable':
		# 关闭笔记本键盘  sc config i8042prt start= disabled
		os.system('sc config i8042prt start= disabled')
	elif command == '开启' or command == 'open':
		# 打开笔记本键盘  sc config i8042prt start= auto
		os.system('sc config i8042prt start= auto')
	else:
		print('请输入正确命令')
		switch()

def reboot():
	reb = input('该操作重启电脑后完成，是否现在重启：')
	if reb == "是":
		print('将在10秒后重启')
		time.sleep(10)
		os.system('shutdown -r')
	elif reb == '否':
		print('请稍后自行重启电脑')
	else:
		print('请输入正确命令')
		reboot()

if __name__ == '__main__':
	switch()
	reboot()
	input('按回车退出程序')
