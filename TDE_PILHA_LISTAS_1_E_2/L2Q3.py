# 3-	Construa um programa em Python de acordo com situação problema descrita:
# Um grupo de soldados está cercado e não há esperança de vitória,
# porém existe somente um cavalo disponível para escapar e buscar por reforços.
# Para determinar qual soldado deve escapar para encontrar ajuda,
# eles formam um círculo (Fila Circular) e sorteiam um número de um chapéu.
# Começando por um soldado sorteado aleatoriamente, uma contagem é realizada até o número sorteado.
# Quando a contagem terminar, o soldado em que a contagem parou é removido do círculo,
# um novo número é sorteado e a contagem recomeça no soldado seguinte ao que foi eliminado.
# A cada rodada, portanto, o círculo diminui em um, até que somente um soldado reste e seja escolhido para a tarefa.

import numpy as np


class FilaCircular:
    def __init__( self, capacidade ):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def escolher( chapeu ):
        soldado = [i for i in range(1, chapeu + 1)]
        i = 0
        c = 1
        while len(soldado) > 1:
            if i == len(soldado) - 1:
                print(f'Rodada {c} Sobraram:  {soldado} Eliminado:   {soldado[0]}')
                soldado.pop(0)
                i = 0
                c += 1
            elif i == len(soldado) - 2:
                print(f'Rodada {c} Sobraram:  {soldado} Eliminado:   {soldado[i + 1]}')
                soldado.pop(i + 1)
                i = 0
                c += 1
            else:
                print(f'Rodada {c} Sobraram:  {soldado} Eliminado:   {soldado[i + 1]}')
                soldado.pop(i + 1)
                i += 1
                c += 1
        print(f'\nSoldado escolhido foi o que tem o chapéu : {soldado[i]} ')

    escolher(10)