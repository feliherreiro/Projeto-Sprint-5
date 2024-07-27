# Função para pré-processar os dados
def preprocess_data(data):
    """Realiza o pré-processamento dos dados, como tratamento de valores ausentes e formatação."""
    data = data.dropna()  # Remove linhas com valores ausentes
    data.loc[:, 'price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)  # Converte preços para float
    return data