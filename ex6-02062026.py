while True:
#Solicitando valor em reais
  valor_reais = float(input("Informe o valor em reais para conversão: "))

#Apresentando o menu de opções
  print("[ MENU ]")
  print("1 - Dólar")
  print("2 - Euro")
  print("3 - Libra")
  print("4 - Iene")

#Solicitando escolha do menu
  opcao_menu = input("Escolha uma opção do menu: ")
#Convertendo opções
  if opcao_menu == "1":
    dolar = valor_reais / 5.02
    print(f"Valor em dólares: US$ {dolar:.2f}")
  elif opcao_menu == "2":
    euro = valor_reais / 5.84
    print(f"Valor em euros: € {euro:.2f}")
  elif opcao_menu == "3":
    libra = valor_reais / 6.76
    print(f"Valor em libras: £ {libra:.2f}")
  elif opcao_menu == "4":
    iene = valor_reais / 0.031
    print(f"Valor em ienes: ¥ {iene:.2f}")
  else:
    print("Opção inválida. Por favor, digite uma opção válida!")
