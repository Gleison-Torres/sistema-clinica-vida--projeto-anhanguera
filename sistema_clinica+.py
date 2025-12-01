# === SISTEMA CLÍNICA VIDA+ ===

# Cores para o sistema
verde = '\033[1;32m'
roxo = '\033[1;35m'
cor = '\033[m'

pacientes = []  # Lista para armazenar os dicionários de pacientes


def cadastrar_paciente():
    print(verde + "--- Cadastro de Paciente ---" + cor)

    nome = input("Nome do paciente: ").strip().title()

    # Tratando erros de entrada.
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Erro: Digite um número válido para idade.")

    telefone = input("Telefone: ").strip()

    paciente = {"nome": nome, "idade": idade, "telefone": telefone}
    pacientes.append(paciente)

    print("Paciente cadastrado com sucesso!")


def ver_estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    media_idade = sum(idades) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(verde + "--- Estatísticas ---" + cor)
    print(f"Número total de pacientes: {total}")
    print(f"Idade média: {media_idade:.1f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")


def buscar_paciente():
    nome_busca = input("Digite o nome do paciente a buscar: ").strip().title()
    encontrados = [p for p in pacientes if p["nome"].lower() == nome_busca.lower()]

    if encontrados:
        print(verde + "--- Paciente Encontrado ---" + cor)
        for p in encontrados:
            print(f"Nome: {p['nome']}")
            print(f"Idade: {p['idade']}")
            print(f"Telefone: {p['telefone']}")
    else:
        print("Paciente não encontrado.")


def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    print(verde + "--- Lista de Pacientes ---" + cor)
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")
    print()


# Loop principal do sistema
while True:
    print(f'{verde + 10* "==="} SISTEMA CLÍNICA VIDA+ {10 * "===" + cor}\n')
    print(roxo + "1. Cadastrar paciente" + cor)
    print(roxo + "2. Ver estatísticas" + cor)
    print(roxo + "3. Buscar paciente" + cor)
    print(roxo + "4. Listar todos os pacientes" + cor)
    print(roxo + "5. Sair" + cor)

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        ver_estatisticas()
    elif opcao == "3":
        buscar_paciente()
    elif opcao == "4":
        listar_pacientes()
    elif opcao == "5":
        print("Encerrando o sistema... Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
