#DICIONÁRIO MÉTODOS BPASICOS
dicionarios = {'Douglas':10, 'Clayton': 11} #Definição dicionári
dicionarios2 = {'Diego': 12, 'Lucas': 13}

len(dicionarios)

for dicionario in dicionarios.keys():
    print('Chave: ', dicionario)

for dicionario in dicionarios.values():
    print('Valor: ', dicionario)

#MÉTODOS

print('Valor da chave Douglas: ', dicionarios.get('Douglas')) #Retorna o valor associado a chave
print('Todas as chaves: ', dicionarios.keys()) #Todas as chaves do dicionario
print('Todas os values: ', dicionarios.values()) #Todos os valores do dicionarios
print('Atualiza os valores do dicionario atual: ', dicionarios.update(dicionarios2)) #Atualiza os valores do cionário atual
print('Remove todos os itens do dicionario: ', dicionarios.clear()) #Exclui todos os itens do dicionario 
