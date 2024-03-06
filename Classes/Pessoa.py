from Classes.Cidade import Cidade

class Pessoa:

    def __init__(self,idPessoa,nome,quantosEmail,quantosTelefones,cidade : Cidade):
        self.idPessoa = idPessoa
        self.nome = nome
        self.email = []
        self.telefone = []
        contador = 0
        while contador < quantosEmail:
            self.email.append(str(input(f"Digite seu {contador+1}º email: ")))
            contador += 1
        contador = 0
        while contador < quantosTelefones:
            self.telefone.append(str(input(f"Digite seu {contador+1}º telefone: ")))
            contador += 1
        
        self.idCidade = cidade.adicionarCidade(str(input("Digite o nome da sua cidade: ")),str(input("Digite o seu UF: ")))

    def printPessoa(self,cidade : Cidade):
        print(f"{self.idPessoa} | {self.nome} | {self.email} | {self.telefone} | {self.idCidade} | {cidade.dicionarioCidade[self.idCidade][0]} | {cidade.dicionarioCidade[self.idCidade][1]}")