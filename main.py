import pandas as pd
import matplotlib.pyplot as plt
import json

# Lendo o arquivo CSV
dados = pd.read_csv('janela.csv')

# Convertendo a coluna 'created_at' para o tipo datetime
dados['created_at'] = pd.to_datetime(dados['created_at'])

# Processando a coluna 'value'
dados['value'] = dados['value'].apply(json.loads)
dados['aberturaMaximaJanelaCM'] = dados['value'].apply(
    lambda x: x['aberturaMaximaJanelaCM'])
dados['aberturaJanelaCm'] = dados['value'].apply(
    lambda x: x['aberturaJanelaCm'])
dados['temperatura'] = dados['value'].apply(lambda x: x['temperatura'])

# Definindo 'created_at' como índice
dados.set_index('created_at', inplace=True)

# Plotando a temperatura ao longo do tempo
plt.figure(figsize=(12, 6))
plt.plot(dados['temperatura'], label='Temperatura')
plt.title('Temperatura e Abertura da Janela ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('Temperatura / Abertura da Janela')
plt.legend()

# Plotando a abertura da janela ao longo do tempo
plt.plot(dados['aberturaJanelaCm'], label='Abertura da Janela')
plt.legend()

# Mostrando o gráfico
plt.show()
