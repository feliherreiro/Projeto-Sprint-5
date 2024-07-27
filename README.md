# Projeto-Sprint-5
O objetivo deste projeto é desenvolver um dashboard web interativo para análise de dados de veículos usados. Utilizando Python, Pandas, Plotly Express e Streamlit, o aplicativo permite visualizar distribuições de odômetro e a relação entre preço e quilometragem. O projeto é implementado na nuvem usando Render para fácil acesso público.

### Análises Gráficas Realizadas e Contexto

No aplicativo web desenvolvido, foram realizadas duas análises gráficas principais utilizando os dados de um DataFrame carregado a partir de um arquivo CSV (`vehicles.csv`). As análises gráficas foram feitas para explorar e visualizar a distribuição e a relação entre diferentes variáveis no conjunto de dados de veículos usados. As duas principais análises gráficas são:

1. **Histograma para Odômetro**
2. **Gráfico de Dispersão para Preço vs. Odômetro**

#### 1. Histograma para Odômetro

**Objetivo**: Visualizar a distribuição dos valores do odômetro (quilometragem) dos veículos usados.

**Descrição**:
- O histograma é uma representação gráfica que organiza um grupo de pontos de dados em intervalos especificados.
- No histograma, a variável representada no eixo x é a quilometragem (odômetro) dos veículos, enquanto o eixo y mostra a contagem de veículos que se enquadram em cada intervalo de quilometragem.
- Essa visualização ajuda a entender a distribuição da quilometragem dos veículos no conjunto de dados, identificando faixas de quilometragem mais comuns e detectando possíveis outliers ou anomalias.

**Código Utilizado**:
```python
def plot_histogram(data, column):
    """Plota um histograma para a coluna especificada."""
    fig = px.histogram(data, x=column, title=f'Histograma da coluna {column}', 
                       labels={column: column.capitalize(), 'count': 'Contagem'},
                       template='plotly_dark')
    fig.update_layout(xaxis_title=column.capitalize(), yaxis_title='Contagem', title_x=0.5)
    st.plotly_chart(fig)
```

#### 2. Gráfico de Dispersão para Preço vs. Odômetro

**Objetivo**: Visualizar a relação entre o preço dos veículos e a quilometragem (odômetro).

**Descrição**:
- O gráfico de dispersão é uma visualização que mostra a relação entre duas variáveis numéricas.
- No gráfico de dispersão, o eixo x representa a quilometragem (odômetro) dos veículos, enquanto o eixo y representa o preço dos veículos.
- Cada ponto no gráfico representa um veículo individual, com sua posição determinada pelos valores das duas variáveis.
- Essa visualização ajuda a identificar padrões, correlações ou tendências entre a quilometragem e o preço dos veículos. Por exemplo, podemos observar se há uma tendência de preços mais baixos para veículos com quilometragem mais alta.

**Código Utilizado**:
```python
def plot_scatter(data, x_column, y_column):
    """Plota um gráfico de dispersão para as colunas especificadas."""
    fig = px.scatter(data, x=x_column, y=y_column, title=f'Gráfico de Dispersão: {x_column} vs. {y_column}',
                     labels={x_column: x_column.capitalize(), y_column: y_column.capitalize()},
                     template='plotly_dark')
    fig.update_layout(xaxis_title=x_column.capitalize(), yaxis_title=y_column.capitalize(), title_x=0.5)
    st.plotly_chart(fig)
```

### Contexto das Análises no DataFrame

O DataFrame carregado contém dados sobre veículos usados, incluindo informações como preço, quilometragem (odômetro), entre outros atributos. No contexto deste projeto, as análises gráficas são focadas em duas variáveis principais:

- **Odômetro (quilometragem)**: Representa a distância total percorrida pelo veículo.
- **Preço**: Representa o valor de venda do veículo.

As análises gráficas realizadas fornecem insights importantes sobre a distribuição dos dados e a relação entre a quilometragem e o preço dos veículos. Isso pode ser útil para diversas finalidades, como:

- **Identificação de Padrões**: Entender como a quilometragem afeta o preço dos veículos.
- **Detecção de Outliers**: Identificar veículos com quilometragem ou preços anormais.
- **Tomada de Decisões**: Informar decisões de compra ou venda de veículos baseadas em dados.

### Aplicação no Dashboard Web

No aplicativo web desenvolvido, os usuários podem interagir com os dados e visualizar os gráficos gerados clicando nos botões "Criar Histograma" e "Criar Gráfico de Dispersão". Essas interações fornecem uma maneira dinâmica de explorar os dados e obter insights visuais de maneira intuitiva e interativa.

https://projeto-sprint-5-1-d0yr.onrender.com/
