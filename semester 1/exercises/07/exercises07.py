##########
# Exercises 07 - String Formatting, Files and URL
##########

# Author		: 	Jonas-Mika Senghaas
# Date Created	:	14.09.2020

import re
import random

#########
# Exercise 1 - Format String that changes Capitalization
#########

def change_cap():
	string = input("Example String: ")
	new_string = ""

	for character in string:
		if character.islower():
			new_string += character.upper()
		else:
			new_string += character.lower()
	return new_string

def change_cap_2(string):
	return string.swapcase()


#########
# Exercise 2 - Write a function that will take a string as input and return a version stripped of trailing whitespace.
#########

def cut_spaces(string):
	return string.strip()

#########
# Exercise 3 - Replace a with 4
#########

def swap_a_4(string):
	return string.replace("a", "4")

#########
# Exercise 4 - Hide Letters/ Digits in a String
#########

def hide_letters(string): #without regex
	new_string = ""

	for character in string:
		if character.isalpha():
			new_string += "*"
		else:
			new_string += character

	return new_string

def hide_digits(string):
	return re.sub(r"\d", "*", string)

#########
# Exercise 5 - Function to have a separator at thousands
#########

def thousand_separator(amount):
	return "I wish I had {amount:,}$".format(amount=amount)

#########
# Exercise 6 - Insert formatted String 
#########

def string_formatting(s1, s2):
	return "My name is {name}, I am from {country}".format(name=s1.capitalize(), country=s2.capitalize())


#########
# Exercise 7 - 
#########

def openfile(filename):
	L = []
	file = open(filename, "r")
	
	for line in file: 
		L.append(line.strip())
		
	return L

#########
# Exercise 8 - Write to a file
#########

def write_file(L):
	outfile = open("output.txt", "w")
	L2 = []

	for item in L:
		if item.isalpha():
			L2.append(item.lower())

	outfile.writelines("\n".join(L2))
	print ("The List", L2, "was successfully inserted in Document output.txt")

#########
# Exercise 9 - RegEx Search Patterns 
#########

# Search for occurence a9

def regex_search(string):
	regex = "a9"

	return len(re.findall(pattern, string))

# Check if format is e-mail

def check_email(email):
	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

	if re.search (regex, email):
		print("Valid Email")
	else:
		print("Invalid Email")























