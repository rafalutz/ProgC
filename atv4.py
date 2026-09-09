notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)

print(f"\nNotas digitadas: {notas}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

if 10 in notas:
    print("Parabéns! Você tirou nota máxima em pelo menos uma avaliação!")

print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
