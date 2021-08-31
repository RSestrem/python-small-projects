from models.client import Cliente
from models.account import Conta

john: Cliente = Cliente(
    'John Doe', 'john@doe.com', '123.456.789-00', '01/01/1980'
)

dummy: Cliente = Cliente(
    'Crash Dummy', 'crash@dummy.com', '987.654.321-99', '31/12/1985'
)

contaj: Conta = Conta(john)
contad: Conta = Conta(dummy)
