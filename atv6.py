matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz:")
for linha in matriz:
    print(linha)

print("\nSoma de cada linha:")
for i in range(3):
    soma_linha = 0
    for j in range(3):
        soma_linha += matriz[i][j]
    print(f"Linha {i}: {soma_linha}")

print("\nSoma de cada coluna:")
for j in range(3):
    soma_coluna = 0
    for i in range(3):
        soma_coluna += matriz[i][j]
    print(f"Coluna {j}: {soma_coluna}")

print("\nDiagonal principal:")
diagonal = []
for i in range(3):
    diagonal.append(matriz[i][i])
print(diagonal)

elementos = []
for linha in matriz:
    for valor in linha:
        elementos.append(valor)

print(f"\nElementos da matriz em lista única: {elementos}")

n = len(elementos)
for i in range(n):
    for j in range(n - i - 1):
        if elementos[j] > elementos[j + 1]:
            elementos[j], elementos[j + 1] = elementos[j + 1], elementos[j]

print(f"Elementos ordenados: {elementos}")

matriz_ordenada = []
indice = 0
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(elementos[indice])
        indice += 1
    matriz_ordenada.append(linha)

print("\nMatriz reorganizada em ordem:")
for linha in matriz_ordenada:
    print(linha)

print("\nOperações bit a bit sobre os elementos ordenados:")
for num in elementos:
    if num & 1 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    dobro = num << 1        
    metade = num >> 1        

    print(f"Número: {num} | {paridade} | Dobro (<<1): {dobro} | Metade (>>1): {metade}")

procurado = int(input("\nDigite um número para procurar na matriz: "))

if procurado in elementos:
    print(f"O número {procurado} existe na matriz.")
else:
    print(f"O número {procurado} não existe na matriz.")
