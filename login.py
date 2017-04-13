#Brian Nuckles
#CPSC 223P
#Login Module

import sys
import string



def userLogin():
	counter = 0

	while 1:
		name = str(input("Please enter your username:"))		#asks user for their login info
		passwd = str(input("Please enter your password:"))

		in_file = open('user_login_info.txt','r')
		while 1:												#loops until EOF conditions are met
			readname = in_file.readline()						#reads name
			readname = readname.rstrip()						#strips extra blank space and \n character from line
			if not readname:	
				break
				
			readpasswd =in_file.readline()						#reads password
			readpasswd = readpasswd.rstrip()					#strips etra bank space and \n character from line
			if not readpasswd:
				break
				
			in_file.readline()									#reads blank line between sets of user information
			
			if name == readname and passwd == readpasswd: 		#checks to see if name and password match
				print("Login succesfull.")
				return
				
		in_file.close()
		print("Login failed. Please try again.")
		counter = counter+1										#increment retry counter then loop back to user input
		if counter == 5:
			print("Too many attempts.")
			sys.exit()											#too many retries, close program
		
		
