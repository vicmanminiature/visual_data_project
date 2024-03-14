import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.markdown("<h1 style='text-align: center; color: orange;'>Análisis de Vehículos - Visualización Interactiva</h1>", unsafe_allow_html=True)

if st.checkbox('Mostrar gráfico de barras de tipo de combustible'):
    st.write("Este gráfico de barras muestra el número de vehículos para cada tipo de combustible.")
    fig = px.bar(car_data, x="fuel", color="transmission", title="Número de vehículos por tipo de combustible",
                 color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig)

if st.checkbox('Mostrar gráfico de caja de precios'):
    st.write("Este gráfico de caja muestra la distribución de los precios para cada tipo de vehículo.")
    fig = px.box(car_data, x="type", y="price", title="Distribución de precios por tipo de vehículo",
                 color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig)

if st.checkbox('Mostrar histograma de años de modelo'):
    st.write("Este histograma muestra la distribución de los años de los modelos.")
    fig = px.histogram(car_data, x="model_year", title="Distribución de años de modelo",
                       color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig)

if st.checkbox('Mostrar gráfico de dispersión de precio vs odómetro'):
    st.write("Este gráfico de dispersión muestra la relación entre el precio y el odómetro, coloreado por el tipo de transmisión.")
    fig = px.scatter(car_data, x="price", y="odometer", color="transmission", title="Precio vs Odómetro por tipo de transmisión",
                     color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig)