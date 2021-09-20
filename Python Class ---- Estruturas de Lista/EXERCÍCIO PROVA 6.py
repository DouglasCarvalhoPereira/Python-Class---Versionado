def factorial(n):
    if not isinstance(n, int):
        print("Fatorial é definido apenas para inteiros!")
        return None

    elif n < 0:
        print("Factorial não é definido para números negativos.")
        return None
    
    elif n == 0:
        return 1

    else:
        return n * factorial(n-1)

print(factorial(5.9))


def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'Factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recursive = factorial(n-1)
        result = n * recursive
        print(space, 'returning', result)
        return result

print(factorial(1))