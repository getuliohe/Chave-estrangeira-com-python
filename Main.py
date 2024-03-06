from Classes.Cidade import Cidade
from Classes.Pessoa import Pessoa


novaCidade = Cidade()
quantidadeDePessoas = 2
listaDePessoas = []
contador = 1

while contador <= quantidadeDePessoas:
    print(f"Pessoa {contador}: \n")
    listaDePessoas.append(Pessoa(contador,str(input("Digite o nome: ")),int(input("Digite a quantidade de emails: ")),int(input("Digite a quantidade de telefones: ")),novaCidade))
    contador += 1

print("Id Pessoa | nome | emails | telefones | Cidade | Uf")
for pessoa in listaDePessoas:
    pessoa.printPessoa(novaCidade)

