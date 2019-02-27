class Conta:
    '''Representa uma conta bancária'''

    def __init__(self, numero, titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0
        self.__limite = 0

    def valor_valido(self, valor):
        '''Verifica se o valor informado é válido'''
        return valor > 0

    def __pode_sacar(self, valor):
        '''Verifica se é possivel realizar o saque do valor'''
        if self.valor_valido(valor):
            return valor <= self.saldo + self.limite

    def sacar(self, valor):
        '''Realiza o saque na conta'''
        if self.__pode_sacar(valor):
            self.__saldo -= valor

    def depositar(self, valor):
        '''Deposita um valor na conta'''
        self.__saldo += valor

    def transferir(self, valor, conta_destino):
        '''Transfere um valor de uma conta para outra'''
        if self.__pode_sacar(valor):
            self.sacar(valor)
            conta_destino.depositar(valor)

    def emitir_extrato(self):
        #TODO: Criar lógica para modelo de extrato
        pass

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
