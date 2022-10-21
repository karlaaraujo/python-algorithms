# Conta Bancária (Real Brasileiro)
import time

menu = """
-- Conta Bancária --

1. Consultar Saldo
2. Sacar
3. Depositar
4. Sair

- Escolha uma opção:
"""

saldo = 0.0

def realizarOperacao(idOperacao):
    match idOperacao:
        case 1:
            consultarSaldo()
        case 2:
            sacar()
        case 3:
            depositar()
        case other:
            print("Encerrando.")

def obterSaldoFormatado():
    return str(saldo).replace('.',',')

def mostrarMenuInicial():
    operacao = int(input(menu))

    realizarOperacao(operacao)

def sacar():
    valorSaque = float(input("Informe o valor do saque: R$ ").replace(',','.'))

    global saldo

    if saldo >= valorSaque:

        saldo-= valorSaque
        print(f"Saque realizado com sucesso. Saldo atual: R$ {obterSaldoFormatado()}")
    
    else:
        print("O saldo atual é menor que o valor de saque informado.")

    time.sleep(1.5)
    mostrarMenuInicial()

def consultarSaldo():
    print(f"\n Saldo atual: R$ {obterSaldoFormatado()}")

    time.sleep(1.5)
    mostrarMenuInicial()

def depositar():

    global saldo

    valorDeposito = float(input("Informe o valor de depósito: R$ ").replace(',','.'))

    saldo += valorDeposito

    print(f"Depósito realizado com sucesso. Saldo atual: R$ {obterSaldoFormatado()}")

    time.sleep(1.5)
    mostrarMenuInicial()

mostrarMenuInicial()