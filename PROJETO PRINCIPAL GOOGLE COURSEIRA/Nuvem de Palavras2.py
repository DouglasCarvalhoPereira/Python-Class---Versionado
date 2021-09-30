import string
import wordcloud

#ABRI O ARQUIVO
ref_arquivo = open("txtNuvemPalavra.txt","r", encoding="utf-8")

#LI O ARQUIVO .TXT
words_in_list = ref_arquivo.read().lower()

#PALAVRAS QUE DEVEM SER EXCLUIDAS
exclude = ["em","uma","sem","sua","seu","mais","se","","do","da","você","ele","eles","como","ela","elas","nós","nos"
"não","de","suas","para","que","a","o","um","uns","não","há","e","é","as","os","mas","com","seus","pelo","pois","0",
"1","2","3","4","5","6","7","8","9","10","toda","sobre","no","na","isso","ou","ao","são","por","mesmo",]


#RETIREI A PONTUAÇÃO
not_punctuation = ''.join([i for i in words_in_list if i not in string.punctuation]).split()

#EXCLUIR PALAVRAS REPETITIVAS E SEM DEFINIÇÃO
new_texto = ' '.join([word.title() for word in not_punctuation if word not in exclude]).split()

frequencies = {}

for word in new_texto:
    cont_word = new_texto.count(word)
    frequencies[word] = cont_word

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")


