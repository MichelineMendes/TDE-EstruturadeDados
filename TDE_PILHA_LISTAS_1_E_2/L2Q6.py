#Construa uma lista Sequencial utilizando a linguagem Python com as seguintes operações: a.
#Verificar se um número pertence lista; b. Inserir um novo elemento na lista; c.
#Remover um elemento da lista; d.
#Imprimir os valores da lista;

import numpy as np


class ListaSequencial:
    def __init__( self, capacidade ):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.itens = np.empty(self.capacidade, dtype=int)

    def pesquisar( self, valor ):
        for i in range(self.ultima_posicao + 1):
            if valor == self.itens[i]:
                return i
        return -1

    def verLista( self ):
        print(self.itens)

    def inserir( self, valor ):
        if self.ultima_posicao == self.capacidade - 1:
            print('A lista está cheia')
        else:
            self.ultima_posicao += 1
            self.itens[self.ultima_posicao] = valor

    def remover( self, valor ):
        for i in range(self.ultima_posicao + 1):
            if valor == self.itens[i]:
                posicao = i
                if posicao == -1:
                    return -1
                else:
                    for i in range(posicao, self.ultima_posicao):
                        self.itens[i] = self.itens[i + 1]

                    self.ultima_posicao -= 1
                    print("Item removido com sucesso!")

    def imprimir( self ):
        if self.ultima_posicao == -1:
            print('A lista está vazia')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"A posição {i} recebeu o item {self.itens[i]}")


