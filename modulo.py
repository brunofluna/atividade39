# importa biblioteco para criação das classes abstratas
from abc import ABC, abstractmethod

# classe abstrata que irá funcionar como uma interface
class Conta(ABC):
    # interface só possui métodos
    @abstractmethod
    def consultar_saldo(self):
        ... # ou o comando pass
    
    @abstractmethod
    def fazer_deposito(self):
        pass

    @abstractmethod
    def fazer_saque(self):
        ...

# subclasse conta correte
class ContaCorrente(Conta):
    # atributos
    def __init__(self, nome, cpf, agencia, conta, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
    
    #getter
    @property
    def nome(self):
        return self.__nome    
    @property
    def cpf(self):
        return self.__cpf
    @property
    def agencia(self):
        return self.__agencia
    @property
    def conta(self):
        return self.__conta
    @property
    def saldo(self):
        return self.__saldo
    
    # setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    @conta.setter
    def conta(self, conta):
        self.__conta = conta
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    

    # metodos da classe abstrata
    def consultar_saldo(self):
        return self.__saldo
    
    def fazer_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def fazer_saque(self, valor):
        self.__saldo -= valor
        return self.__saldo
    
    def exibir_menu(self):
        print('\nOPÇÕES\n')
        print('1 - Fazer saque.')
        print('2 - Fazer depósito.')
        print('3 - Sair.')

