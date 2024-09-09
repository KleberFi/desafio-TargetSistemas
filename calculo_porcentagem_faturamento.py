faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

for estado, valor in faturamento_por_estado.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")

# Os valores de faturamento de cada estado são armazenados em um dicionário, o total de faturamento é calculado somando os valores de todos os estados, para cada estado, o percentual de contribuição ao faturamento total é calculado e impresso.