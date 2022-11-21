#Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um:
#3- se positivo, inserir na pilha P;
#- se negativo, inserir na pilha N;
#- se zero, retirar um elemento de cada pilha.



def TPilha2(N:list,P:list,vetor:list):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(N) > 0:
                print(f"Foi retirado o número : {N[len(N)-1]}")
                N.pop()
            if len(P) > 0:
                print(f"Foi retirado o número : {P[len(P) - 1]}")
                P.pop()


        elif vetor[i] > 0:
            P.append(vetor[i])

        else:
            N.append(vetor[i])

    print(f"Os numero negativos foram: {N}, e os números positivos foram {P}")

parametros = TPilha2([],[],[7,-3,3,8,-4, -2,2,9, -9, 0, -5])