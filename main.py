from bancoDelas import ContaBanco, ContaComun, ContaEspecial

##############################################################################################################
print('Insira:\n Nome do cliente \n Telefone \n Renda  \n Sexo(0 para feminino e 1 para masculino).')
print('Ainda é necessário fazer as validações para os valores inseridos para o atributo sexo')
print(100*'=')

print('INSTANCIAR CONTA ESPECIAL (MULHERES)')
cliente = ContaEspecial('Andressa', '3223-2222', 2000)
print('---------')
print(cliente.deposito(1000))
print('---------')
print(cliente.deposito(1000))
print('---------')
print(cliente.saldo)
print('')

print('---------')
print(cliente.saque(1000))
print(cliente.saldo)
print('---------')
print(cliente.saque(1000))
print(cliente.saldo)
print('---------')
print(cliente.saque(1000))
print(cliente.saldo)
print('---------')

print('')


"""
print('INSTANCIAR CONTA Comun (Homens)')
cliente = ContaComun('Aderson', '3223-2222', 2500)
print(cliente)
print(cliente.deposito(1000))
print(cliente.saque(1500))
print('')

"""


