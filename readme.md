# 📈 Monitor de Preço de Criptomoedas

Um painel interativo desenvolvido com **Streamlit** que permite acompanhar, em tempo real, os preços, variações e volumes das principais criptomoedas.

## 🚀 Funcionalidades
- **Preços em Tempo Real**: Exibe os preços das 100 principais criptomoedas, como Bitcoin e Ethereum.
- **Análise de Variação**: Gráficos interativos para acompanhar as variações de preço nas últimas 24 horas.
- **Alertas de Grandes Variações**: Destaque para moedas com altas ou quedas significativas (> 5% ou < -5%).

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem base para manipulação de dados e integração com APIs.
- **Streamlit**: Framework para criação do painel interativo.
- **CoinGecko API**: Fonte dos dados em tempo real.
- **Pandas**: Manipulação de dados tabulares.
- **Plotly**: Visualizações interativas e atraentes.

## 🖥️ Como Executar o Projeto

### 1. Clone este repositório
```bash
git clone https://github.com/DiegoMB2/Monitor-de-Pre-o-de-Criptomoedas.git
cd Monitor-de-Pre-o-de-Criptomoedas
2. Instale as dependências
Certifique-se de ter o Python instalado. Em seguida, execute:

pip install -r requirements.txt
3. Execute o painel
Inicie o Streamlit para visualizar o painel:

streamlit run monitor.py
4. Visualize no navegador
O Streamlit abrirá automaticamente o painel no navegador. Caso isso não ocorra, acesse:

http://localhost:8501