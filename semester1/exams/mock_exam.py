# program flow

def program_flow():
    i=0
    while i<= 100:
        if 2*(i // 2) + (i % 2) == 0:
            print(i) 
        i+=1

#program_flow()

def secret_operation(s, i):
    m = int(len(s)/2) # store the half of the length of the string in a inteture variable called m (rounded down, if odd nnumber len(s))
    if m+i+1>=len(s): # Return True if m+1 is greater or equal to the length of the string
        return True
    elif s[i] != s[-m+i]: # Return False if the string at index i is not equal to 
        return False 
    else:
        return secret_operation(s,i+1) # recursive step -> search in next 

#print(secret_operation("jonasjonaw",0))

# m = 3
# i = 0
# if: 4 is not greater equal to 6
# elif: s[0] == s[-3] so no execution
# else: recursion with i+1

# i=1
# if: 5 is not greater equal to 6
# elif: s[1] == s[-3] so no execution

# i=2
# if condition holds: 3+1+2 == 6
# return True

def sum_of_cubes(n):
    if n==1:
        return 1
    return n**3+sum_of_cubes(n-1)

# print(sum_of_cubes(3))

import numpy as np

# print(np.percentile([20,30,30,30,50,58,80,80,85,90],[0,25,50,75,100]))

class Employee:
    empCount = 0
    
    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print("Total Employees: ", Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
Employee.displayCount(emp1)

emp2.displayEmployee()


