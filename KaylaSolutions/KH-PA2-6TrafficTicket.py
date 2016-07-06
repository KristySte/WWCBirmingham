#
#Practice Assignment 2-6 Solution
#Author: Kayla Harris
#Last Updated: July 2nd, 2016
#

#Import the argv function to accept parameters.
#Integers should be used for the speed limit and the
#speed the driver was going. Negative numbers will
#not be accepted for calculations.

from sys import argv

script, speedLimitIn, speedDriverIn = argv

#Convert numbers entered to integers

speedLimit = int(speedLimitIn)
speedDriver = int(speedDriverIn)

#Set base cost of ticket, calculate the difference in speeds, and
#initialize variables used in print statements.

baseCost = 30.00
speedDiff = speedDriver - speedLimit
ticketAmount = 0
extraAction = ""

#First check if the numbers are valid speeds.

if speedLimit < 0 or speedDriver < 0:
	print "One of the numbers entered were negative. That's not possible! Please re-enter numbers."

#If the difference in speeds is negative or zero, that means the driver was driving
#under or at the speed limit.

elif speedDiff <= 0:
	print "The driver was driving within the speed limit! No ticket issued. Why are you using me?"

#The rest of the conditions check how over the speed limit the
#driver was driving using certain intervals. The higher the speed 
#the driver was going is, the more severe the consequences.
#Print statements are formatted in a structured format that is easy
#to read, no matter what the output is.

elif speedDiff < 5:
	ticketAmount = baseCost
	extraAction = "Can dispute"
	print "Ticket amount:\t\t$%.2f\nExtra action(s):\t%s" %(ticketAmount, extraAction)
elif speedDiff >= 5 and speedDiff <= 10:
	ticketAmount = baseCost + (baseCost * 0.1)
	extraAction = "Can't dispute"
	print "Ticket amount:\t\t$%.2f\nExtra action(s):\t%s" %(ticketAmount, extraAction)
elif speedDiff >= 11 and speedDiff <= 20:
	ticketAmount = baseCost + (baseCost * 0.25)
	extraAction = "Can't dispute"
	print "Ticket amount:\t\t$%.2f\nExtra action(s):\t%s" %(ticketAmount, extraAction)
elif speedDiff >= 21 and speedDiff <= 30:
	ticketAmount = baseCost + (baseCost * 0.50)
	extraAction = "Driving school"
	print "Ticket amount:\t\t$%.2f\nExtra action(s):\t%s" %(ticketAmount, extraAction)
elif speedDiff >= 30:
	ticketAmount = baseCost + (baseCost * 0.75)
	extraAction = "Court date"
	print "Ticket amount:\t\t$%.2f\nExtra action(s):\t%s" %(ticketAmount, extraAction)