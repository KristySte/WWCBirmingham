#
#Practice Assignment 2-3 Solution
#Author: Kayla Harris
#Last Updated: July 2nd, 2016
#

#Import the argv function to accept parameters.

from sys import argv

script, numIn1, numIn2, numIn3 = argv

#Convert the numbers entered into float values.
#If anything other than a number is entered,
#the program will fail here.

num1 = float(numIn1)
num2 = float(numIn2)
num3 = float(numIn3)

#Compare the first number to the second and third numbers.
#Use <= to include numbers that are equal to each other.

if (num1 <= num2 and num1 <= num3):
	print "%.0f is the lowest number!" %(num1)

#Compare the second number to the first and third numbers.

elif (num2 <= num1 and num2 <= num3):
	print "%.0f is the lowest number!" %(num2)

#Compare the third number to the first and second numbers.

elif (num3 <= num1 and num3 <= num2):
	print "%.0f is the lowest number!" %(num3)