nomes = ['Douglas', 'Lucas', 'Clayton', 'Diego','Cintia']
new = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]
print(new)