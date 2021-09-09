medir = 0
for i in range(1,6):
    numero = float(input('Digite o {}° número: '.format(i)))
    if numero > medir:
        medir = numero #MEDIR SE MANTÉ COM O VALOR DO LOOP ANTERIOR

print('O maior é o {:.0f}.' .format(medir))