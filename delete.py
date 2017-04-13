#from test import *



#class removePatient:
	
    #	def search (list,name):
	#	counter = -1;
	#	for l in list:
	#		counter = counter + 1;
	#		if list[counter].getName().strip('\n') in name:
	#			return True;

#	def readFile():
#		counter = 0
#		a=[0]
#		f = open('patient.txt', 'r')
#		for line in f:
#			#print(line, end=' ')
#			name= f.readline()
#			ssn= f.readline()
#			sex= f.readline()
#			birthday= f.readline()
#			description= f.readline()
#			blank= f.readline()
#			a[counter]= Patient(name, ssn, sex, birthday, description)
#			counter +=1
#			a.append(counter)
#		a.pop()
#		return a;

def remove(theList):
    patient = (input("Enter the SSN who you want to Delete:"))
    counter = -1
    for l in theList:
        counter = counter + 1
        if theList[counter].ssn == patient:
            del theList[counter]
            print("PATIENT HAS BEEN REMOVE\n")
    return theList
