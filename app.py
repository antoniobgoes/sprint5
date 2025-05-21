import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Anúncios de vendas de carros')

car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma')

if hist_button:

    st.write('Criando um histograma para a coluna de odômetro')

    fig_hist = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig_hist, use_container_width=True)

scatter_box = st.checkbox('Criar gráfico de dispersão')

if scatter_box:
    st.write('Criando um histograma para a coluna de preço anunciados')

    fig_scatter = px.scatter(car_data, x='price', y='model')

    st.plotly_chart(fig_scatter, use_container_width=True)
