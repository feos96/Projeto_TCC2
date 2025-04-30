import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# ----- 1. CARREGAMENTO DOS DADOS -----
consumo_df = pd.read_csv('consumo_mensal_energia.csv')  # ['Data', 'Região', 'Consumo_MWh']
consumo_df['Data'] = pd.to_datetime(consumo_df['Data'])
consumo_df = consumo_df.sort_values('Data')

# ----- 2. AGRUPAMENTO POR REGIÃO (exemplo com Sudeste) -----
regiao = 'Sudeste'
serie = consumo_df[consumo_df['Região'] == regiao].set_index('Data')['Consumo_MWh']

# ====================== OPÇÃO 1: ARIMA ======================

# Modelagem ARIMA
arima_model = ARIMA(serie, order=(2, 1, 2))  # valores (p,d,q) ajustáveis
arima_fit = arima_model.fit()
forecast_arima = arima_fit.forecast(steps=12)

# Plot ARIMA
plt.figure(figsize=(10, 4))
plt.plot(serie[-36:], label='Histórico')
plt.plot(forecast_arima.index, forecast_arima, label='Previsão ARIMA', color='red')
plt.title(f'Projeção ARIMA - Consumo Elétrico ({regiao})')
plt.legend()
plt.tight_layout()
plt.show()

# ====================== OPÇÃO 2: LSTM ======================

# Escalonar os dados
scaler = MinMaxScaler()
serie_scaled = scaler.fit_transform(serie.values.reshape(-1, 1))

# Criar sequência para LSTM
def criar_sequencia(series, n_passos):
    X, y = [], []
    for i in range(n_passos, len(series)):
        X.append(series[i-n_passos:i])
        y.append(series[i])
    return np.array(X), np.array(y)

n_passos = 12
X, y = criar_sequencia(serie_scaled, n_passos)

# Modelagem LSTM
model = Sequential([
    LSTM(50, activation='relu', input_shape=(n_passos, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=100, verbose=0)

# Fazer previsões futuras
entrada = serie_scaled[-n_passos:]
entrada = entrada.reshape((1, n_passos, 1))
predicoes = []

for _ in range(12):
    yhat = model.predict(entrada, verbose=0)
    predicoes.append(yhat[0, 0])
    entrada = np.append(entrada[:, 1:, :], [[yhat]], axis=1)

predicoes_lstm = scaler.inverse_transform(np.array(predicoes).reshape(-1, 1))

# Plot LSTM
plt.figure(figsize=(10, 4))
plt.plot(serie[-36:], label='Histórico')
plt.plot(pd.date_range(serie.index[-1], periods=13, freq='M')[1:], predicoes_lstm, label='Previsão LSTM', color='green')
plt.title(f'Projeção LSTM - Consumo Elétrico ({regiao})')
plt.legend()
plt.tight_layout()
plt.show()