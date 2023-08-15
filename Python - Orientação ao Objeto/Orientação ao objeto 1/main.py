from conta import Conta
from cliente import Cliente

conta1 = Conta(123, 'Lucas', 500, 1000)
conta2 = Conta(321, 'João', 1000, 1000)

conta1.Extrato()
conta1.Saca(1600)
conta1.Extrato()
