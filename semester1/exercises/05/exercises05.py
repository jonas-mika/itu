##########
# Exercises 05 - Loops
##########

# Author		: 	Jonas-Mika Senghaas
# Date Created	:	07.09.2020

import random

###########
# Ecercise A - Output number of items in list using for-loop
###########

def lenList(): 
	exList = [1,2,3,4,5,6,7]
	count = 0

	for i in exList: 
		count = count + 1
	return count

##########
# Exercise B - Take list of Integers and return max number
##########

def maxNo():
	exList = [1,2,3,4,5,10,7]
	max_number = 0

	for i in exList:
		if i > max_number:
			max_number = i
	return max_number

#########
# Exercise C - Reverse a list of Integers
#########

def reverseList():
	exList = [1,2,3,4,5,10,7]
	newList = []

	for i in exList:
		newList.insert(0, i)
	return newList

#########
# Exercise D - Sum all Elements of a List
#########

def sumList():
	exList = [1,2,3,4,5,10,7]
	curr_sum = 0

	for i in exList:
		curr_sum += i
	return curr_sum

#########
# Ecercise E - Guess No. between 1-10
#########

def gameGuess():
	solution = random.randint(1,10)
	guessed = False

	while not guessed: 
		guess = int(input("Guess a Number between 1 and 10 >> ")) 
		if guess == solution: 
			guessed = True
			print ("Congrats. Your are right. The number was", solution)
		else: 
			print ("No, that was not the number. Try again")

########
# Exercise F - Construct Pattern
########

def constructPattern(depthUser):
	depth = 1
	item = "*"
	max_depth = depthUser
	
	
	for i in range (max_depth):
		print (item * depth)
		if depth < max_depth:
			depth += 1
	for i in range (max_depth - 1):
		depth -= 1
		print (item * depth)
		














