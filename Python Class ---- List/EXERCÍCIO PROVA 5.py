import math

x = 0
y = 2

def comparate(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

print(comparate(x, y))

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is ', dx)
    print('dy is ', dy)
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)

    return result

distance(2, 5, 8, 9)


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

print(is_divisible(12, 12))

#RECURSIVA, EXECUTA ATÉ CHEGAR A ZERO
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = recurse*n
        return result

print(factorial(0))



    


