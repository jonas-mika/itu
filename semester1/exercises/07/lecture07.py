###################
# encoding/decoding
###################
# ord('a')
# chr(97)
# ord(chr(99))
# chr(ord('ø'))

###################
# string operations, 
###################
#strip
a_string = "hello     \n this is next line :-)   \n"
print(a_string)
#trim leading and trailing whitespace.
#whitespace: space, newline, tab, + some more exotic ones
a_string.strip() 

# ex: date conversion
# Input the date in mm/dd/yyyy format (dateStr)
# Split dateStr into month , day and year strings
# Convert the month string into a month number
# Use the month number to look up the month name
# Create a new date string in form Month Day, Year
# Output the new date string


def convert_date():
	# get the date
	dateStr = input("Enter a date (dd/mm/yyyy): ")
	# split into components
	dayStr, monthStr, yearStr = dateStr.split( "/" )
	# convert monthStr to the month name
	months = ["January", "February", "March", "April",
	"May", "June", "July", "August",
	"September", "October", "November", "December"]
	monthStr = months[int(monthStr)-1]
	# output result in month day, year format
	print("The converted date is:",dayStr + ".", monthStr + ",", yearStr)

####################
# template string formatting
####################
def convert_date_2():
	# get the date
	dateStr = input("Enter a date (dd/mm/yyyy): ")
	# split into components
	dayStr, monthStr, yearStr = dateStr.split( "/" )
	# convert monthStr to the month name
	months = ["January", "February", "March", "April",
	"May", "June", "July", "August",
	"September", "October", "November", "December"]
	monthStr = months[int(monthStr)-1]
	# output result in month day, year format
	#output = "The converted date is: {0}. {1}, {2}".format(dayStr, monthStr, yearStr)
	output = "The converted date is: {day}. {month}, {year}".format(day=dayStr, month=monthStr, year=yearStr)
	print(output)

####################
# file processing
####################
# Prints a file to the screen.
def print_file():
	fname = input( "Enter filename : " )
	infile = open(fname , "r" )
	data = infile.read()
	print(data)

###################
# regex
###################
import re
def main():
	pattern = '^a...s$'
	test_string = 'abyss'
	#test_string = 'abyt'
	result = re.match(pattern, test_string)
	if result: #testing result is not None
		print(result)
		print("Search successful.")
	else:
		print(result)
		print("Search unsuccessful.")

###################
#regex examples
###################
re.findall("a", "ga6hjhjerahhhaa")
re.findall("[ah]", "ga6hjhjerahhhaa")
re.findall("ah", "ga6hjhjerahhhaa")
re.search("a", "ga6hjhjerahhhaa")
re.sub("a","", "ga6hjhjerahhhaa")
re.findall("[^ah]", "ga6hjhjerahhhaa")

re.findall("ab*", "aba.aabbbbbbb")

re.search("\d", "abc4")
re.match("t...\$", "the $")

####################
# the finite automata regex examples
####################
regex = "(b*ab*ab*)*"
re.match(regex, "")
re.match(regex, "aa")
re.match(regex, "babbbbabaa")

#################
# text from url - find all links with regex
#################

import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context

url='https://www.thedanishparliament.dk/en/political-parties'
with urllib.request.urlopen(url) as response:
   html = response.read().decode('utf-8')#why utf-8

#links = re.findall('href=\".*\"', html)
#links = re.findall('href=\"http.*\"', html)
links = re.findall('href=\"http\S*\"', html)

   



