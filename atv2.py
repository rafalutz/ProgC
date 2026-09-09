num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

print(f"\nSoma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} x {num2} = {multiplicacao}")

if num2 != 0:
    divisao = num1 / num2
    print(f"Divisão: {num1} / {num2} = {divisao}")
else:
    print("Divisão: não é possível dividir por zero.")
