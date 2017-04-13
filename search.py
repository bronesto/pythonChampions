#created by Ursula Rosa Monteiro de Castro
#updated by Minh Nguyen 11/12
import sys, os
import readFile			#or from a module that takes care of reading
				#make sure you put patient.txt and readFile.py and this file in the same directory
from readFile import Patient

#def getTheList():
#	tempArry = readFile.readText()
#	return tempArry

def search (theList):  #pass in the list from main to search through!
	mainList = theList
	#receive the list where the information about patient are
	counter = -1;
	patient = input("ENTER SSN TO CHECK IF RECORD EXISTS:")
	for l in mainList: #search in the list
		counter = counter + 1
		if mainList[counter].getSsn() in patient:
			name = mainList[counter].getName() #get the name
			ssn = mainList[counter].getSsn() #get the ssn
			sex = mainList[counter].getGender() #get the sex
			birthday = mainList[counter].getBirthday() #get the birthday
			description = mainList[counter].getDescription() #get the description

			print("Name: " , name, "SSN: ", ssn, "Sex: ", sex, "Birthday: ", birthday, "Description: ", description)
    	

#search()
# enter the ssn, then this function will print out directly the info 
#you can modify this list to return array, bool or a value needed for your module  
#updated the module name to search.py for easy import calling





#UPDATED 11/18 added this second function.
#to be used before calling other people's functions in main module
#THIS SEARCH RETURNS TRUE OR FALSE ONLY, not information 
def find (theList):  #pass in the list from main to search through!
	mainList = theList
	#receive the list where the information about patient are
	value = False
	counter = -1;
	patient = input("ENTER SSN TO CHECK IF RECORD EXISTS:")
	for l in mainList: #search in the list
		counter = counter + 1
		if mainList[counter].getSsn() in patient:
			value = True
	return value