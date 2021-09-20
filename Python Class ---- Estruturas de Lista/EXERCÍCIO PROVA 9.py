fruti =['Banana','Abacaxi']
letter = []
index = 0
while index < len(fruti):
    letter.append(fruti[index])
    index += 1

print(' '.join((letter)), 'delicia')


for let in letter[0][-1]:
    print(let, end='\n')

iniciais = '123456'
final = 'akg'
for letra in iniciais:
    print(letra + fruti[1][::-1])