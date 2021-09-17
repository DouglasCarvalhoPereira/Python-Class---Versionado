def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x += 1
    return x * y

def c(x, y ,z):
    total = x + y + z
    square = b(total**2)
    return square


x = 0
y = x + 0
print(c(x, y+1, x+y))

