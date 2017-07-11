# Name:COLLIN FRANCE
# Date:JULY 11 17

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers iS:2
# True/False loop: end ewhen usr type in a 0
# loop control variable=True
# n1=raw_input ("enter a number")
# sum=0
# while loop control variable is True:
#     if user types in 0
#     loop control is False
#     else raw_input ("enter a number")
#     sum=sum +user input
loop_control = True
collin=0
while loop_control == True:
    Number=raw_input("any number to a start equation. Enter a zero to show you are finished")
    if (Number) == "0":
        loop_control = False
    collin = int(Number) + collin
print (collin),'is the sum'


