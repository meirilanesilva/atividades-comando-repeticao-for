# Atividade 3 - Contagem Condicional

pontuacoes = [5, 9, 3, 10, 2, 7, 8]

criticas_encontradas = 0  # acumulador

for pontuacao in pontuacoes:
    if pontuacao >= 8:
        criticas_encontradas += 1

print(f"Total de máquinas em situação crítica: {criticas_encontradas}")
