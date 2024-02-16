import textwrap   

def menu():
    menu = """\n
    ================ MENU ================
    [1] \tDepositar
    [2] \tSacar
    [3] \tExtrato
    [4] \tNova conta
    [5] \tListar contas
    [6] \tNovo usuario
    [7] \tSair
    ->"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("Operacao falhou! O valor informado e invalido.")

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
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n====================== EXTRATO ======================")
    print("Nao foram realizadas movimentacoes." if not extrato else extrato)
    print(f"\nSaldo total: R$ {saldo:.2f}")
    print("======================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente os numeros!): ")



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("DIgite o valor que quer depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == "7":
            print("Saindo do sistema....")
            break
        
        else:
            print("Operacao invalida, por favor selecione novamente a operacao desejada.")

main()