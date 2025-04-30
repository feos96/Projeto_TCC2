# 📊 Distribuição Renovável

### Projeção de Demanda de Energia Elétrica e Recomendação de Distribuição de Fontes Renováveis por Região e Subsistema Brasileiro

---

## 💡 Objetivo do Projeto

Este projeto tem como finalidade:
- **Projetar a demanda de energia elétrica** em diferentes regiões e subsistemas do Brasil.
- **Analisar a capacidade instalada de geração de fontes renováveis** (solar, eólica, hídrica, etc.).
- **Cruzar dados de consumo, geração e atuação das distribuidoras** para **recomendar uma melhor distribuição de energia renovável**, levando em consideração a realidade de cada região.

---

## 🗃️ Bases de Dados Utilizadas

### 🔌 1. Consumo Mensal de Energia Elétrica  
- **Fonte**: EPE – Empresa de Pesquisa Energética  
- **Link direto**: [https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/Consumo-Mensal-de-Energia-Eletrica](https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/Consumo-Mensal-de-Energia-Eletrica)  
- **Formato**: `.xls` ou `.csv`  
- **Descrição**: Contém dados mensais de consumo de energia elétrica por região, subsistema e classe de consumo.  
- **Uso no projeto**: Base para a projeção de demanda por região.

---

### ⚡ 2. Capacidade Instalada de Geração  
- **Fonte**: ONS – Operador Nacional do Sistema Elétrico  
- **Link direto**: [https://www.ons.org.br/paginas/energia-acompanhamento-da-operacao/capacidade-instalada](https://www.ons.org.br/paginas/energia-acompanhamento-da-operacao/capacidade-instalada)  
- **Formato**: `.xlsx` ou `.csv`  
- **Descrição**: Dados de potência instalada (em MW) das usinas por fonte energética (eólica, solar, hídrica, térmica, etc.) e localização.  
- **Uso no projeto**: Análise da disponibilidade de geração renovável em cada região.

---

### 🏢 3. Indicadores Comerciais das Distribuidoras de Energia  
- **Fonte**: ANEEL – Agência Nacional de Energia Elétrica  
- **Link direto**: [https://www.gov.br/aneel/pt-br/assuntos/dados/indicadores-gerenciais-da-distribuicao-indger](https://www.gov.br/aneel/pt-br/assuntos/dados/indicadores-gerenciais-da-distribuicao-indger)  
- **Formato**: `.csv`  
- **Descrição**: Dados mensais por município com indicadores como faturamento, perdas, atendimento e área de concessão das distribuidoras.  
- **Uso no projeto**: Entender a atuação das distribuidoras e sugerir fontes renováveis viáveis para suas áreas.

---

## ⚙️ O Que o Código Faz

### 1. **Carregamento e Pré-processamento**
- Carrega os arquivos `.csv` contendo os dados citados acima.
- Realiza limpeza básica e transformação temporal dos dados.

### 2. **Análise da Demanda**
- Filtra a série de consumo para uma região (ex: Sudeste).
- Aplica dois métodos de previsão:
  - **ARIMA**: Modelo estatístico para séries temporais.
  - **LSTM (Long Short-Term Memory)**: Rede neural recorrente que aprende padrões temporais não-lineares.
- Gera gráficos comparativos entre o histórico e as projeções.

### 3. **Análise da Geração**
- Agrupa e soma a capacidade instalada de fontes renováveis por região.
- Permite identificar gargalos e oportunidades de expansão renovável.

### 4. **Recomendações**
- Integra as previsões de consumo com a capacidade instalada.
- Cruzamento com os dados das distribuidoras permite sugerir:
  - Expansão de energia solar em regiões com alta demanda e baixa capacidade.
  - Aproveitamento de eólica em regiões com alto potencial e baixa cobertura atual.

---

## 📈 Resultados Esperados

- Visualizar a tendência de crescimento da demanda elétrica por região.
- Identificar desbalanceamento entre consumo e geração renovável.
- Criar recomendações práticas e localizadas para expansão sustentável da matriz energética.

---

## 📌 Tecnologias e Bibliotecas

- Python 3
- pandas / numpy
- matplotlib / seaborn
- statsmodels (ARIMA)
- scikit-learn (escalonamento)
- TensorFlow / Keras (LSTM)

---

## 🚧 Próximos Passos

- Implementar análise por **subsistema**.
- Aplicar modelos **SARIMA e Prophet** como alternativa ao ARIMA.
- Integrar API de dados atualizados em tempo real (EPE, ONS, ANEEL).
- Gerar um dashboard com filtros por região, tipo de fonte e distribuidora.

---

### 👤 Autor
**Erick Sousa**  
Estudante de Engenharia de Controle e Automação  
Especialista em dados aplicados à energia e transporte  
[LinkedIn](https://www.linkedin.com/in/erick-sousa-b4183a214/)
