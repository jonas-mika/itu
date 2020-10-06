##########
# Exercises 10 - Algorithm Design and Complexity
##########

# Author		: 	Jonas-Mika Senghaas
# Date Created	:	23.09.2020

############
# Exercise 1: Bubble Sort Algorithm
############

list_to_sort = [2,1,3]

def bubble_sort(list_to_sort : [], order : str):
    ordered_list = []
    length_of_list = len(list_to_sort)
    
    if order == "descending":
        for i in range(length_of_list-1):
            for j in range(0, length_of_list-i-1): 
                if list_to_sort[j] > list_to_sort[j+1]:
                    list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    
        for i in range(length_of_list):
            ordered_list.append(list_to_sort[i])
    
    elif order == "ascending":
        for i in range(length_of_list-1):
            for j in range(0, length_of_list-i-1): 
                if list_to_sort[j] < list_to_sort[j+1]:
                    list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    
        for i in range(length_of_list):
            ordered_list.append(list_to_sort[i])

    else: 
        print("Please insert how the list should be sorted")

    return ordered_list

#print(bubble_sort(list_to_sort, "ascending"))
#print(bubble_sort(list_to_sort, "descending"))

############
# Exercise 2: Deerypton on message
############

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb."
message1 = "jonas"

encryption = {
    "k": "m",
    "o": "q",
    "e": "g"
}

def decode(message : str, encryption : dict):
    my_keys = list(encryption.keys())
    val_keys = list(encryption.values())

    encrypted_message = ""

    for character in message:
        try:
            replaced_character = character.replace(my_keys[0], val_keys[0])
            replaced_character = character.replace(my_keys[1], val_keys[1])
            replaced_character = character.replace(my_keys[1], val_keys[2])
        except: 
            replaced_character = character

        encrypted_message += replaced_character
        
    return encrypted_message

#Driver Code
#print(decode(message, encryption))

############
# Exercise 3: Find Pattern in Text File
############

import re

file = "bigmess.txt"

def find_in_file(file):
    L = []

    with open(file, "r") as infile:
        read_lines : [str] = infile.readlines()
        lines : str = "".join(str(element).strip() for element in read_lines)
        
    matches : list = re.findall("[A-Z]{3}[a-z][A-Z]{3}", lines)

    for match in matches:
        L.append(match[3])

    return L

#print(find_in_file(file))
print(len(find_in_file(file)))


############
# Exercise 4: List Slicing and Indexing
############

example_list = ["a","b","c","d","e"]

def rotate(L : [str], num_rotation):
    pass

def flip(L : [str]):
    flipped_list = []

    for item in L:
        flipped_list.insert(0, item)

    return flipped_list

#print(flip(example_list))

############
# Exercise 5: Lists and Loops
############

def elim_cons_duplicates(L : [str]):
    pass
