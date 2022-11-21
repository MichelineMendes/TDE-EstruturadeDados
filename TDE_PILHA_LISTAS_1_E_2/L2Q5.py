from __future__ import annotations
import numpy as np


# Escreva um programa em Python que simule o controle de uma pista de decolagem de aviões em um aeroporto.
# Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:
# Listar o número de aviões aguardando na fila de decolagem;
# Autorizar a decolagem do primeiro avião da fila;
# Adicionar um avião à fila de espera;
# Listar todos os aviões na fila de espera;
# Listar as características do primeiro avião da fila.


class Pista:

    def __init__( self, capacidade: object ) -> object:
        self.capacidade = capacidade
        self.inicio = 0
        self.ultimo = -1
        self.numero_avioes = 0
        self.aeronave = np.empty(self.capacidade, object)

    def quantidade(self):
        print( self.numero_avioes)

    def adicionar( self, aviao ):
        if self.numero_avioes == self.capacidade:
            print("Não é possível adicionar")
            return
        else:
            self.ultimo += 1
            self.aeronave[self.ultimo] = aviao
        self.numero_avioes += 1

    def decolar( self ):
        if self.numero_avioes == 0:
            print('A fila já está vazia')
            return
        temp = self.aeronave[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.numero_avioes -= 1
            print(f"O avião que decolou foi : {temp} ")

    def todosDaFila( self ):
            print(self.aeronave)

    def primeiroAviao( self ):
        if self.numero_avioes > 0:
            print(f"O primeiro avião aguardando decolagem na pista é : {self.aeronave[self.inicio]}")
        if self.numero_avioes == 0:
            print("pista vazia")


if __name__ == '__main__':
    pista = Pista(4)
    pista.adicionar('Boeing')
    pista.adicionar('Monomotor')
    pista.adicionar('AirBus')
    pista.adicionar('Caça')

    pista.quantidade()

    pista.todosDaFila()
    pista.primeiroAviao()
    pista.decolar()
    pista.primeiroAviao()