#Cliente: 0 = feminino e cliente = 1 masculino. Falta colocar validações par essa variavel para retornar o erro.
from random import randint
from datetime import datetime
from cliente import Cliente

"""
    O metodo saque utiliza o atributo sexo e valor do saque 
    No caso das mulheres(banco delas, classe conta especial)  a condicional define  o atributo sexo for igual a zero e o saldo maior oi igual ao saque
     ou valor do saque for menor ou igual ao limite da conta  (limite = renda) ele realiza as operações.Caso
     contrario retorna saldo insuficiente

     Para atributo sexo = 1(homens, Arquivo conta comum, classe conta comum) a condição é somente para saldo maior ou igual ao valor do saque
"""

class ContaEspecial (Cliente):

   def __init__(self, nome, telefone, renda_mensal):
      super().__init__(nome, telefone, renda_mensal,sexo = 0 )
      self.titular = nome

   def saque(self,valor_saque):
      if (self.sexo == 0 and self.saldo >= valor_saque or valor_saque <= self.limite ):
         self.saldo -= valor_saque
         saldo_atual = self.saldo
         self.saldo = saldo_atual
         self.especial = 'Conta especial'
         data =datetime.now()
         return f'Tipo conta: {self.especial}. Saque de R${valor_saque}.\nSaldo tual da conta até {data} é de :R${self.saldo}'
      else:
         return 'Saldo insuficiente'


       