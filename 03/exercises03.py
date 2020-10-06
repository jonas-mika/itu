# Exercises_03
# Date: 31st August 2020
# TA: Simon (smbr@itu.dk)

import math

###############

# A function to calculate the BMI
def bmi (weight, height) :
	bmi = weight / height**2
	return bmi

# print (round(bmi(70,1.80), 2))

################

# A function, that takes three variables and prints out the sum and average

def calc (x,y,z) : 
	return "This is the Sum: ", x+y+z, "\n This is the mean: ", round((x+y+z)/3, 2)
 
################

# A program, that counts the digits of a sum.

def calc2 (x,y,z) : 
	intSum = x+y+z
	intLength = len(str(intSum))
 	
 	#intLength = int(math.log10(n))+1
	return intSum, intLength

# print(calc2(80,20,30))

################

# A function to calculate the area of a circle using the radius

# radius = eval(input("What is the radius of the circle? (cm): "))

def areaCircle (radius): 
	area = math.pi * radius ** 2
	return area

# print ("This is the area of the circle (cm^2): ", round(areaCircle(radius),2))

###############
# A function to measure distance in a grid 

# x1 = eval(input("Enter x1: "))
# y1 = eval(input("Enter y1: "))

# x2 = eval(input("Enter x2: "))
# y2 = eval(input("Enter y2: "))


def distance (x1,y1,x2,y2): 
	distance = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

	return distance 

# print("This is the distance between P1 and P2: ", round(distance(x1,y1,x2,y2), 2))


# A function to calculate the escape velocity

def escapeVelocity (mass, radius): 
	gravitationalPull = 6.67 * 10 * math.e ** -11


	escapeVelocity = math.sqrt ((2 * gravitationalPull * mass)/radius)

	return escapeVelocity 

#print ("This is the speed needed to escape the planet: ", escapeVelocity(100000000, 6378.1))




