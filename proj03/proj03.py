# Name: Collin France Richard Young
# Date:7-12-17


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
#counter
#loops
#if else elif
#loop control variable
#number generator
#math operations < > / + = -
import random
cow = 0
X = random.randint(1,9)
loop_control = True
print "The number is between 1 and 9. "
while loop_control == True and cow < 3:
    guess = int(raw_input("guess the number: "))
    cow = cow + 1
    if guess < X:
        print "Guess is to low."

    elif guess > X:
        print "Guess is to high."

    else:
        print "Congrats, you guessed the number!"
        loop_control =False
    if cow==3:
        print"you have run out of chances"

print "it took you ",(cow),"guesses."