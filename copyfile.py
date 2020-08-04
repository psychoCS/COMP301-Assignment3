''' 
Name: copyfile.py
Author: Thiago Batista
Student Number: 301110966
Description: Assignment 3 - Task1
Program: COMP301
Date: 04/08/2020
'''

#Task 1: Write a python console script named copyfile.py. This script will copy the contents of one file into another file

#a. The console script will prompt the user for two file names (Source and Destination) (4 Marks Functionality)
print()
print("We will copy the contents of one file into another file")
print()

# Prompt the user for the first file 
print("So please, enter first the name of the file that will have its contents transfered")
firstFile = input()
print()

# Prompt the user for the second file
print("Now enter the name of the file that will receive this information")
secondFile = input()
print()
print("Ok. Lets transfer the content of the files")
print()

#b. After the user enters the Destination file name the scripty will copy the contents of the Source file into the Destination file (6 Marks Functionality).
class FileCopier():

    # lets take the 2 user imputs 
    def copier(self,firstFile,secondFile):
        print()

    # Open the first file and save its lines on a variable
    with open(firstFile,'r')as fileData:
        firstFileContent= fileData.readlines()
        print("Reading the content on the first file...")
        print()

    # Open the second file and save its lines on a variable
    with open(secondFile,'r')as fileData:
        secondFileContent= fileData.readlines()
        print("Reading the content on the second file...")
        print()

    # Pick each line of the second file and add it to the first one
    for eachline in firstFileContent:
        secondContent = open(secondFile,'a')
        secondContent.write(eachline)
    print("Done. Content from the first file transfered to the second one")
    print()