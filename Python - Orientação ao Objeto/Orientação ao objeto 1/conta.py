class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto ...')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def Extrato(self):
        print(
            f'Titular da conta: {self.__titular} \nSaldo: R${self.__saldo:.2f}')

    def Deposita(self, valor):
        self.__saldo += valor

    def Saca(self, valor):
        if (self.__PodeSacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite!')

    def __PodeSacar(self, valor):
        valor_disponivel = (self.__saldo + self.__limite)
        return valor <= valor_disponivel

    def Transferir(self, destino, valor):
        self.Saca(valor)
        destino.Deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def CodigoBanco():
        return '001'

    @staticmethod
    def CodigosBancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
