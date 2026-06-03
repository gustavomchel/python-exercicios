"""
● Crie um programa que simule o funcionamento de um caixa
eletrônico. O usuário inicia com um saldo fictício e pode
realizar as seguintes operações através de um menu iterativo:
1.Consultar saldo
2.Depositar dinheiro
3.Sacar dinheiro
4.Sair
● O programa deve repetir o menu até o usuário escolher a
opção 4 (sair).
"""
 
#Criando saldo
saldo = 0.0
#Criando apresentação do menu // prints
print("=== Bem-vindo ao Caixa Eletrônico ===")

while True:
  print("\n[ MENU ]")
  print("1 - Consultar Saldo")
  print("2 - Depositar Dinheiro")
  print("3 - Sacar Dinheiro")
  print("4 - Sair")
#Criando solicitação de opção // input
  opcao = input("\nEscolha uma opção: ")
#Criando estruturas de controle: while(repetição), if/elif/else(condicional), break(controle de fluxo)
  if opcao == "1":
    print(f"\nSaldo atual: R$ {saldo:.2f}")
  elif opcao == "2":
    valor = float(input("Valor a depositar: "))
    if valor > 0:
      saldo += valor
    else:
      print("\nValor inválido. Digite um valor positivo!")
  elif opcao == "3": 
    valor = float(input("\nValor a sacar: "))
    if valor <= 0: 
      print("Valor inválido. Digite um valor positivo!")
    elif valor > saldo:
      print("\nSaldo insulficiente para o saque!")
    else:
      saldo -= valor
      print(f"Saque de {valor:.2f} realizado com sucesso!")
      print(f"Saldo disponível: {saldo:.2f}")
  elif opcao == "4":
    print("\nObrigado por usar nosso sistema. Até logo!")
    break
  else:
    print("\nOpção inválida. Tente novamente!")


