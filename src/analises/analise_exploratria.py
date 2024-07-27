# Função para plotar histograma
def plot_histogram(data, column):
    """Plota um histograma para a coluna especificada."""
    fig = px.histogram(data, x=column)
    fig.show()

def plot_scatter(data, x_column, y_column):
    """Plota um gráfico de dispersão para as colunas especificadas."""
    fig = px.scatter(data, x=x_column, y=y_column)
    fig.show()

# Função para plotar gráfico de dispersão
def plot_scatter(data, x_column, y_column):
    """Plota um gráfico de dispersão para as colunas especificadas."""
    fig = px.scatter(data, x=x_column, y=y_column)
    st.plotly_chart(fig)