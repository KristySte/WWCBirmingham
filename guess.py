import random
print "Guess a number betweem 0 and 1000"
number = random.randrange(1000)

while True:
    guess = int(raw_input("Your Guess: "))
    print number
    if guess > number:
        print"Too high"
    elif guess < number:
        print"Too low"
    else:
        print number
        break
        
        
                      

