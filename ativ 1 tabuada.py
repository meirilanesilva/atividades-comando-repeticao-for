# Atividade 1 - Gerador de Tabuada

numero = int(input("Digite um número inteiro: "))

for i in range(1, 10 + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
