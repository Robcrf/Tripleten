import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('vehicles_us.csv')

st.header("Panel de Control: Análisis de Vehículos en EE.UU.")

if st.checkbox("Mostrar Histograma de Precios"):
    
    st.write("Generando histograma de precios...")
    filtered_data = data[(data['odometer'] >= 0) & (data['odometer'] <= 300000)]
    fig = go.Figure(data=[go.Histogram(x=filtered_data['odometer'], nbinsx=50)])
    fig.update_layout(
        title='Histograma de Odómetro de Vehículos (0-300,000 millas)',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Frecuencia',
        bargap=0.2,
        template='plotly_white'
    )
    st.plotly_chart(fig)

    st.write("Análisis completado.")


if st.checkbox("Mostrar Gráfico de Dispersión de Precio vs Odómetro"):
    st.write("Generando gráfico de dispersión de precio vs odómetro...")
    filtered_data_scatter = data[(data['odometer'] >= 0) & (data['odometer'] <= 300000) & (data['price'] > 0)]
    fig_scatter = go.Figure(data=go.Scatter(
        x=filtered_data_scatter['odometer'],
        y=filtered_data_scatter['price'],
        mode='markers',
        marker=dict(
            size=5,
            color='rgba(152, 0, 0, .8)',
            line=dict(
                width=1,
                color='rgba(0, 0, 0, .8)'
            )
        )
    ))
    
    fig_scatter.update_layout(
        title='Scatter Plot de Precio vs Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)',
        template='plotly_white'
    )
    st.plotly_chart(fig_scatter)
    st.write("Análisis completado.")

