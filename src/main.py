# SISTEMA DE CRONOGRAMA DE ESTUDOS
#
# Requisitos

# O usuário deve digitar o conteúdo e o dia para o sistema guardar
# o sistema deve informar o usuário sobre o dia e o conteúdo
# O sistema deve ter uma opção de adicionar, quando interagir, o sistema pede o nome e dia da matéria.
# O sistema deve ter uma opção de remover caso a o usuário queira remover alguma materia.

Conteudo = []

def carregar_dados():
    try:
        with open("dados/Materias.txt", "r") as arquivo:
            for linha in arquivo:
                nome_materia, dia = linha.strip().split(";")
                Conteudo.append({"nome": nome_materia, "dia": dia})
    except FileNotFoundError:
        pass
                
def Adicionar():
    nome_materia = input("Digite o nome do conteúdo:").strip()
    dia = (input("Digite o dia da semana para estudar essa matéria:"))
    Conteudo.append({"nome": nome_materia, "dia": dia})
    print("adicionado com sucesso!\n")

    with open("dados/Materias.txt", "a") as arquivo:
            arquivo.write(f"{nome_materia};{dia}\n")
    
def Listar():
    if not Conteudo:
        print("Nenhuma matéria cadastrada ainda.\n")
        return

    print("\n=== MATÉRIAS CADASTRADAS ===")
    for index, item in enumerate(Conteudo, start=1):
        print(f"{index} - {item['nome']} ({item['dia']})")
    print()


def Remover():
    if not Conteudo:
        print("Não há matérias para remover.\n")
        return

    print("=== MATÉRIAS CADASTRADAS ===")
    for item in Conteudo:
        print(f"{item['nome']} - {item['dia']}")

    remover = input("\nDigite o nome da matéria a ser removida: ").strip()

    for item in Conteudo:
        if item["nome"].lower() == remover.lower():
            Conteudo.remove(item)
            print("Removido com sucesso!\n")

            # Agora reescreve o arquivo SEM a matéria removida
            with open("dados/Materias.txt", "w") as arquivo:
                for materia in Conteudo:
                    arquivo.write(f"{materia['nome']};{materia['dia']}\n")

            break
    else:
        print("Matéria não encontrada.\n")
        
        
def Menu():
    opcao = 0
    while (opcao != 4):
      
        print("===MENU===")
        print("1 - ADICIONAR ")
        print("2 - Remover")
        print("3 - Listar")
        print("4 - Encerrar")

        try:
            opcao = int(input("Digite a opção desejada:"))
        except ValueError:
            print("por favor, digite um numero valido.\n")
            

        if opcao == 1:
            Adicionar()
            
        elif opcao == 2:
            Remover()

        elif opcao == 3:
            Listar()

        elif opcao == 4:
            print("Encerrando...")
            
        else:
            print("O número digitado é inválido")
        
carregar_dados()
Menu()