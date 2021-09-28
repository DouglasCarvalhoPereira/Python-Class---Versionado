import string
import wordcloud

#ABRI O ARQUIVOpip
ref_arquivo = open("txtNuvemPalavra.txt","r", encoding="utf-8")

#LI O ARQUIVO .TXT
words_in_list = ref_arquivo.read()

#PALAVRAS QUE DEVEM SER EXCLUIDAS
exclude = ["sem","do","da","você","ele","eles","como","ela","elas","nós",
"não","de","suas","para","que","a","o","um","uns","Não","há","é","as","os","mas","com"]

#RETIREI A PONTUAÇÃO
not_punctuation = ''.join([i for i in words_in_list if i not in string.punctuation]).split()

#EXCLUIR PALAVRAS REPETITIVAS E SEM DEFINIÇÃO
new_texto = ' '.join([word for word in not_punctuation if word not in exclude]).split()

cloud = {}

for word in new_texto:
    cont_word = new_texto.count(word)
    cloud[word] = cont_word

print(cloud)