#LENDO PALAVRAS DENTRO DE UM ARQUIVO DE TEXTO
#UTILIZANDO UM LIMITE PARA LEITURA
#IMPRIME PALAVRAS COM MAIS DE 20 CARACTERES

fin = open('words.txt')
fin.readline().strip()
letter_proib = ['wyz']

for letter in fin:
    new_word = [letra for letra in letter_proib if letra in letter]
    print(f'Palavra {letter} que contém  ({new_word})')
