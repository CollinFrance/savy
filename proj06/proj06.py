# Name:Collin and Jack
# Date:July 13 2017


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
#x = user input
wordlist = load_words()

# your code begins here!
word = choose_word(wordlist)
lst1 = []
for letter in word:
    lst1.append(letter)
print lst1
lst2 = []
for letter in word:
    lst2.append("_")
print lst2

counter = 0
while counter < 12:
    x = raw_input("Enter a letter, for the hangmans life is on the line. To speed up the execution type zero :")
    counter = counter +1
    if counter == 12:
        print "Game over. The hangmans blood is on your hands."
    if x == '0':
        print "Game over. The hangmans blood is on your hands."
        counter = 12
if lst1 == lst2:
    print "You win"
counter = 0



