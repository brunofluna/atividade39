from modulo import *
import os
# Completem o programa: o usuário vai informar o nome e o CPF, e o programa informa qual a agência, conta e saldo. E ai o usuário vai poder escolher se deseja fazer saque, depósito ou sair do programa.

if __name__ == '__main__':
    cc = ContaCorrente("", '', '1001-1', '10010-1', 0)

    cc.nome = input('Digite o nome do titular: ')
    cc.cpf = input('Digite o CPF do titular: ')

    print(f'Nome: {cc.nome}.')
    print(f'CPF: {cc.cpf}.')
    print(f'Agência: {cc.agencia}.')
    print(f'Conta: {cc.conta}.')

    while True:
        cc.exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')
        match opcao:
            case '0':
                print('CONSULTAR SALDO\n')
                print(f'Saldo disponível R$ {cc.consultar_saldo():,.2f}.')
            case '1':
                valor = str(input('Valor do saque: R$ '))
                valor = float(valor.replace(',', '.'))
                if valor < cc.saldo:
                    cc.saldo = cc.fazer_saque(valor)
                    print('Saque efetuado!')
                    print(f'Saldo atual: {cc.saldo:,.2f} ')
                else:
                    print('Não foi possivel efetuar o saque!')
                    continue
            case '2':
                valor = str(input('Valor do depósito: '))
                valor = float(valor.replace(',', '.'))
                saldo = cc.fazer_deposito(valor)
                print('Depósito efetuado com sucesso.')
                print(f'Saldo atual: R$ {saldo:,.2f}')
                continue
            case '3':
                break
            case _:
                print('Opção inválida!')
                continue
