class Cidade():
    dicionarioCidade = dict()
    contador = 0

    def adicionarCidade(self,cidade,uf):
        contador = 0
        while contador < self.contador:
            contador = contador + 1
            if cidade == self.dicionarioCidade[contador][0]:
                return contador
        self.contador = self.contador +1
        self.dicionarioCidade [self.contador]= [cidade,uf]
        return self.contador