#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

while True:
    paisA = float(input("Qual a polulação atual do país A? "))
    paisB = float(input("Qual a polulação atual do país B? "))

    crescimento_A_porcent = float(input("Quanto por cento cresce a população de A anualmente? "))
    crescimento_B_porcent = float(input("Quanto por cento cresce a população de B anualmente? "))
    ano = 0

    while paisA < paisB:
    
        paisA += paisA/100*crescimento_A_porcent
        paisB += paisB/100*crescimento_B_porcent
        ano += 1

    print("Levaria {} Anos para A se igualar ou ultrapassar B." .format(ano))