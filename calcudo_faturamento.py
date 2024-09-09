import json

with open('C:\\Users\\klebe\\OneDrive\\Desktop\\Desafio\\dados.json') as file:
    faturamento = json.load(file)

faturamentos_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(faturamentos_validos)
maior_faturamento = max(faturamentos_validos)

media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

dias_acima_da_media = len([dia['valor'] for dia in faturamento if dia['valor'] > media_mensal])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Ele filtra apenas os dias com faturamento maior que zero (ignora dias sem faturamento), calcula o menor e maior faturamento do mês e a média de faturamento dos dias válidos e o número de dias com faturamento acima da média é calculado e todos os resultados são exibidos.