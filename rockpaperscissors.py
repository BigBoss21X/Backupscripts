#make a rock paper scissors game
#import first

from random import randint
from time import sleep

#setup constants
options = ["R","P","S"]
INFO_WIN = "Sweet, you win!"
INFO_LOSE = "Bahh, you lose!"

#function to decide who wins

def decide_winner(user_choice,computer_choice):
    print str(user_choice)
    print "Computer Selecting..."
    sleep(.8)
    print str(computer_choice)
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print "It's a Tie, everyone loses."
	return
    elif user_choice_index == 0 and computer_choice_index == 2:
	print INFO_WIN
	return
    elif user_choice_index == 1 and computer_choice_index == 0:
	print INFO_WIN
	return
    elif user_choice_index == 2 and computer_choice_index == 1:
	print INFO_WIN
	return
    elif user_choice_index > 2:
	print "What are you doing???"
	return
    else:
	print INFO_LOSE
	return
#now that choices are made, we create a function to actually play

def play_RPS():
    print "It's Rock, Paper, Scissors, BABY"
    sleep(1)
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,len(options)-1)]
    decide_winner(user_choice,computer_choice)

play_RPS()
