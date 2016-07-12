from sys import argv

#file input
script, filename = argv

#reads in file input
print "we're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#Ask for user response
raw_input ("?")

#opens file to write in
print "Opening the file..."
target = open(filename, 'w')

#shortens the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#Ask for user input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to wrtie these to the file."

#writes in the user input into file 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#Closes the file
print "And finally, we close it."
target.close()
