class No:
    def __init__(self, conteudo):
        """
        Inicializa um nó (cidade) com o conteúdo especificado.
        """
        self.conteudo = conteudo  # Conteúdo do nó
        self.vizinhos = {}  # Dicionário para armazenar vizinhos e custos

    def adicionar_vizinho(self, vizinho, custo):
        """
        Adiciona um vizinho (outra cidade) com o custo da aresta.
        """
        self.vizinhos[vizinho] = custo  # Adiciona um vizinho com o custo da aresta

    def __lt__(self, other):
        """
        Define a comparação entre nós com base no conteúdo (nome da cidade).
        """
        return self.conteudo < other.conteudo  # Define a comparação entre nós
