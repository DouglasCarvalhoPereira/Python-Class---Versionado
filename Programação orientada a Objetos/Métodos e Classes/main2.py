#Classes conversando com classes
from classes import Escritor
from classes import Ceneta
from classes import Maquina_Escrever

escritor = Escritor('Douglas')
caneta = Ceneta('Bic')
maquina = Maquina_Escrever('Samsung')

#O valor NONE atribuído a FERRAMENTA na classe escritor recebeu "caneta.escrever()"
escritor.ferramenta = caneta.escrever('','')
escritor.ferramenta = maquina.escrever('','')

#Ou o valor NONE atribuído a Ferramenta na classe Escritor recebe o objeto Maquina, tendo assim acesso ao método escrever.
escritor.ferramenta = maquina
escritor.ferramenta.escrever(escritor.nome, 'é o escritor que está usando a cenata...')

#Ou o valor NONE atribuído a Ferramenta na classe Escritor recebe o objeto Caneta, tendo assim acesso ao método escrever.
escritor.ferramenta = caneta
escritor.ferramenta.escrever(escritor.nome, 'é o escritor que está usando a maquina...')