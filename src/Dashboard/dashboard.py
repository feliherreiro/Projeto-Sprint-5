# Função principal para o Streamlit
def main():
    st.title('Análise de Veículos Usados')

    # Carrega e pré-processa os dados
    file_path = Path("../Data/vehicles.csv")  # Caminho correto do arquivo
    data = load_data(file_path)
    data = preprocess_data(data)

    # Exibe os dados carregados
    st.write("Dados Carregados")
    st.write(data.head())

    # Opções de visualização
    if st.button('Criar Histograma'):
        st.write('Criando um histograma para o odômetro')
        plot_histogram(data, 'odometer')

    if st.button('Criar Gráfico de Dispersão'):
        st.write('Criando um gráfico de dispersão para preço vs. odômetro')
        plot_scatter(data, 'odometer', 'price')

if __name__ == "__main__":
    main()