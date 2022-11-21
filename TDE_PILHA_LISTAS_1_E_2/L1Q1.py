from __future__ import annotations
import numpy as np
#Escrever uma função que receba como parâmetro uma pilha.
#A função deve retornar o maior elemento da pilha. A passagem deve ser por valor ou referência?

#procura-se por valor


class Pilha:

    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def pilhaCheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilhaVazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def adicionar(self, valor):
        if self.pilhaCheia():
            print("Rua cheia")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def ver_itens(self):
        if self.pilhaVazia():
            print("Pilha está vazia")
        else:
            print("Os valores da pilha são: " , self.valores)

    def maiorValor(self):
        maior = 0
        for i in range(len(self.valores)):
            for j in range (1, len(self.valores)):
                if self.valores[j] > self.valores[i]:
                    maior = self.valores[j]
                    break
                print(maior)

