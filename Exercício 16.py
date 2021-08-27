#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da 
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.

metros_quadrados = float(input("Quantos metros quadrados serão pintados? "))
litro = 3 # 1 Litro pinta 3 metros
latas = 18 #Litros
valor = 80 #Valor

tinta_necessaria = metros_quadrados/litro
latas_de_tinta = tinta_necessaria/latas
valor = latas_de_tinta*valor

if metros_quadrados <= 18:
    print('Para pintar {} m² é necessário menos de 18 Litros'.format(metros_quadrados))
    print('Trabalhamos com latas de 18 Litros apenas e custa R$ 80,00.')
else:
    print('Para pintar {} m² será necessário {:.0f} Litros, será preciso {:.1f} latas de 18 litros.'.format(metros_quadrados, tinta_necessaria,latas_de_tinta))
    print('O total seria R$ {0:.2f}'.format(valor))