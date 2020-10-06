# happyBirthday.py
# A PROGRAM, THAT SINGS "HAPPY BIRTHDAY
# created by Jonas-Mika Senghaas, 31st August 2020

personName = input ("What is your name?: ")
lineGeneral = "Happy birthday to you!"

def linePerson (personName) : 
	print ("Happy birthday, dear", personName, "!")

def song () : 
	print (lineGeneral)
	print (lineGeneral)
	linePerson (personName)
	print (lineGeneral)

song ()


