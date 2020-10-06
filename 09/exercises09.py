##########
# Exercises 09 - Dictionaries and collections comprehensions
##########

# Author		: 	Jonas-Mika Senghaas
# Date Created	:	21.09.2020

###############
# Exercise 1 
###############

def build_pet_dict():
	myPet = {}
	
	myPet["name"] = "Spot"
	myPet["animal"] = "dog"
	myPet["fav_snack"] = ["sausages", "peanutbutter", "droppedpopcorn"]

	return myPet

#print(build_pet_dict())

###############
# Exercise 2 
###############

inventory = { 
	'gold' : 500,
	'pouch' : ['flint', 'twine', 'gemstone'],
	'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'] 
	}

def modify_dict(my_dict):
	my_dict["pocket"] = ["seashell", "lint"]
	my_dict["backpack"].sort()
	my_dict["backpack"].remove("dagger")
	my_dict["gold"]+=50
	return my_dict

#print(modify_dict(inventory))

###############
# Exercise 3 
###############

def open_text_file(file):
	L = []

	with open(str(file), "r") as infile:
		for line in infile: 
			L.append(line.strip().lower())

	return L

words = open_text_file("JFK.txt")
#print(words)

def find_unique_words(words):
	return set(words)

unique_words = find_unique_words(words)
#print(unique_words)

def create_dict(unique_words, all_words):
	word_count_dict = {}

	for unique_word in unique_words:
		word_count_dict[unique_word] = 0
	for word in all_words:
		word_count_dict[word] += 1

	return word_count_dict

#print(create_dict(unique_words, words))

###########
# Exercise 04 - List Comprehension
###########

L1 = [i for i in range(10)]
#print(L1)

L2 = [i**2 for i in L1]
#print(L2)

L3 = [i**3 for i in L1 if i%2 != 0]
#print(L3)

###########
# Exercise 05 - Dictionary Comprehension
###########

students = {
"dennis": 23,
"david": 21,
"mary": 9,
"daniel": 25, 
"darius": 17,
"jim": 10, 
"marvin": 19
}

students_upper = {i.upper():students[i] for i in students}
#print(students_upper)

students_over_18 = [i.capitalize() for i in students if students[i]>=18]
print(students_over_18)

