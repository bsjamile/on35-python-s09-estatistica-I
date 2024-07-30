## Conjunto de Dados
# Os dados estão disponíveis em formato csv (‘vendas_ficticias.csv’) e contêm as seguintes informações para cada venda:

#   •	Data da venda
#   •	Valor da venda
#   •	Vendedor
#   •	Quantidade vendida
#   •	Produto


# from tabulate import tabulate

# print(tabulate(arquivo.head(), headers='keys', tablefmt='fancy_grid'))

f = open('vendas_ficticias.csv', 'r')

data = f.read()

rows = data.split('\n')

print(rows)

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)