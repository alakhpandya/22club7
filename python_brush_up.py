# Modifying a tuple

# l1 = [23, 12, 0, -5, 16, 50]
# sorted(l1)
# l1.sort()
# print(l1)

# t1 = (23, 12, 0, -5, 16, 50)
# t2 = tuple(sorted(t1))
# print(t2)
# t1 = tuple(sorted(t1))


# Ordered & Unordered
"""
            Ordered     Mutable
list        Ordered     Mutable
tuple       Ordered     Immutable
set         Unordered   Mutable
frozenset   Unordered   Immutable

string: Ordered & Immutable collections of characters
dictionary: Unordered & Mutable collections of key : value pairs

Meaning of ordered:
Index nos to each element starting with 0
-ve index nos   - learn
accessing through +ve/-ve index nos
slicing is possible with +ve/-ve index
slicing with step
"""

# myList = [12, -10, 34, 50.5, "Surat", "Palanpur", "Surajgadh", -45.54, True, 85000]
# index:  0     1   2   3       4           5           6           7   8       9
# -ve ind:-10   9   8   7       6           5           4           3   2       1
# myString = "Today is Thursday but I don't know why I'm not feeling hungry at this time."
# index:    0123456789.................................................................
# -ve:      ..................................................................987654321

# print(myList[-3])
# print(sorted(myString))
# print(myString[5 : 25])
# myString[3 : -4]

# Write a program to reverse the given string.

# myString[15 : 5 : -1]

# lambda functions
# def sqrt(n):
#     return n ** 0.5
"""
sqrt = lambda n : n ** 0.5
avg = lambda a, b : (a + b)/2
printHello = lambda : "Hello"

# Write a function that takes a 3x3 matrix from user & returns to the main program.
# [[1,2,3], [4,5,6], [7,8,9]]

# def scan3x3Matrix():
#     return [[int(input()) for j in range(3)] for i in range(3)]

# scan3x3Matrix = lambda : [[int(input()) for j in range(3)] for i in range(3)]
# print(scan3x3Matrix())

lambda : [[int(input()) for j in range(3)] for i in range(3)]
"""

# Use the fact() function written below & the list 'numbers' and create another list 'factorials' which is having factorial of each memeber of 'numbers'
"""
def fact(n):
    t = 1
    for i in range(1, n+1):
        t = t * i
    return t

numbers = [8, 5, 3, 9, 10, 6, 4, 5]

factorials = map(fact, numbers)
# factorials = list(map(fact, numbers))

# print(factorials)

# for x in factorials:
#     print(x)
"""

# Do not change this:
"""
def average(temperature_data):
    return sum(temperature_data)/len(temperature_data)

def aboveAverage(x):
    return x > avg

temperatures = [-40, -30, -35, -30, -38, -10, -4, 0, -37, 2, -3]
avg = average(temperatures)
"""
# Use the function aboveAverage() and the list of temperatures to create another list of 'above_average_temperature_points' which consists of temperatures those are higher than the average temperature.

# Write your code from here:
"""
above_average_temperature_points = []
for i in temperatures:
    if aboveAverage(i):
        above_average_temperature_points.append(i)
"""
"""
above_average_temperature_points = filter(aboveAverage, temperatures)

print(above_average_temperature_points)

print(list(above_average_temperature_points))


# lambda functions as anonymous functions (in-line functions)
above_average_temperature_points = filter(lambda x : x > avg, temperatures)
"""

"""
Absolute value:
|5| = 5
|-5| = 5

Absolute funciton:
print(abs(-5))
print(abs(5))
"""

# Write a program that prints total transacted amount using the 'absoluteAddition()' function below:
'''
from functools import reduce

def absoluteAddition(a, b):
    return abs(a) + abs(b)

transactions = [1000, -500, -1200, 2500, -3000, 4000, 1500, -250, -450]
"""
sum = 0
for amount in transactions:
    sum = sum + abs(amount)
"""
"""
sum = 0
for amount in transactions:
    sum = absoluteAddition(sum, amount)
print(sum)
"""
sum = reduce(absoluteAddition, transactions)

sum = reduce(lambda a, b : abs(a) + abs(b), transactions)
'''
"""
5! = 5 x 4 x 3 x 2 x 1

5! = 5 x 4! = 120
4! = 4 x 3! = 24
3! = 3 x 2! = 6
2! = 2 x 1! = 2
1! = 1 x 0! = 1

0! = 1

Recursive Definition of factorial:
    Recursive Step:
    n! = n * (n-1)!
    Non-recursive Step:
    0! = 1

# recursiveFact(n-1)
def recursiveFact(n):
    if n == 0:
        return 1
    else:
        return n * recursiveFact(n-1)
    
print(recursiveFact(998))
"""
# Write a recursive function for finding nth term of an arithmetic progression whose 1st term is a and common difference is d. Ask a, d & n from user in the main program and call the recursive function 'recursiveAP()' to get the nth term.
"""
example of an AP with a = 3 & d = 4:
3, 7, 11, 15, 19, 23, 27

Recursive Step:
nth term = (n-1)th term + d
Non recursive Step:
1st term = a
"""
"""
def recursiveAP(a, d, n):
    if n == 1:
        return a
    else:
        return recursiveAP(a, d, n-1) + d

a = int(input("First Term: "))
d = int(input("Common Difference: "))
n = int(input("Term you want to find: "))
print(recursiveAP(a, d, n))
"""

# Write a recursive function for finding nth term of an geometric progression whose 1st term is a and common ratio is r. Ask a, r & n from user in the main program and call the recursive function 'recursiveGP()' to get the nth term.
"""
example of an AP with a = 3 & r = 4:
3, 12, 48, 192...

Recursive Step:
nth term = (n-1)th term * r
Non recursive Step:
1st term = a
"""

# Write a recursive function that returns nth term of fibonacci sequence. Write a main program that an integer 'n' from user & print all the terms of fibonacci sequece till 'n' (inclusive).
"""
def recurssiveFibo(n1):
    if n1==1 or n1==2:
        return 1
    else:
        return recurssiveFibo(n1-1) + recurssiveFibo(n1-2)
    
n1=int(input())
for i in range(1,n1+1):
    print(f"{i}. {recurssiveFibo(i)}")
"""
# Memoization
"""
# memory = {1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, ............, 35 : }
cache_memory = {}
def fib(n):
    if n in cache_memory.keys():
        return cache_memory[n]
    
    if n == 1:
        cache_memory[n] = 0
        return 0
    elif n == 2:
        cache_memory[n] = 1
        return 1
    else:
        t = fib(n-1) + fib(n-2)
        cache_memory[n] = t
        return t
    
nth=int(input("Enter the n terms:"))
for i in range(1,nth+1):
    print(f"{i}. {fib(i)}")
# print(cache_memory)
"""

# myDict = {1 : "Lamya", 2 : "Dharmangi", 3 : "Vedangi", 4 : "Nihar", 5 : "Khush"}

# myDict[3]
"""
from functools import lru_cache

# Decorators/Wrapper Functions

@lru_cache(maxsize=3)
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
nth=int(input("Enter the n terms:"))
for i in range(1,nth+1):
    print(f"{i}. {fib(i)}")
"""