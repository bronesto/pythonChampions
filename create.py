#Dang Phan
#CPSC 223P-01
#Group: Titans of Python
#last modified date: 11 17 2015

import readFile			#or from a module that takes care of reading
				#from text file, created by Minh Nguyen
from readFile import Patient	#to use the Patient class from the readFile module
#import ursula_rosamonteirodecastro #the module taking care of search function
#import  search
import sys, os
import re 		#use to check input information

#get the patient list from readFile module
#def getTheList():
#	tempArry = readFile.readText()
#	return tempArry

#check validation of full name (only firstName-'space'-lastName as Tony Lee)
def checkName(prompt):
	nameRegex = re.compile("^[^\W_]+( [^\W_]+)?$")
	while True:
		tempN = input(prompt)
		if re.match(nameRegex, tempN) is None:
			continue
		else:
			return tempN

#check validation of SSN (9 digit numbers only as 123456789)
def checkSSN(prompt):
	SsnRegex = re.compile("\d{9}$")
	while True:
		tempS = input(prompt)
		if re.match(SsnRegex, tempS) is None:
			continue
		else:
			return tempS

#check validation of gender (Male or Female) 
def checkGender(prompt):
	genderRegex = re.compile("(Male)$|(Female)$")
	while True:
		tempG = input(prompt)
		if re.match(genderRegex, tempG) is None:
			continue
		else:
			return tempG

#check validation of birthday 
def checkBOD(prompt):
	bdRegex = re.compile("\d{2} \d{2} \d{4}$")
	while True:
		tempB = input(prompt)
		if re.match(bdRegex,tempB) is None:
			continue
		else:
			return tempB

#search for existing SSN in the current patient List
def find(aList, ssn):
	counter = -1
	value = False
	for i in aList:
		counter += 1
		if aList[counter].getSsn() == ssn:
			value = True
	return value
			
	
#create new patient's record and return an array of updated patient list
def newPatient(theList):
	#to get the list of patient from text file
	patientArr = theList

	#initial conditions for while-loop
	stop ='y'
	
	while stop == 'y':
		SSN = checkSSN('Patient SSN (in format #########): ')
		if find(patientArr,SSN):
			print ('This SSN is already recorded')
		else:
			name = checkName('Patient Name (FirstName LastName only): ')
			gender = checkGender('Patient Gender (Male or Female): ')
			birthD = checkBOD('Patient Birthdate (in format ## ## ####): ')
			msg = input('Any message or description along with this patient: ')
			newPatient = Patient(name,SSN,gender,birthD,msg)
			patientArr.append(newPatient)
		stop = input('Press \'y\' if you want to continue to add other new patient or any character if you want to stop: ')
	return patientArr

#test print
#temp = newPatient()
#print(temp)
