''' 
Name: copyfile.py
Author: Thiago Batista
Student Number: 301110966
Description: Assignment 3 - Task2
Program: COMP301
Date: 04/08/2020
'''

#Task 2: The Payroll Department keeps a list of employee information for each pay period in a text file called data.txt. Write a script, payroll.py that reads the data.txt file and outputs the wages paid to each employee in tabular format to the console. (20 Marks: Functionality).


#a. Create data.txt so that it creates 10 employee records. Each employee record should be comma separated and structured in the following way <Employee Number>,<LastName>,<FirstName>,<Hours Worked> (5 Marks: Functionality). - Done

# b. Write payroll.py so that it reads data.txt and outputs each employee Record in a three column table nicely formatted with a Header Row that includes the following Employee Number | Employee Name | Hours Worked (15 Marks: Functionality)

#step 1 is open a file
fileObject = open("data.txt", "r")

#step 2 - read from the file
contents = fileObject.read()

#step 3 - close out
fileObject.close()


print(contents)


fileObject = open("numbers2.txt", "w+")
numbers = [33, 55, 66, 77, 88, 99, 110, 121]

count = 0

for number in numbers:
    count += 1
    if count == len(numbers):
        fileObject.write(str(number))
    else:
        fileObject.write(str(number) + ",")

fileObject.close()