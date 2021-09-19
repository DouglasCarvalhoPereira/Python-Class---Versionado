#COMPOSIÇÃO

class Repository:
    def __init__(self):
        self.packages = {} # Recebe os pacotes # Totat variável mutável deve ir dentro do método construtor
    def add_package(self, package):
        self.packages[package.name] = package  #Dicionário recebe pacotes
    def package_size(sefl):
        reusult = 0 #Recebe e soma o tamanho dos arquivos totais
        for package in self.package.values():
            result += package.size
        return result
 