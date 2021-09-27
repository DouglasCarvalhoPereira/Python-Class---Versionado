import string

ref_arquivo = open("txtNuvemPalavra.txt","r", encoding="utf-8")
words_in_list = ref_arquivo.read().split( )
pontuacao = string.punctuation

new_txt = [position for position in words_in_list for letter in position if letter in pontuacao]

exclude = ["do","da","você","ele","eles","como","ela","elas","nós","não","de","suas","para","que","a","o","um"
,"uns",""]

print(new_txt)
#for position in words_in_list:
#    for letter in position:
#        if letter.isalpha() != False:
#            del letter
#        
#        print(words_in_list)