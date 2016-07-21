import random
import sys

moves=['rock', 'paper', 'scissors']
win_moves = ['rockscissors', 'paperrock','scissorspaper']

while True:
    print"Choose rock, paper, scissors. When you are done playing type quit"

    player1_move = raw_input("Player 1 move: ")
     
      

player2_move=random.choice(moves)

print "Player 2 move: ", player2_move

if player1_move == player2_move:
    print "Tie!"
elif player1_move + player2_move:
    print"Player 1 wins!"
else:
    print"Player 2 wins!"
