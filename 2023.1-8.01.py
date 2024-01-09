'''
--> Criar matriz 2 X 3
--> import random
--> Somar as matriz (A e B)
--> Gerar a matriz C (através da soma)
--> Exibir matrizes no formato de matriz.
'''

import random

#Ordem da matriz
nlin = 2
ncol = 3

#Criação da matriz A
matrizA = []
for i in range(nlin):
    matrizA.append([None] * ncol)

#Criação da matriz B
matrizB = []
for i in range(nlin):
    matrizB.append([None] * ncol)

#Alimentando a matriz A
for i in range(nlin):
    for j in range(ncol):
        matrizA[i][j] = random.randint(1,50)

#Alimentando a matriz B
for i in range(nlin):
    for j in range(ncol):
        matrizB[i][j] = random.randint(1,50)

# Criação matriz C
matrizC = []

#Soma da matriz A e B
soma = 0
for i in range(nlin):
    for j in range(ncol):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

print("A:", matrizA)
print("B:", matrizB)
print("C:", matrizC)

for i in range(2):
    for j in range(3):
        print(matrizC[i][j], end=' ')
    print()