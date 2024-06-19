from colorama import init, Fore

from graph import Grafo

init(autoreset=True)  # Inicializa colorama para reset automático das cores

def mostrar_menu(grafo):
    """
    Função para exibir o menu interativo e interagir com o grafo.
    """
    while True:
        print("\nMenu:")
        print(f"{Fore.BLUE}1. Adicionar cidade")
        print(f"{Fore.BLUE}2. Adicionar rota entre cidades")
        print(f"{Fore.BLUE}3. Mostrar caminho menos custoso entre duas cidades")
        print(f"{Fore.BLUE}4. Mostrar todas as rotas entre duas cidades")
        print(f"{Fore.RED}5. Sair")
        escolha = input(f"\n{Fore.YELLOW}Escolha uma opção: ")

        if escolha == '1':
            # Opção para adicionar uma cidade ao grafo
            cidade = input(f"\nDigite o nome da cidade: ")
            novo_no = grafo.adicionar_no(cidade)
            if novo_no:
                print(f'Cidade {cidade} adicionada.')
        
        elif escolha == '2':
            # Opção para adicionar uma rota entre duas cidades no grafo
            if len(grafo.nos) < 2:
                print("É necessário adicionar pelo menos duas cidades para adicionar uma rota.")
                continue

            print(f"\n{Fore.BLUE}Cidades disponíveis:")
            for id, no in grafo.nos.items():
                print(f"{Fore.GREEN}{id}: {no.conteudo}")

            origem_id = int(input(f"\nDigite o número da cidade de origem: "))
            destino_id = int(input(f"\nDigite o número da cidade de destino: "))
            custo = float(input(f"\nDigite a distância em km: "))
            grafo.adicionar_rota(origem_id, destino_id, custo)
            print(f'Rota de {grafo.nos[origem_id].conteudo} para {grafo.nos[destino_id].conteudo} com distância {custo} km adicionada.')

        elif escolha == '3':
            # Opção para mostrar o caminho menos custoso entre duas cidades no grafo
            if len(grafo.nos) < 2:
                print("É necessário adicionar pelo menos duas cidades para buscar um caminho.")
                continue

            print(f"\n{Fore.BLUE}Cidades disponíveis:")
            for id, no in grafo.nos.items():
                print(f"{Fore.GREEN}{id}: {no.conteudo}")

            origem_id = int(input(f"\nDigite o número da cidade de origem: "))
            destino_id = int(input(f"\nDigite o número da cidade de destino: "))
            grafo.mostrar_caminho_menos_custoso(origem_id, destino_id)
        
        elif escolha == '4':
            # Opção para mostrar todas as rotas entre duas cidades no grafo
            if len(grafo.nos) < 2:
                print("É necessário adicionar pelo menos duas cidades para buscar rotas.")
                continue

            print(f"\n{Fore.BLUE}Cidades disponíveis:")
            for id, no in grafo.nos.items():
                print(f"{Fore.GREEN}{id}: {no.conteudo}")

            origem_id = int(input(f"\nDigite o número da cidade de origem: "))
            destino_id = int(input(f"\nDigite o número da cidade de destino: "))
            grafo.mostrar_todas_as_rotas(origem_id, destino_id)

        elif escolha == '5':
            # Opção para sair do programa
            print(f"{Fore.RED}Saindo...")
            break
        
        else:
            # Tratamento para escolhas inválidas
            print(f"{Fore.RED}Opção inválida. Tente novamente.")

def main():
    # Função principal que inicializa o grafo e mostra o menu interativo
    grafo = Grafo()
    mostrar_menu(grafo)

if __name__ == "__main__":
    main()