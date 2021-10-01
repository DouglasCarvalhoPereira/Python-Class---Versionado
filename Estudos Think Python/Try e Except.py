#TENTATIVA E ERRO, SEMELHANTE A IF E ELSE

#3 TENTATIVAS DE LE OS ARQUIVOS

try:
    fin = open("words1.txt","r")
    print(fin.read())
except:
    print("Is not possible words1.txt.")
    try:
        fin = open("words2.txt","r")
        print(fin.read())
    except:
        print("Is not possible words2.txt.")
        try:
            fin = open("words.txt","r")
            print(fin.read())
        except:
            print("Is not possible words.txt.")