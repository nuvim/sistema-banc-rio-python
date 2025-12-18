import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [cc]\tConsultar cliente
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf_input = input("Informe o CPF (somente número): ")

    cpf = "".join(filter(str.isdigit, cpf_input)) # remove pontos e traços do numero de cpf

    usuario = filtrar_usuario(cpf, usuarios)

    if len(cpf) != 11: # validando o cpf pelo tamanho
        print("\n@@@ CPF inválido! O CPF deve conter 11 dígitos numéricos. @@@")
        return

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def buscar_conta (numero_conta, contas):
    for conta in contas:
        if conta["numero_conta"] == numero_conta: # verifica se o numero da conta bate
            return conta # retorna a conta se encontrada
    return None # retorna None se a conta não for encontrada

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def consultar_cliente(usuarios):
    cpf_input = input("Informe o CPF para busca: ")
    cpf = "".join(filter(str.isdigit, cpf_input)) # limpa o CPF igual da outra vez

    usuario_encontrado = filtrar_usuario(cpf, usuarios)

    if usuario_encontrado:
        print("\n" + "=" * 40) # imprime uma linha de separação
        print(f"Nome: {usuario_encontrado['nome']}")
        print(f"CPF: {usuario_encontrado['cpf']}")
        print(f"Data de Nascimento: {usuario_encontrado['data_nascimento']}")
        print(f"Endereço: {usuario_encontrado['endereco']}")
        print("=" * 40 + "\n") # imprime uma linha de separação
    else:
        print("\n@@@ Usuário não encontrado! @@@\n")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios) # procura o usuario pelo cpf dentro da lista de usuarios

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        
        return {
            "agencia": agencia, 
            "numero_conta": numero_conta, 
            "usuario": usuario,
            "saldo": 0.0,
            "extrato": "",
            "numero_saques": 0
            }

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            
            numero_conta = int(input("Informe o número da conta para depósito: "))
            conta = buscar_conta(numero_conta, contas)

            if conta:
                valor = float(input("Informe o valor do depósito: "))
                novo_saldo, novo_extrato = depositar(conta["saldo"], valor, conta["extrato"])

                conta["saldo"] = novo_saldo
                conta["extrato"] = novo_extrato
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "s":
            numero_conta = float(input("Informe o número da conta: "))
            conta = buscar_conta(numero_conta, contas) # busca a conta pelo numero, o buscar_conta retorna a conta ou None, numero_conta é o input do usuario e o contas é a lista de contas
            
            if conta:
                valor = float(input("Informe o valor do saque: "))
            
                novo_saldo, novo_extrato, novos_saques = sacar(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=500,
                    numero_saques=conta["numero_saques"],
                    limite_saques=LIMITE_SAQUES,
                )

                conta["saldo"] = novo_saldo
                conta["extrato"] = novo_extrato
                conta["numero_saques"] = novos_saques
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "e":
            numero_conta = float(input("Informe o número da conta: "))
            conta = buscar_conta(numero_conta, contas)

            if conta:
                exibir_extrato(conta["saldo"], extrato=conta["extrato"])
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            consultar_cliente(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()