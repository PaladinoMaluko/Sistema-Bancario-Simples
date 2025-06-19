menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
lista_de_saques = []
lista_de_depositos = []


def depositar(valor:float) -> None:
    global saldo
    if valor > 0:
        saldo += valor
        lista_de_depositos.append(valor)
        print("Deposito efetuado com sucesso.")
        return
    
    print("Valor invalido.")
    

def saque(valor:float) -> None:
    global saldo, numero_saques
    if (valor < 500) and (valor <= saldo) and (numero_saques < LIMITE_SAQUES):
        saldo -= valor
        lista_de_saques.append(valor)
        numero_saques += 1
        print("Saque efetuado com sucesso.")
        return
    
    if valor >= 500:
        print("Limite ultrapassado, tente outro valor.")
        return
    
    if valor > saldo:
        print("Saldo insuficiente.")
        return
    
    if numero_saques >= LIMITE_SAQUES:
        print("numero de saques atingido.")
        return

def extrato():
    if lista_de_saques or lista_de_depositos:
        print("\n================ EXTRATO ================")
        print(f"\nSaldo: R$ {saldo:.2f}")
        
        if lista_de_saques:
            print("Saques efetuados:")
            for i in lista_de_saques:
                print(f"-R$ {i:.2f}")

        if lista_de_depositos:
            print("Depositos efetuados:")
            for j in lista_de_depositos:
                print(f"+R$ {j:.2f}")
                
        print("\n==========================================")
    else:
        print("Não foram realizadas movimentações.")


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saque(valor)
    elif opcao == "e":
        extrato()
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")