#application.py


#THIS IS OUR TOP LEVEL MODULE (aka the main)

#modules here are to be renamed into something more relevant to what they do

#RENAME THE MODULES 
from menu import *							#menu
from writeFile import *					#write file
from delete import *						#delete patient
from login import userLogin					#log in
from edit import *							#edit patient
from create import *						#create patient
from search import *						#search
from readFile import *						#read file



#call the login from module: brian_nuckles
userLogin()


#upon successful login, call Read File module: mihn_nguyen to get patient List
patientList = readText()


command = 100

#loop until EXIT has been selected
while command != 0:

	#call Menu Module for menu display
	command = Menu()	#menu will return a value back module:adam_rounds
	
	#call corresponding function
	if command == 1:
	#call search to see if the patient already exists in the list or not. If exists then don't add #NOTE: this SEARCH function is to only return a BOOLEAN, different from the command search option
		if find(patientList) is True:
			print("CAN NOT ADD! RECORD ALREADY EXISTS IN THE LIST!\n")

		else:
			#add new patient (create )
			patientList = newPatient(patientList)  #pass in the list from main, return the list back with new patient added in
			print("NEW RECORD HAS BEEN ADDED\n")
    
		
	elif command == 2:
		#call search to see if the patient already exists in the list or not. If it does not exist, you can not edit
		if find(patientList) is False:  #NOTE: this SEARCH function is to only return a BOOLEAN, different from the command search option
			print("RECORD NOT FOUND IN LIST! CAN NOT EDIT!\n")
		else:
			#edit patient (edit)
			patientList = EditRecord.implementEdit(patientList) #pass in the list from main, return the list back after it has been editted
		
	elif command == 3:
		#call search to see if the patient exists in the list or not. If it does not exist, you can not delete
		if find(patientList) is True:  #NOTE: this SEARCH function is to only return a BOOLEAN, different from the command search option
			patientList = remove(patientList) #pass in the list from main, return the list back after you delete the record
		else:
			print("RECORD NOT FOUND!\n")
	elif command == 4:
		#search for a record
		search(patientList)     #this search function will print out record information if found, or say not found. DIFFERENT FROM THE ABOVE SEARCH FUNCTIONS

	elif command == 5:
		#print out list to console
		for i in patientList:
			print(i , "\n")
		
	elif command == 6:

		#write list to file (write file)
		list_write(patientList)
		
	elif command == 0:
		print("EXITING\n")
	else:
		print("INVALID INPUT\n")