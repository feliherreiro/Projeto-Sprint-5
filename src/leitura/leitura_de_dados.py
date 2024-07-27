# Função para carregar os dados
def load_data(file_path):
    """Carrega os dados de um arquivo CSV e retorna um DataFrame."""
    data = pd.read_csv(file_path)
    return data