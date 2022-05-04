#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: Isaac Privett
#Date: 05-01-2022
#Description: Script to try anonymous ftp login on a host

import ftplib

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous','anonymous')
		print("[*] " + hostname + " Anonymous FTP login successful.")
		ftp.quit()
		return True
	except:
		print("[-] " + hostname + " Anonymous FTP login failed.")

host = input("Enter IP of target: ")
anonLogin(host)
