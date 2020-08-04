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

# We'll need the Comma Separator Value to transform the data.txt into 'chunks of data' that we can use on the table, so let's start by importing the CSV library
import csv

# Then we open the data as a CSV file, separating the 'chunks' by the comma
with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Lets create the Header Row    
    print
    print(f"\n\t\t\tAvengers Worked Hours")
    print(f"\n\t-----------------------------------------------")
    print(f"\t|Employee Number|Employee Name\t|Hours Worked\t|")
    print("\t-----------------------------------------------")

    # Finaly one loop that goes line by line od the data file, putting it in a formatted table.
    employees = 0
    for avenger in csv_reader:
        print(f'\t|\t{avenger[0]}\t|\t{avenger[2]}\t|\t{avenger[3]}\t|')
        print("\t-----------------------------------------------")
        employees += 1

    # And just for fun lets count the number of 'Employees' found on the payroll
    print(f'\n\t\t\tFound {employees} avengers.\n')