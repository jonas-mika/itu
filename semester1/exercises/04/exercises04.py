# Exercises_04 - Programs and Types
# Date: 2nd September 2020
# TA: Simon (smbr@itu.dk )

###########
#Recursive Function
###########

def mainRecursion ():

	userString = input ("Enter the string you want to be repeated: ")
	userCounter = eval(input("How many times do you want this string to be outputted?: "))

	def forLoop (string, counter): 
		if counter >0:
			print(string)

			if counter != 0:
				forLoop (string, counter-1)
			else:
				return

	forLoop (userString, userCounter)





myList = [1,2,3,4,5,6,7,8,9]

def countEvenNumbers (myList):
	if myList == []:
		return 0 
	our_number = myList[0]
	num_evens = countEvenNumbers(myList[1:])

	if our_number % 2 == 0 :
		num_evens += 1 # num_evens = num_evens + 1

	return num_evens

# print(countEvenNumbers(myList))

##########
# Program to give the Data Type of a Input-List
##########

datalist = [1452, 11.23, 1+2j, True, "w3resource", (0,-1), [5,12]]

def giveType (L):
	if L == []:
		return  

	item = L[0]
	print ("Data Type: ", type(item))

	return giveType(L[1:])


##########
# Program to count from 0-6, except for 3 and 5
##########

def count (x):
	if x == 7: 
		return

	if x!=3 and x!=5: 
		print (x)

	count(x+1)
	
##########
# Program to output Grade, depending on Score as input
##########

def main():
	score = eval(input("Enter the achieved score (0-100): "))

	def calcGrade (score): 

		if score>=90 and score<=100:
			print("Your score is: ", score, "\nGrade: A")

		elif score>=80 and score<=89:
			print("Your score is: ", score, "\nGrade: B")

		elif score>=70 and score<=79:
			print("Your score is: ", score, "\nGrade: C")

		elif score>=60 and score<=69:
			print("Your score is: ", score, "\nGrade: 0")

		elif score<60:
			print("Your score is: ", score, "\nGrade: F")

		else: 
			print ("Something went wrong here! Try inputting a number between 0 and 100")

	calcGrade(score)

#########
# Program to print out Feedback on BMI
#########

def main2():

	userWeight = eval(input("Please enter your weight (in kg): "))
	userHeight = eval(input("Please enter your height (in m): "))

	def calcBMI (weight, height): 
		bmi = weight/(height**2)
		return bmi 

	def giveFeedback (valueBMI): 
		if valueBMI <19: 
			print ("Your BMI is:", valueBMI,"\nYou are below, what is considered to be healthy")

		elif valueBMI >25: 
			print ("Your BMI is:", valueBMI,"\nYou are above, what is considered to be healthy")

		else: 
			print ("Your BMI is:", valueBMI,"\nYou are right at the sweet spot of your BMI. You are very healthy")

	giveFeedback(calcBMI(userWeight, userHeight))

############
# Program, to test whether a year is a leap year
############

def main3():

	yearToTest = eval(input("Put in a Year to test, if it is a leap year: "))

	def testIfLeap (year):

		if year % 4 == 0:
			if year % 100 == 0 and year %400 !=0:
				print ("The year ", year, "was not a leap year") 

			else:
				print ("The year ", year, "was a leap year!")  

		else : 
			print ("The year ", year, "was not a leap year")

	testIfLeap (yearToTest)

###########
# Logic Problems with Booleans - See the Slide and try them out in the terminal
###########

##########
# Program to calculate Factorial of the input
##########

def mainFactorial():

	userNumber = eval(input("Get the factorial of: "))

	def calcFact (number):
		if number == 0: 
			return 1

		return number * calcFact (number-1) 

	print("This is the factorial of",userNumber,"is:   ", calcFact (userNumber))


##########
# Program to calculate the length of a String-Input
##########

def mainCalcString (): 

	userInput = input("Get the length of: ")
	
	def findLength (string): 
		
		for i in string: 
			count += 1
		return count

	print(findLength(userInput))










