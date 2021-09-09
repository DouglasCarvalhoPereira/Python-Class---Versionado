salario_atual = float(input('Digite seu salário para saber o valor do seu aumento: '))

if salario_atual <= 280:
    reajuste = salario_atual+ (salario_atual/100)*20
    print('O salário de {salario_atual} + 20% é = {reajuste}' .format(salario_atual=salario_atual, reajuste=reajuste))

elif salario_atual > 280 and salario_atual < 700:
    reajuste = salario_atual+ (salario_atual/100)*15
    print('O salário de {salario_atual} + 15% é = {reajuste}' .format(salario_atual=salario_atual, reajuste=reajuste))

elif salario_atual > 700 and salario_atual < 1500:
    reajuste = salario_atual + (salario_atual/100)*10
    print('O salário de {salario_atual} + 10% é = {reajuste}' .format(salario_atual=salario_atual, reajuste=reajuste))

else:
    
    reajuste = salario_atual + (salario_atual/100)*5
    print('O salário de {salario_atual} + 5% é = {reajuste}' .format(salario_atual=salario_atual, reajuste=reajuste))
