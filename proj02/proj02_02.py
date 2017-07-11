# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
loop_control = 0
Number=raw_input("How many numbers of the code you would like to see.")
x=1
y=1
while loop_control <int(Number):
    loop_control = loop_control + 1
    print y
    z = y + x
    x = y
    y = z
loop_control = False











