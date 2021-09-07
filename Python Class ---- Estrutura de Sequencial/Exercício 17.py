usuario_metro_quadrado = float(input('Quantos metros quadrados? '))
metro_quadrado_por_1L_tinta = usuario_metro_quadrado/6 #M²
tinta_galaão = 3.6 #Litros
tm_lata = 18 #Litros
valor_lata = 80 #Reais
por_galao = 25 #Reais

if metro_quadrado_por_1L_tinta <= tinta_galaão:
    #QNTD_METROS + SUGESTÃO DE TINTA GALÃO
    print('Você pode levar o galão de tinta com {} litros.'.format(tinta_galaão))
    print('Custa R$ {}.'.format(por_galao))

else: 
    #QNTD_METROS + SUGESTÃO DE TINTA LATA
    print('Você pode levar a lata de tinta com {} litros.'.format(tm_lata))
    print('Custa R$ {}.'.format(valor_lata))