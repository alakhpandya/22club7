# Modifying a tuple

# l1 = [23, 12, 0, -5, 16, 50]
# sorted(l1)
# l1.sort()
# print(l1)

t1 = (23, 12, 0, -5, 16, 50)
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

# remaining topics: reduce, functools, call back functions, lrucache