#2-	Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação problema:
# Armazene as placas dos carros de luxos (apenas os números) que estão estacionados em um placa sem saída.
# Dado uma placa verifique se o carro está estacionado na placa.
# Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.


import numpy as np

class Pilha:

    def __init__( self, capacidade: int ) -> object:
        self.capacidade = capacidade
        self.topo = -1
        self.rua = np.empty(self.capacidade, dtype=int)

    def rua_cheia( self ):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def rua_vazia( self ):
        if self.topo == -1:
            return True
        else:
            return False

    def estacionar( self, valor ):
        if self.rua_cheia():
            print("Rua cheia")
        else:
            self.topo += 1
            self.rua[self.topo] = valor

    def remover( self ):
        if self.rua_vazia():
            print("Rua está vazia")
        else:
            self.topo -= 1

    def ver_rua( self ):
        return self.rua

    def ver_topo( self ):
        if self.topo != -1:
            return self.rua[self.topo]
        else:
            return -1

    def retirar( self, valor ):
        while valor != self.rua[self.topo]:
            print("sai o carro", self.rua[self.topo])
            self.topo -= 1
        else:
            print("pode tirar o carro agor")

    def buscar( self, valor ):
        if valor in self.rua:
            print("Carro está nessa rua")
        else:
            print("carro não está aqui")

