# =========================================================
# SISTEMA DE CADASTRO DE ALUNOS (PROJETO DIDÁTICO)
# Desenvolvido para estudo de:
# - Funções
# - Listas (arrays)
# - Dicionários
# - Menus
# - Modularização
# - Validação de dados
# - Estruturas condicionais
# - Laços
# - Sem variáveis globais
# =========================================================

# ----------- MODELO DE DADOS -----------
def criar_aluno(nome, idade, matricula, notas):
    return {
        "nome": nome,
        "idade": idade,
        "matricula": matricula,
        "notas": notas
    }

# ----------- VALIDAÇÕES -----------
def validar_nome(nome):
    return nome.replace(" ", "").isalpha()


def validar_idade(idade):
    return idade.isdigit() and 0 < int(idade) < 120


def validar_matricula(matricula, alunos):
    if not matricula.isdigit():
        return False
    for a in alunos:
        if a["matricula"] == matricula:
            return False
    return True


# ----------- FUNÇÕES DO SISTEMA -----------
def cadastrar_aluno(alunos):
    print("\n--- CADASTRO DE ALUNO ---")

    while True:
        nome = input("Nome: ")
        if validar_nome(nome):
            break
        print("Nome inválido.")

    while True:
        idade = input("Idade: ")
        if validar_idade(idade):
            idade = int(idade)
            break
        print("Idade inválida.")

    while True:
        matricula = input("Matrícula: ")
        if validar_matricula(matricula, alunos):
            break
        print("A matrícula é inválida ou já existente.")

    notas = []
    for i in range(3):
        while True:
            nota = input(f"Nota {i+1}: ")
            try:
                nota = float(nota)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve ser entre 0 e 10")
            except:
                print("Digite um número válido")

    aluno = criar_aluno(nome, idade, matricula, notas)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!!\n")



def listar_alunos(alunos):
    print("\n--- LISTA DE ALUNOS ---")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
        return

    for i, a in enumerate(alunos, 1):
        media = sum(a["notas"]) / len(a["notas"])
        print(f"{i} - {a['nome']} | Matrícula: {a['matricula']} | Média: {media:.2f}")
    print()



def buscar_aluno(alunos):
    print("\n--- BUSCAR ALUNO ---")
    mat = input("Digite a matrícula: ")

    for a in alunos:
        if a["matricula"] == mat:
            media = sum(a["notas"]) / len(a["notas"])
            print("\nAluno encontrado:")
            print(f"Nome: {a['nome']}")
            print(f"Idade: {a['idade']}")
            print(f"Matrícula: {a['matricula']}")
            print(f"Notas: {a['notas']}")
            print(f"Média: {media:.2f}\n")
            return

    print("Aluno não encontrado.\n")



def remover_aluno(alunos):
    print("\n--- REMOVER ALUNO ---")
    mat = input("Matrícula: ")

    for i, a in enumerate(alunos):
        if a["matricula"] == mat:
            del alunos[i]
            print("Aluno removido com sucesso!\n")
            return

    print("Aluno não encontrado.\n")


# ----------- MENU -----------
def menu():
    print("""
========== SISTEMA DE CADASTRO ==========
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Remover aluno
0 - Sair
========================================
""")


# ----------- PROGRAMA PRINCIPAL -----------
def sistema():
    alunos = []

    while True:
        menu()
        op = input("Escolha: ")

        if op == "1":
            cadastrar_aluno(alunos)
        elif op == "2":
            listar_alunos(alunos)
        elif op == "3":
            buscar_aluno(alunos)
        elif op == "4":
            remover_aluno(alunos)
        elif op == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!\n")


# ----------- EXECUÇÃO -----------
sistema()

