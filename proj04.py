# Name:Collin and Jack
# Date:july 12 2017

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
str = raw_input("Enter a list of words and this program will tell you if that word is a palindrome. ")
lst1 = []
lst2 = []
for letter in str:
    lst1.append(letter)
    lst2.append(letter)
lst2.reverse()
if lst1 == lst2:

    print "yes"
else:
     print "No"





