from bancoDelas import  ContaEspecial
from cliente import Cliente
from contaComun import ContaComun
##############################################################################################################

print('Insira:\n Nome do cliente \n Telefone \n Renda  \n Sexo(0 para feminino e 1 para masculino).')
print('Ainda é necessário fazer as validações para os valores inseridos para o atributo sexo')
print(100*'=')

print('INSTANCIAR CONTA ESPECIAL (MULHERES)')
cliente = ContaEspecial('Andressa', '3223-2222', 2000)

print(cliente.deposito(1000))
print(cliente.deposito(1000))
print(cliente.saldo)

print('')

print(cliente.saque(1000))
print(cliente.saldo)
print(cliente.saque(3000))
print(cliente.saldo)


print('')

print('INSTANCIAR CONTA COMUM (Homens)')
conta = ContaComun('Aderson', '3223-2222', 2500)
print(conta)
print(conta.deposito(100))
print(conta.saque(100))
print(conta.saque(100))








