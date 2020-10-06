
#lecture05
###################
# definite loop - 'for' statement
###################
# for i in [0,1,2,3]: 
#    print(i)

# for i in "hello":
# 	print(i)

###################
# indefinite loop - 'while' statement
###################
i=0
while i <= 10: #as long as this is true...
	print(i)
	i = i + 1
 
################ 
################
# interactive loop
###############
def main():
	total = 0.0
	count = 0
	moredata = "yes"
	while moredata [0] == "y":
		x = float(input("Enter a number >> "))
		total = total + x
		count = count + 1
		moredata = input("Do you have more numbers (yes or no)? ")
	print("\nThe average of the numbers is", total / count)

if __name__ == '__main__': main()

####################
# sentinel loop
####################
def sentinel():
	total = 0.0
	count = 0
	x = float(input("Enter a number (negative to quit) >> "))
	while x >= 0:
		total = total + x
		count = count + 1
		x = float(input("Enter a number (negative to quit) >> "))
	print("\nThe average of the numbers is", total / count)


####################
# file loop
####################
def file_loop():
	fileName = "numbers.txt"
	infile = open(fileName, 'r')
	total = 0.0
	count = 0
	for line in infile:
		total = total + float(line)
		count = count + 1
	infile.close() #good practice to free up resource
	print("\nThe average of the numbers is", total / count)


####################
# nested loop
#####################
def nested():
	infile = open("numbers_line.csv", 'r')
	total = 0.0
	count = 0
	line = infile.readline()
	while line != "":
		# update total and count for values in line
		for xStr in line.split(","):
			total = total + float(xStr)
			count = count + 1
		line = infile.readline()
	print("\nThe average of the numbers is", total / count)
	
####################
# sentinel with break
####################
def sentinel_with_break():
	total = 0.0
	count = 0
	while True:
		x = float(input("Enter a number (negative to quit) >> "))
		if x < 0: break
		total = total + x
		count = count + 1
		x = float(input("Enter a number (negative to quit) >> "))
	print("\nThe average of the numbers is", total / count)

#####################
# list comprehension
#####################
def even_numbers(limit):
	nums = []
	for i in range(limit):
		nums.append(2*i)
	return numbers

#short version 
x = [2*x for x in range(50)]

#also works for set
x = {2*x for x in range(50)}

