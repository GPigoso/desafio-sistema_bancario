menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("DIgite o valor que quer depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operacao falhou! O valor informado e invalido.")
       

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if numero_saques > LIMITE_SAQUES -1:
            print("Operacao falhou! Excedeu o numero de saques diarios.")

        elif valor_saque > 0 and valor_saque <= limite :
            if valor_saque <= saldo:

                numero_saques += 1
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"

            else:
                print(f"Saldo insuficiente para fazer o saque! Saldo disponivel R$ {saldo:.2f}.")

        else:
                print("Operacao falhou! O valor informado e invalido.")

    elif opcao == "e":
        print("\n====================== EXTRATO ======================")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo total: R$ {saldo:.2f}")
        print("======================================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")