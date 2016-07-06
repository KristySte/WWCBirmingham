#
#Practice Assignment 2-5 Solution
#Author: Kayla Harris
#Last Updated: July 2nd, 2016
#

#Import the argv function to accept parameters.
#The tax rate and tip rate should be entered
#in decimal format, not percentage format.

from sys import argv

script, mealCostIn, taxRateIn, tipRateIn = argv

#Convert the numbers entered into float values.
#If anything other than a number is entered,
#the program will fail here.

mealCost = float(mealCostIn)
taxRate = float(taxRateIn)
tipRate = float(tipRateIn)

#Calculate the tax amount, tip amount, and the meal total.

taxAmount = mealCost * taxRate
tipAmount = mealCost * tipRate
mealTotal = mealCost + taxAmount + tipAmount

#Multiply the tax rate and the tip rate so that the
#rates can be displayed as percentages.

dispTaxRate = taxRate * 100
dispTipRate = tipRate * 100

#Print the percentages and amounts in a structured format like a sales receipt.

print "Meal cost:\t$%.2f\nTax rate:\t%.2f%%\nTip rate:\t%.2f%%" %(mealCost, dispTaxRate, dispTipRate)
print "--------------------"
print "Tax amount:\t$%.2f\nTip amount:\t$%.2f\nMeal total:\t$%.2f" %(taxAmount, tipAmount, mealTotal)