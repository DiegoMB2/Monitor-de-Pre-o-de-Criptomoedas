import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Configuração do layout do Streamlit
st.set_page_config(page_title="Monitor de Preço de Criptomoedas", layout="wide")
st.title("📈 Monitor de Preço de Criptomoedas")
st.markdown("""
Acompanhe os preços, variações e volumes das principais criptomoedas em tempo real.
Os dados são atualizados diretamente da API CoinGecko.
""")

# Função para obter dados da CoinGecko API
@st.cache_data(ttl=60)
def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",  # Moeda de referência (USD)
        "order": "market_cap_desc",  # Ordenar por capitalização de mercado
        "per_page": 100,  # Número de criptomoedas
        "page": 1,
        "sparkline": False,  # Não incluir dados de histórico (gráficos menores)
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error("Erro ao obter dados da CoinGecko API.")
        return pd.DataFrame()

# Obter dados de criptomoedas
crypto_data = get_crypto_data()

if not crypto_data.empty:
    # Mostrar tabela de criptomoedas
    st.header("📊 Principais Criptomoedas")
    st.dataframe(
        crypto_data[["name", "current_price", "market_cap", "price_change_percentage_24h", "total_volume"]],
        height=600,
    )

    # Gráfico interativo de variação de preço
    st.header("📉 Variação de Preço (%)")
    fig = px.bar(
        crypto_data,
        x="name",
        y="price_change_percentage_24h",
        color="price_change_percentage_24h",
        title="Variação de Preço em 24h (%)",
        labels={"name": "Criptomoeda", "price_change_percentage_24h": "Variação (%)"},
        template="plotly_white",
    )
    st.plotly_chart(fig, use_container_width=True)

    # Destacar grandes variações
    st.header("🔔 Alertas de Variações Significativas")
    high_variations = crypto_data[crypto_data["price_change_percentage_24h"] > 5]
    low_variations = crypto_data[crypto_data["price_change_percentage_24h"] < -5]

    if not high_variations.empty:
        st.success(f"{len(high_variations)} criptomoedas com alta acima de 5% nas últimas 24h:")
        st.table(high_variations[["name", "price_change_percentage_24h"]])

    if not low_variations.empty:
        st.error(f"{len(low_variations)} criptomoedas com queda acima de 5% nas últimas 24h:")
        st.table(low_variations[["name", "price_change_percentage_24h"]])
else:
    st.warning("Nenhum dado encontrado. Tente novamente mais tarde.")

# Nota de rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Diego da Silva Meneses, um analista de dados e entusiasta de blockchain.")
