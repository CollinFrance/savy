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
#lst1 = word list, lst2 = _, lst3 = letters guessed in alphabet
# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
#x = user input
wordlist = load_words()
print "Lets play some hangman!!!"
# your code begins here!
word = choose_word(wordlist)
lst1 = []
for letter in word:
    lst1.append(letter)

lst2 = []
for letter in word:
    lst2.append("_")
print lst2

lst3 = []

counter = 0
while counter < 14:
    x = raw_input("Enter a letter, for the hangman's life is on the line. To speed up the execution type zero :")
    lst3.append(x)
    print lst3, "Letters guessed"
    counter = counter + 1
    print (14 - counter), "guesses left."
    if x in lst1:
        print "Correct!"
    else:
        print "Terrible!"
    if x in lst1:
        counter2 = 0
        while counter2 < len(word):
            if x == lst1[counter2]:
                lst2[counter2] = x
            counter2 = counter2 + 1
        print lst2
    if counter == 14:
        print "Game over. The hangman's blood is on your hands. Also the word was",(word)
    elif x == '0':
        print "Game over. The hangman's blood is on your hands. Also, the word was",(word)
        counter = 14
    elif lst1 == lst2:
        print "You win! The hangman is forever in your debt."
        counter = 14








#if letter is not in the list, what happens?
#add letters to list if they are correct
#keep track of letters that have been guessed