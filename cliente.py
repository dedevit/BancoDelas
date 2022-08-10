#Cliente: 0 = feminino e cliente = 1 masculino. Falta colocar validações par essa variavel para retornar o erro.
from random import randint
from datetime import datetime

class Cliente:
   """
    Cria a super classe Cliente que sera a base para as classes conta epecial e Conta comum.
    Segundo requisito o limite da conta para mulheres sera igual a renda. O mesmo não vale para homens
    O atributo com especial foi inicializado comum e será modificado segundo o tipo de sexo(0,1) 
    O numero da conta é gerado aleatório com numeros entre 1 a 9999.
   """

   def __init__(self, nome, telefone, renda_mensal : float, sexo: int):  
     self.nome = nome
     self.telefone = telefone
     self.renda = renda_mensal
     self.sexo = sexo
     self.numero_conta = randint(1, 9999)
     self.limite = self.renda
     self.saldo = 0
     self.conta_especial = 'Conta Comum'

   def deposito(self,deposito):
      self.saldo += deposito
      saldo_total = self.saldo
      self.saldo = saldo_total
      data =datetime.now()
      return f'Deposito de R${deposito} .Saldo da conta até {data} é de :R${self.saldo}'


   def __str__(self):
      return f'Titular: {self.nome },Telefone: {self.telefone}, Renda mensal R${self.renda}, Gênero:{self.sexo},Nº da conta:{self.numero_conta} '