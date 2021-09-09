name = 'Testar a formatação de Strings'
value = 'Douglas'
value_2 = 'Carvalho'

print('Dessa forma conseguimos {}'.format(name.lower()))

def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format( grade=grade, name=name)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


print("{:>3} #Aqui eu digo para o resultado se alinhar 3 espaçoas a direita")
print("{:>6.2f} #Aqui eu digo para se alinhar 6 espaços para direita e manter 2 casa decimais após a virgula.")