#    Utilizando uma pilha resolver o exercício a seguir:
#    Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.

import numpy as np

class Pilha:

    def __init__(self, capacidade: int) -> object:
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.pilha_cheia():
            print("pilha cheia")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha está vazia")

        else:
            self.topo -= 1

    def ver__topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def ver_itens(self):
        if self.pilha_vazia():
            print("Pilha está vazia")
        else:
            print("Os valores da pilha são: " , self.valores)

    def ver_invertido(self):
        if self.pilha_vazia():
            print("Pilha está vazia")
        else:
            print("A pilha com os valores invertidos é :" ,self.valores[::-1])




pilha = Pilha(5)


pilha.empilhar(1)
pilha.empilhar(4)
pilha.empilhar(8)
pilha.empilhar(5)
pilha.empilhar(9)

pilha.ver_itens()

pilha.ver_invertido()