import random
import sys
#win-lose table

#     r  s  p
#    __________    
# r| X  l   w
# s| w  X   l 
# p| l  w   X

#player 2 moves
moves=['rock', 'paper', 'scissors']

#moves in order for player 1 to win
win_moves = ['rockscissors', 'paperrock','scissorspaper']

#creates a loop for game
while True:
    print"Choose rock, paper, scissors. When you are done playing type quit"
#Asks for player input
    player1_move = raw_input("Player 1 move: ")
     
      
#randomly chooses a moves from the list 'moves'
player2_move=random.choice(moves)

#prints player 2's moves
print "Player 2 move: ", player2_move

#If there is a tie
if player1_move == player2_move:
    print "Tie!"
#if player one combination works    
elif player1_move + player2_move:
    print"Player 1 wins!"
else:
#if neither tie not player 1's combination comes up.
    print"Player 2 wins!"
