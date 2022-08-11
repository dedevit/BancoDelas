#Cliente: 0 = feminino e cliente = 1 masculino. Falta colocar validações par essa variavel para retornar o erro.
from random import randint
from datetime import datetime


class ContaBanco:
   """
    Cria a super classe Conta banco que sera a base para as classes conta epecial e Conta comum.
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

   """
    O metodo saque utiliza o atributo sexo e valor do saque 
    No caso das mulheres  a condicional define  o atributo sexo for igual a zero e o saldo maior oi igual ao saque
     ou valor do saque for menor ou igual ao limite da conta  (limite = renda) ele realiza as operações.Caso
     contrario retorna saldo insuficiente

     Para atributo sexo = 1(homens) a condição é somente para saldo maior ou igual ao valor do saque
   """
   def saque(self,valor_saque):
    
      if ((self.sexo == 0) and (self.saldo >= valor_saque or valor_saque <= self.limite )):
         self.saldo -= valor_saque
         saldo_atual = self.saldo
         self.saldo = saldo_atual
         self.especial = 'Conta especial'
         data =datetime.now()
         return f'Tipo conta: {self.especial}. Saque de R${valor_saque}.\nSaldo tual da conta até {data} é de :R${self.saldo}'

      if (self.sexo == 1 and self.saldo >= valor_saque):
         print("Cliente não possui conta especial")
         self.saldo -= valor_saque
         saldo_atual = self.saldo
         self.especial = 'Conta comum'
         data =datetime.now()
         return f'Tipo conta: {self.especial}. Saldo da conta até {data} é de :R${saldo_atual}'

      return 'Saldo insuficiente'
   
   def __str__(self):
      return f'Titular: {self.nome },Telefone: {self.telefone}, Renda mensal R${self.renda}, Gênero:{self.sexo},Nº da conta:{self.numero_conta} '

#Cliente: 0 = feminino e cliente = 1 masculino. Falta colocar validações par essa variavel para retornar o erro.

class ContaEspecial (ContaBanco):

   def __init__(self, nome, telefone, renda_mensal):
      super().__init__(nome, telefone, renda_mensal,0 )
      self.titular = nome
      

class ContaComun(ContaBanco):  
    def __init__(self, nome, telefone, renda_mensal):
      super().__init__(nome, telefone, renda_mensal,1 )
      self.titular = nome
     


       
