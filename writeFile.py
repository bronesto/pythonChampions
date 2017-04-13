#Alec Nghiem
#write function module
#894441831

import sys, os

def list_write(n):         #function to define for the write pass a list in

    filename = input('Please enter a filename you wish to save to.' + '\n')
    filename = filename + '.txt'
    with open(filename,'wt') as f:   #opens the file to write into

        for i in range(0,len(n)):          #writes each object into the file

            f.write('\n')
            f.write(n[i].name)
            f.write('\n')
            f.write(n[i].ssn)
            f.write('\n')
            f.write(n[i].gender)
            f.write('\n')
            f.write(n[i].birthday)
            f.write('\n')
            f.write(n[i].description)
            f.write('\n')
            
            
            
        
    print('New patient list has been saved to ' + filename + '\n')
