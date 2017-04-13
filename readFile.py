#created by Minh Nguyen
import sys, os 

#creating a class of patient
class Patient:
    def __init__(self, name, ssn, gender, birthday, description):  #initialize the input values
        self.name=name
        self.ssn=ssn
        self.gender=gender
        self.birthday=birthday
        self.description=description
	
	#when you call these functions below it will return the value you need
    def __repr__(self):
        return (self.name+self.ssn+self.gender+self.birthday+self.description)
    def getName(self):
        return (self.name)
    def getSsn(self):
        return (self.ssn)
    def getGender(self):
        return (self.gender)
    def getBirthday(self):
        return (self.birthday)
    def getDescription(self):
        return (self.description)
    def setName(self, new_name):
        self.name = new_name
    def setSSN(self, new_ssn):
        self.ssn = new_ssn
    def setGender(self, new_gender):
        self.gender = new_gender
    def setBirthday(self, new_birthday):
        self.birthday = new_birthday
    def setDescription(self, new_description):
        self.description = new_description





def readText():
	patients=[] 		#array of patients
	rows = None
	#copy everthying in the text file into a temporary array
	with open('patient.txt', 'r') as f: 		
		arr = f.read().splitlines()
		f.close()
	#print (arr)	
	i = 0
	#the while loop here takes care of get a patient info
	while i < len(arr):
		name = arr[i]
		ssn = arr[i+1]
		gender = arr[i+2]
		birthday = arr[i+3]
		description = arr [i+4]
		#print ('record =',name, ssn, gender, birthday, description)
		#1 index of the array is 1 patient (a instance of Patient class)
		patients.append(Patient(name, ssn, gender, birthday, description))
		i += 6
	return patients

#test the patient array
#a = readText()	# a now contains the array of patients

#examples of how to use this array:
#print (a[3]) #print patient index 3's entire info
#print (a[2].getSsn()) # print patient index 2's ssn
#print (a) #print entire array of patients

	

