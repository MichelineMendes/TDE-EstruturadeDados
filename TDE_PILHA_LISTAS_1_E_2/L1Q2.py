##2)	Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais.
# Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

import numpy as np


class Pilha:
    def __init__(self, capacidade: int):
        self._capacidade = capacidade
        self._topo = -1
        self._valores = np.empty(self._capacidade, dtype=int)

    def __pilha_cheia(self):
        if self._topo == self._capacidade - 1:
            return True
        else:
            return False

    def _pilha_vazia(self):
        if self._topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("pilha cheia")
        else:
            self._topo += 1
            self._valores[self._topo] = valor

    def desempilhar(self):
        if self._pilha_vazia():
            print("Pilha está vazia")
        else:
            self._topo -= 1

    def ver_index(self, index):
        return self._valores[index]

    def ver_topo(self):
        if self._topo != -1:
            return self._valores[self._topo]
        else:
            return -1

    def ver_quantidade_items(self):
        return self._topo


def pilhas_sao_iguais(pilha1: Pilha, pilha2: Pilha) -> bool:
    if pilha1.ver_quantidade_items() != pilha2.ver_quantidade_items():
        return False

    i = 0
    total_pilha1 = pilha1.ver_quantidade_items()
    while i < total_pilha1:
        if pilha1.ver_index(i) != pilha2.ver_index(i):
            return False
        i += 1
    return True


if __name__ == '__main__':

    p1 = Pilha(3)
    p1.empilhar(5)
    p1.empilhar(2)
    p1.empilhar(3)

    p2 = Pilha(3)
    p2.empilhar(5)
    p2.empilhar(2)
    p2.empilhar(3)

    if pilhas_sao_iguais(p1, p2):
        print("Essas listas são iguais!")
    else:
        print("Essas listas não são iguais!")