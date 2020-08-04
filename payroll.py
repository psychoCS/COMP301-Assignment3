''' 
Name: copyfile.py
Author: Thiago Batista
Student Number: 301110966
Description: Assignment 3 - Task2
Program: COMP301
Date: 04/08/2020
'''

#Task 2: The Payroll Department keeps a list of employee information for each pay period in a text file called data.txt. Write a script, payroll.py that reads the data.txt file and outputs the wages paid to each employee in tabular format to the console. (20 Marks: Functionality).


#a. Create a data.txt so that it creates 10 employee records. Each employee record should be comma separated and structured in the following way <Employee Number>,<LastName>,<FirstName>,<Hours Worked> (5 Marks: Functionality). - Done

# b. Write payroll.py so that it reads data.txt and outputs each employee Record in a three column table nicely formatted with a Header Row that includes the following Employee Number | Employee Name | Hours Worked (15 Marks: Functionality)


import csv

with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print()
            print("-----------------------------------------------")
            print(f"|Employee Number|Employee Name\t|Hours Worked\t|")
            print("-----------------------------------------------")
            line_count += 1
        

