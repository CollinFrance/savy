# Name:Collin and Jack
# Date:July 13 2017

# project05: functions and lists

# Part I

def divisors(num):
    counter = 0
    lst = []
    while counter != num:
        counter = counter + 1
        if num % counter == 0:
            lst.append(counter)
        #print "divisor"




    """Takes a number and returns all divisors of the number, ordered least to greatest"
    :param num: int
    :return: list (int)
    """

    # Fill in the function and change the return statment.
    return lst

def prime(num):
    x = divisors(num)
    if len(x) > 2:
        return False
    else:
        return True
    """
    Takes a number and returns True if the number is prime, otherwise False
    :param num: int
    :return: bool
    """

    # Fill in the function and change the return statement.
    return False

# Part II

def intersection(lst1, lst2):
    answer= []
    for item in lst1:
        if item in lst2 and item not in answer:
            answer.append(item)
    return answer


    """
    Takes two lists and returns a list of the elements in common between the lists
    :param lst1: list, any type
    :param lst2: list, any type
    :return: list, any type
    """

    # Fill in the function and change the return statement.
    return ["test"]



print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")