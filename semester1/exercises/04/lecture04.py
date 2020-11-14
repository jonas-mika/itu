bodil= "halløj"
#############################
# boolean expressions
############################
3 < 4

3 * 4 < 3 + 4

"hello" == "hello"

"hello" < "hello"

"Hello" < "hello"

#############################
# simple conditions
############################# 

def converter():
   celsius = float(input("What is the Celsius temperature?"))
   fahrenheit = 9/5 * celsius + 32
   print("The temperature is", fahrenheit, "degrees Fahrenheit.")
# Print warnings for extreme temps
   if fahrenheit > 90:
      print("It’s really hot out there. Be careful!")
   if fahrenheit < 30:   
      print("Brrrrr. Be sure to dress warmly!")
#converter()

#######################
########################
# import and __main__
########################

import math 
math.__name__ 

__name__

#run as main script
def main():
   print("hello from main")

if __name__ == "__main__": main()


########################
# two way decision
########################

def two_way_decision_demo():
   var1 = True
   if var1:
      print("Got a true expression value")
      print(var1)
   else:
      print("Got a false expression value")
      print(var1)

   print("Goodbye!")

######################
# multiway
######################
def multi_way_decision_demo():
   var = 100
   if var == 200:
      print("1 - Got a true expression value")
      print(var)
   elif var == 150:
      print("2 - Got a true expression value")
      print(var)
   elif var == 100:
      print("3 - Got a true expression value")
      print(var)
   else:
      print("4 - Got a false expression value")
      print(var)

   print("Good bye!")

######################
######################
# Exceptions
######################
#try to call with a list
def int_convert(var):
   try:
      return int(var)
   except ValueError as ex:
      print("The argument does not contain numbers\n")
   except:
   	print("something unexpected went wrong, sorry.")


######################
# lists, tuples, sets
######################
mylist = [5,1,9,7]
mylist[2]
mylist[2] = 0
mylist

#help(list.sort)

myString = "Hello world"
myString[2]
#myString[2] = 'z'

this_tuple = (4,3,7, "d")
this_tuple[-1]
len(this_tuple)

my_set = {'a', 'b', 'c'}
my_set.add("q")
my_set.update({1,2}) #set union
my_set.update({1,2,3})

######################
# factorial
######################
def fact(n):
   if n == 0:
      return 1
   else:
      return n * fact(n-1)
