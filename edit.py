#created By: Brian Onesto
#date: 11-07-15
#for: python 223 Project, medical office records keeper
import tkinter
from readFile import readText #need to use the module created by Minh Nguyen
from readFile import Patient
import search # this module will search to see if the file they want to edit exist.


class EditRecord(): 
       
       #    def editRecord(self):
       #patient = input("Enter the patient name you want to edit:")
        #if name matches ask what they want to edit
        #if patient in readText():
        #    print('patient is in our system')
        #else:
        #    print('patient does not exist in our system')
            
    def implementEdit(theList):
        
        #GET INDEX OF ELEMENT IN THE LIST
        ssn = input("ENTER PATIENT SSN YOU WISH TO EDIT: ")
        
        i = -1
        for l in theList:
            i = i + 1
            if theList[i].getSsn() == ssn:
                break
    #by this point i is the index
    
        
        print('what would you like to change?')
        editChoice = int(input("enter 1 for editing name\n, 2 for editing SSN\n, 3 for editing gender\n, 4 for editing DOB\n,5 for editing description\n, 6 to cancel\n"))
        if editChoice == 1:
            #edit name
            print('current name is: ', theList[i].getName())#display Name
            nameChange = input('enter name edit here-> ')
            theList[i].setName(nameChange)
        
        elif editChoice == 2:
            #edit SSN
            print(' current SSN is: ', theList[i].getSSN())#display SSN
            ssnChange = input('enter SSN edit here-> ')
            theList[i].setSSN(ssnChange)
        elif editChoice == 3:
            #edit Gender
            print('current gender is: ', theList[i].getGender())#display gender
            genderChange = input('enter gender edit here-> ')
            theList[i].setGender(genderChange)
        elif editChoice ==4:
            #edit DOB
            print('current DOB is: ', theList[i].getBirthday())    #display DOB
            dobChange = input('enter DOB edit here-> ')
            theList[i].setBirthday(dobChange)
        elif editChoice ==5:
            #edit description
            print('current description is: ', theList[i].getDescription()) #display Description
            descriptionChange = input('enter description edit here-> ')
            theList[i].setDescription(descriptionChange)
            
        elif editChoice ==6:
            print('going back home: ')
            #back to main menu             
        elif editChoice >= 7 | editChoice <= 0:
            print('you entered a wrong number')
        else:
            print('thanks for trying, ')
        return theList


    #   def changeRecord(self):
        #open the file with module from readFile
    #    readText()
        #user change Dang Phan to Dang Awesome
         #Dang Phan
        #assign a[0].name = a[0].name = 'Dang Awesome'    
        #change the Record with new Change
def main():
    changeRecord = EditRecord()
    changeRecord.editRecord()
    
    searchResult = find() # object to search for existing name    
    Read = readText()
    
if __name__ == "__main__": main()




