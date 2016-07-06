#
#Practice Assignment 2-1 Solution
#Author: Kayla Harris
#Last Updated: July 2nd, 2016
#

#Receives input from user and converts to an integer.

num = int(raw_input("Please enter a whole number:\n"))

#If the remainder is 0 after being divided by 2, 
#the number is even.

if (num % 2) == 0:
	print "%d is even!" %(num)
	
#If the remainder is anything other than 0,
#the number is odd.

else:
	print "%d is odd!" %(num)