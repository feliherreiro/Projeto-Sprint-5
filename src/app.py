import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

# Função para carregar os dados
def load_data(file_path):
    """Carrega os dados de um arquivo CSV e retorna um DataFrame."""
    data = pd.read_csv(file_path)
    return data

# Função para pré-processar os dados
def preprocess_data(data):
    """Realiza o pré-processamento dos dados, como tratamento de valores ausentes e formatação."""
    data = data.dropna()  # Remove linhas com valores ausentes
    data.loc[:, 'price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)  # Converte preços para float
    return data

# Função para plotar histograma
def plot_histogram(data, column):
    """Plota um histograma para a coluna especificada."""
    fig = px.histogram(data, x=column, title=f'Histograma da coluna {column}', 
                       labels={column: column.capitalize(), 'count': 'Contagem'},
                       template='plotly_dark')
    fig.update_layout(xaxis_title=column.capitalize(), yaxis_title='Contagem', title_x=0.5)
    st.plotly_chart(fig)

# Função para plotar gráfico de dispersão
def plot_scatter(data, x_column, y_column):
    """Plota um gráfico de dispersão para as colunas especificadas."""
    fig = px.scatter(data, x=x_column, y=y_column, title=f'Gráfico de Dispersão: {x_column} vs. {y_column}',
                     labels={x_column: x_column.capitalize(), y_column: y_column.capitalize()},
                     template='plotly_dark')
    fig.update_layout(xaxis_title=x_column.capitalize(), yaxis_title=y_column.capitalize(), title_x=0.5)
    st.plotly_chart(fig)

# Função principal para o Streamlit
def main():
    st.title('Análise de Veículos Usados')
    
    # Carrega e pré-processa os dados
    file_path = Path("Data/vehicles.csv")  # Caminho correto do arquivo
    data = load_data(file_path)
    data = preprocess_data(data)
    
    # Exibe os dados carregados
    st.write("### Dados Carregados")
    st.write(data.head())
    
    # Opções de visualização
    if st.button('Criar Histograma'):
        st.write('## Histograma para o Odômetro')
        plot_histogram(data, 'odometer')
    
    if st.button('Criar Gráfico de Dispersão'):
        st.write('## Gráfico de Dispersão para Preço vs. Odômetro')
        plot_scatter(data, 'odometer', 'price')

if __name__ == "__main__":
    main()
