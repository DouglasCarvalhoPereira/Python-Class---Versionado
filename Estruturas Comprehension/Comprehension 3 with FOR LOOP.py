#FOR PARA LINHAS COLUNAS
for x in range(10):
    for y in range(5):
        print(x,y)


#OU UTILIZAR DA MESMA MANEIRA
linhas_e_colunas = [(x,y) if y%2 == 0 else 'Você era impar' for x in range(1, 11) for y in range(1,6) if x != 2 if y != 2]
print((linhas_e_colunas))