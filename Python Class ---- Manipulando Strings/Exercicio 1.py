leitor_string = str(input('Digite a primeira string: '))
leitor_string_2 = str(input('Digite a segunda string: '))

if len(leitor_string) == len(leitor_string_2):
    print('As Strings possuem o mesmo comprimento.')
    
else:
    print('O tamanho das satrings são diferentes. ')

if leitor_string == leitor_string_2:
    print('E possuem o mesmo conteúdo')
else:
    print('Strings com conteúdos diferentes.')

print('A primeira string enviada é', leitor_string, 'e tem', len(leitor_string),'de comprimento!')
print('A segunda string enviada é', leitor_string_2, 'e tem', len(leitor_string_2),'de comprimento!')



