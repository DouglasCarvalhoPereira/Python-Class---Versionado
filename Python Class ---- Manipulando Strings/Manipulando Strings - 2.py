#INDEXAÇÃO DE STRINGS E ALTERAÇÃO

frase = 'My name is Douglas ans, im very nice for is here! But, im do not continue'
#.index Retorna apenas a primeira posição encontrada
print(frase.index("Douglas")) #Identifica a posição de Douglas/String na frase
print(frase.index("here")) #Identifica a posição de Here/String na frase
print(frase.index("not")) #Identifica a posição de Not/String na frase

print("Douglas" in frase) #NESSE CASO "in" verifica se "Douglas" está presente na variavel 'frase'.


def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email
