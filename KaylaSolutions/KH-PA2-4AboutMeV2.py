#
#Practice Assignment 2-4 Solution
#Author: Kayla Harris
#Last Updated: July 2nd, 2016
#

#Import the argv function to accept parameters.

from sys import argv

script, my_name, my_age, my_cur_city = argv

#After printing first statement, prompt user by asking if they were
#born in the city they currently live in.

print "My name is", my_name + ". I am", my_age, "years old and live in", my_cur_city + "."
born_here = raw_input("Were you born here?\n")

#If the user answer 'n' or 'N', prompt user by asking where they were born.
#That information is stored in `my_birth_city` and printed in a new statement.

if born_here.lower() == 'n':
	my_birth_city = raw_input("Where were you born?\n")
	print "My name is", my_name + ". I am", my_age, "years old and live in", my_cur_city + ". But I was born in", my_birth_city + "."

#If the user answers with anything else other than 'n' or 'N', they were
#born in the city they are currently living in. Another statement is printed
#to clarify that the user was born in the city they are currently living in.

else:
	print "My name is", my_name + ". I am", my_age, "years old and I was born and live in", my_cur_city + "."