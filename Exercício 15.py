#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre 
# o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para 
# o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valor_por_hora = float(input("Valor por hora? "))
horas_por_mês = float(input("Horas por mês? "))
salario_mensal = valor_por_hora*horas_por_mês
ir = (salario_mensal*11)/100
inss = (salario_mensal*8)/100
sindicato = (salario_mensal*5)/100
descontos = ir + inss + sindicato
liquido = salario_mensal - descontos

print("Seu salário BRUTO esse mês é R$ {:.2f}." .format(salario_mensal))
print("=========")
print("Descontos")
print("=========")
print("Ir = R$ {:.2f}" .format(ir))
print("inss = R$ {:.2f}" .format(inss))
print("sindicato = R$ {:.2f}" .format(sindicato))
print("=========")
print("Liquído")
print("=========")
print("Salário a receber = R$ {:.2f}" .format(liquido))