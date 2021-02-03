# fibonacchi recursively 

# 0 1 1 2 3 5 8 13 ...

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)


# working with files
def load_csv_into_dict(filename):
    with open(filename, "r") as infile:
        headers = [header for header in infile.readline().strip().split(",")]
        contents = [[element for element in line.strip().split(",")] for line in infile.readlines()]
        ans = {header: [] for header in headers}

        for row in contents:
            for x, element in enumerate(row):
                if element.isnumeric():
                    ans[headers[x]].append(int(element))
                else: ans[headers[x]].append(element)

    return ans
    
# print(load_csv_into_dict("test.csv"))

def find_most_common(int_list):
    uniques = set(int_list)
    count_dict = {x: 0 for x in uniques}

    for val in int_list:
        count_dict[val] += 1
    
    return [x for x in count_dict if count_dict[x] == max(count_dict)]

import collections

def find_most_commmon_collections(L):
    return [x[0] for x in collections.Counter(L).most_common() if x[1] == max(collections.Counter(L))]

# print(find_most_common([1,1,2,2,2,1,3]))
# print(find_most_commmon_collections([1,1,2,2,2,1,3]))

import itertools

class Employee:
    count = 0
    yearly_bonus = 0.03

    @classmethod
    def incr(cls):
        cls.count += 1
        return cls.count

    def __init__(self, fname, lname, hourly_pay):
        self.fname = fname
        self.lname = lname
        self.name = f"{fname} {lname}"
        self.pay = hourly_pay
        self.id = self.incr()

    def __str__(self):
        return f"[{self.id}] {self.name}: {self.pay} (DKK/h)"

    def __repr__(self):
        return f"<Employee Object: {self.name}({self.id})>"

emp1 = Employee("Jonas", "Senghaas", 120)
emp2 = Employee("Tildi", "Völcker", 150)

list_of_employees = [emp1, emp2]

# print(list_of_employees)

import csv

with open("test.csv", "a") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["\n6", "Tanja Senghaas", "50"])


with open("test.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    data = [line for line in reader][1:]

#print(data)

def sum_of_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] + sum_of_list(L[1:])

# print(sum_of_list([1,3,7]))

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

#print(fact(6))

infile = open("test.txt","r")

#lines = [line.strip() for line in infile.readlines()]
#print(lines)

# lines = []
# for line in infile:
#     lines.append(line.strip())

lines = [line.strip() for line in infile]
print(lines)