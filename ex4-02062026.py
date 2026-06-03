while True:
#Solicitando entrada de notas
  p1 = float(input("Informe a nota da prova 1: "))
  p2 = float(input("Informe a nota da prova 2: "))
  t1 = float(input("Informe a nota do trabalho 1: "))
  t2 = float(input("Informe a nota do trabalho 2: "))

#Apresentando notas
  print(f"\nNota da prova 1: {p1:.2f}")
  print(f"Nota da prova 2: {p2:.2f}")
  print(f"Nota do trabalho 1: {t1:.2f}")
  print(f"Nota do trabalho 2: {t2:.2f}")

#Calculando média final
  media_provas = (p1 + p2) / 2
  media_trabalhos = (t1 + t2) / 2
  media_final = (0.8 * media_provas) + (0.2 * media_trabalhos)

#Apresentando processamento do cálculo
  print("\nCalculando resultado...")

#Aplicando condições de aprovação
  if media_final >= 6.0:
    print("\nAprovado!")
  else:
    print("\nReprovado!")
