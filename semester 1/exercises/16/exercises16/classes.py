# test on classes

import numpy as np
import csv
import datetime
from dateutil.relativedelta import relativedelta

class Person:
    human_rights = "This is a person with Human Rights."
    
    def __init__(self, name, birthday):
        # assert type(name) == str, "Please insert a valid String as Name"
        # assert type(birthday) == str, "Please insert your birthday in the format DD/MM/YYYY as String"
        
        self.name = name
        self.birthday = birthday
        self.age = self.getAge()

    def getName(self):
        return self.name

    def getBirthday(self):
        return self.birthday.replace("/", ".")

    def getAge(self):
        day, month, year = [int(i) for i in self.birthday.split("/")] # format day, month and year input to fit datetime method 
        birthday = datetime.datetime(year, month, day) # store datetimeobject in birthday var
        current_date = datetime.date.today() # get current date 

        return relativedelta(current_date, birthday).years

    def timeToBirthday(self):
        current_date = datetime.date.today()
        day, month, _ = [int(i) for i in self.birthday.split("/")]
        next_birthday = datetime.datetime(current_date.year + 1, month, day)
    
        next_birthday = relativedelta(current_date, next_birthday)
     
        if abs(next_birthday.months) == 0:
            if abs(next_birthday.days) == 1:
                message = f"{self.name}'s birthday is tomorrow!"
            elif abs(next_birthday.days) == 0:
                message = f"{self.name}'s birthday is today!"
            else:
                message = f"{self.name}'s birthday is {abs(next_birthday.days)} days away"
        else:
            message = f"{self.name}'s birthday is {abs(next_birthday.months)} months and {abs(next_birthday.days)} days away." 

        
        return message

    def __str__(self):
        return f"Name: {self.getName()}\nBirthday: {self.getBirthday()}\nAge: {self.age}"


person1 = Person("Jonas-Mika Senghaas", "28/01/2002")
person2 = Person("Tanja Senghaas-Thomsen", "23/09/1970")

list_of_people = [person1, person2]

for person in list_of_people:
    print(person)
    print("-->" + person.timeToBirthday() + "\n")
