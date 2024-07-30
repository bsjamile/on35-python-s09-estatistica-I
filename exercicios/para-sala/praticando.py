import pandas as pd

idade = [15,20,30,45,20,69]

idade_df = pd.DataFrame(idade)

media_idade = idade_df.mean()

print(media_idade)

moda_idade = idade_df.mode()

print(moda_idade)

mediana_idade = idade_df.median()

print(mediana_idade)

variancia_populacional = idade_df.var(ddof=0) # da amostra inteira

print(round(variancia_populacional,2))

desvio_padrao = idade_df.var() ** 0.5 #raiz quadrada da variancia

print(round(desvio_padrao,2))

cv = (desvio_padrao/media_idade) * 100 #coeficiente de variancia = maior variabilidade relativa
#Um CV de aproximadamente 27.45% indica que o desvio padrão é cerca de 27.45% da média. 

print(idade_df.describe().T)