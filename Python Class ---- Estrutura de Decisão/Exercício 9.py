from typing import Reversible

numeros = input('Digite 10 número: ').split()
numeros.sort(reverse=True)

for i in numeros:
    print(i)