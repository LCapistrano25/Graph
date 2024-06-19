from colorama import init, Fore

from node import No

class Grafo:
    def __init__(self):
        self.nos = {}  # Inicializa um dicionário de nós do grafo
        self.proximo_id = 1  # Inicializa o próximo id disponível para cidades

    def adicionar_no(self, nome):
        # Verifica se o nome da cidade já existe no grafo
        if any(nome == no.conteudo for no in self.nos.values()):
            print(f"{Fore.RED}Erro: A cidade '{nome}' já existe no grafo.")
            return None
        
        no = No(nome)
        self.nos[self.proximo_id] = no  # Adiciona um nó ao dicionário de nós do grafo com o próximo id disponível
        self.proximo_id += 1  # Atualiza o próximo id disponível
        return no

    def adicionar_rota(self, origem_id, destino_id, custo):
        if origem_id in self.nos and destino_id in self.nos:
            origem = self.nos[origem_id].conteudo
            destino = self.nos[destino_id].conteudo
            self.nos[origem_id].adicionar_vizinho(self.nos[destino_id], custo)
        else:
            print("Uma das cidades não foi encontrada no grafo.")

    def _encontrar_caminho_recursivo(self, no_atual, destino, distancias, caminho_anterior, custo_atual):
        """
        Função auxiliar para encontrar o caminho menos custoso de forma recursiva.
        """
        # Se alcançamos o destino, não precisamos continuar
        if no_atual == destino:
            return

        # Explora os vizinhos do nó atual
        for vizinho, custo in no_atual.vizinhos.items():
            custo_total = custo_atual + custo
            # Se o custo total para o vizinho for menor que a distância conhecida
            if custo_total < distancias[vizinho]:
                distancias[vizinho] = custo_total
                caminho_anterior[vizinho] = no_atual  # Atualiza o caminho anterior para o vizinho
                # Chama recursivamente para o vizinho
                self._encontrar_caminho_recursivo(vizinho, destino, distancias, caminho_anterior, custo_total)

    def _encontrar_caminho_menos_custoso(self, origem_id, destino_id):
        """
        Encontra o caminho menos custoso entre duas cidades no grafo,
        utilizando os IDs das cidades.
        Retorna o caminho e o custo total.
        """
        origem = self.nos[origem_id]
        destino = self.nos[destino_id]
        
        # Dicionário para armazenar a menor distância conhecida até cada nó
        distancias = {no: float('inf') for no in self.nos.values()}
        distancias[origem] = 0  # Define a distância da origem como 0

        # Dicionário para armazenar o caminho
        caminho_anterior = {origem: None}

        # Inicia a recursão a partir da origem
        self._encontrar_caminho_recursivo(origem, destino, distancias, caminho_anterior, 0)

        # Recupera o caminho mínimo até o destino
        caminho = []
        no_atual = destino

        while no_atual is not None:
            caminho.insert(0, no_atual)  # Insere o nó atual no início do caminho
            no_atual = caminho_anterior[no_atual]  # Vai para o nó anterior no caminho
        
        # Retorna o caminho e o custo total
        return caminho, distancias[destino]

    def mostrar_caminho_menos_custoso(self, origem_id, destino_id):
        """
        Mostra o caminho menos custoso entre duas cidades no grafo,
        utilizando os IDs das cidades.
        """
        # Encontra o caminho menos custoso e o custo total
        caminho, custo_total = self._encontrar_caminho_menos_custoso(origem_id, destino_id)

        if custo_total != float('inf'):
            # Se existe um caminho, exibe o caminho e o custo total
            print(f'Caminho menos custoso de {self.nos[origem_id].conteudo} para {self.nos[destino_id].conteudo}:')
            for i, no in enumerate(caminho):
                if i < len(caminho) - 1:
                    print(f'{no.conteudo} <- ', end='')
                else:
                    print(f'{no.conteudo}')
            print(f'Custo total: {custo_total} km')
        else:
            # Se não existe um caminho, exibe uma mensagem
            print(f'Não há caminho de {self.nos[origem_id].conteudo} para {self.nos[destino_id].conteudo}')

    def mostrar_caminho(self, origem_id, destino_id):
        """
        Mostra um caminho entre duas cidades no grafo utilizando os IDs das cidades.
        Esta função atualmente não está sendo utilizada no menu principal.
        """
        origem = self.nos[origem_id]
        destino = self.nos[destino_id]
        
        caminho_atual = [origem]  # Inicializa o caminho atual com a origem
        self._traversar(origem.vizinhos, origem, destino, origem.conteudo, caminho_atual)  # Chama a função para mostrar o caminho

    def _traversar(self, vizinhos, origem, destino, caminho, caminho_atual):
        """
        Função auxiliar para realizar a travessia recursiva para encontrar um caminho entre origem e destino.
        Esta função atualmente não está sendo utilizada no menu principal.
        """
        for vizinho, _ in vizinhos.items():
            if destino.conteudo in caminho:
                break

            if vizinho == destino:
                # Se o vizinho é o destino, atualiza e imprime o caminho
                caminho_atualizado = caminho + " <- " + destino.conteudo
                print(caminho_atualizado)
                break

            if vizinho not in caminho_atual:
                # Adiciona o vizinho ao caminho atual e chama a função recursivamente
                caminho_atual.append(vizinho)
                self._traversar(
                    vizinho.vizinhos, origem, destino, caminho + " <- " + vizinho.conteudo, caminho_atual
                )
                caminho_atual.remove(vizinho)  # Remove o vizinho do caminho atual ao voltar da recursão

    def mostrar_todas_as_rotas(self, origem_id, destino_id):
        """
        Mostra todas as rotas entre duas cidades no grafo utilizando os IDs das cidades.
        """
        if origem_id in self.nos and destino_id in self.nos:
            origem = self.nos[origem_id]
            destino = self.nos[destino_id]
            
            todas_as_rotas = []
            self._buscar_todas_as_rotas(origem, destino, [], 0, todas_as_rotas)
            if todas_as_rotas:
                print(f'Todas as rotas de {origem.conteudo} para {destino.conteudo} e seus custos:')
                for rota, custo in todas_as_rotas:
                    print(f'Rota: {" <- ".join(no.conteudo for no in rota)}, Custo: {custo} km')
            else:
                print(f'Não há rotas de {origem.conteudo} para {destino.conteudo}')
        else:
            print("Uma das cidades não foi encontrada no grafo.")

    def _buscar_todas_as_rotas(self, no_atual, destino, caminho_atual, custo_atual, todas_as_rotas):
        """
        Função auxiliar para buscar todas as rotas entre duas cidades no grafo de forma recursiva.
        """
        caminho_atual.append(no_atual)
        if no_atual == destino:
            todas_as_rotas.append((list(caminho_atual), custo_atual))
        else:
            for vizinho, custo in no_atual.vizinhos.items():
                if vizinho not in caminho_atual:
                    self._buscar_todas_as_rotas(vizinho, destino, caminho_atual, custo_atual + custo, todas_as_rotas)
        caminho_atual.pop()

