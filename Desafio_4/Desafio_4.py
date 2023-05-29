import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Diretório principal onde estão os subdiretórios e arquivos:
diretorio_principal = 'C:\\Users\\kenji\\Downloads\\archive (1)'

# Lista para armazenar os dataframes de cada arquivo:
dataframes = []

# Loop de repetição para percorrer todos os subdiretórios e arquivos dentro do diretório principal
for root, dirs, files in os.walk(diretorio_principal):
    for file in files:
        # Verificar se o arquivo é um arquivo CSV
        if file.endswith('.csv'):
            # Caminho completo para o arquivo
            arquivo_csv = os.path.join(root, file)
            print(arquivo_csv)

            # Ler o arquivo CSV e adicionar o dataframe à lista
            df = pd.read_csv(arquivo_csv, encoding='latin1')
            dataframes.append(df)

# Concatenar os dataframes em um único dataframe:
dataframe_final = pd.concat(dataframes)

# Converter a coluna 'OrderDate' para o tipo datetime:
dataframe_final['OrderDate'] = pd.to_datetime(dataframe_final['OrderDate'])

# Agrupar por data e contar a quantidade de pedidos:
pedidos_por_data = dataframe_final.groupby('OrderDate').size()

# Converter a série para um objeto DatetimeIndex com frequência diária:
pedidos_por_data = pedidos_por_data.asfreq('D')

# Preencher valores ausentes com a média dos valores não ausentes:
pedidos_por_data = pedidos_por_data.fillna(pedidos_por_data.mean())

# Decomposição da série temporal:
decomposition = seasonal_decompose(pedidos_por_data, model='additive')

# Obter os resíduos:
residuos = decomposition.resid

# Calcular os z-scores dos resíduos:
z_scores = stats.zscore(residuos)

# Definir um limiar para identificação de outliers (por exemplo, 3 desvios padrão):
limiar = 3

# Identificar os índices dos outliers:
indices_outliers = np.where(np.abs(z_scores) > limiar)[0]

# Criar a figura e os subplots:
fig, axs = plt.subplots(4, 1, figsize=(10, 8))

# Subplot 1: Quantidade de Pedidos por Data:
axs[0].plot(pedidos_por_data)
axs[0].set_title('Quantidade de Pedidos por Data')
axs[0].set_ylabel('Quantidade de Pedidos')

# Subplot 2: Tendência:
axs[1].plot(decomposition.trend)
axs[1].set_title('Tendência')
axs[1].set_ylabel('Tendência')

# Subplot 3: Sazonalidade:
axs[2].plot(decomposition.seasonal)
axs[2].set_title('Sazonalidade')
axs[2].set_ylabel('Sazonalidade')

# Subplot 4: Resíduos com outliers destacados:
axs[3].plot(residuos)
axs[3].scatter(indices_outliers, residuos[indices_outliers], color='red', label='Outliers')
axs[3].axhline(y=0, color='black', linestyle='--')
axs[3].set_title('Resíduos')
axs[3].set_ylabel('Resíduos')
axs[3].set_xlabel('Data')
axs[3].legend()

# Ajustar layout dos subplots:
plt.tight_layout()

# Exibir o gráfico:
plt.show()

# Adicionar coluna de mês ao dataframe:
pedidos_por_data = pedidos_por_data.to_frame(name='TotalOrders')
pedidos_por_data['Month'] = pedidos_por_data.index.month

# Calcular a média móvel da quantidade de pedidos nos últimos 3 meses:
pedidos_por_data['Average_Sales_Last_3_Months'] = pedidos_por_data['TotalOrders'].rolling(window=3).mean()

# Remover as linhas com valores ausentes:
pedidos_por_data = pedidos_por_data.dropna()

# Separar as features e o target:
X = pedidos_por_data[['Month', 'Average_Sales_Last_3_Months']]
y = pedidos_por_data['TotalOrders']

# Criar e treinar o modelo de regressão:
modelo = DecisionTreeRegressor()
modelo.fit(X, y)

# Prever as vendas do próximo mês:
ultimo_mes = pedidos_por_data['Month'].max()
ultimo_mes_3_meses = ultimo_mes - 3
media_ultimos_3_meses = pedidos_por_data[pedidos_por_data['Month'] >= ultimo_mes_3_meses]['TotalOrders'].mean()
previsao_mes_seguinte = modelo.predict([[ultimo_mes + 1, media_ultimos_3_meses]])

print('Previsão de Vendas do Próximo Mês:', previsao_mes_seguinte)


"""Esse texto é mais uma desabafo, por não ter tanto conhecimento do assunto fiz todo o processo acompanhando cursos
online sobre o assunto e por conta disso sinto que poderia ter feito melhor. Mas priorizei deixar o código funcional
e usar todos os conhecimentos précios que já tinha para resolver o problema."""