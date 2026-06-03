while True:
  temp = float(input("Informe a temperatura de hoje: "))#Solcitando entrada de temperatura
  print(f"Temperatura informada: {temp:.2f}°C")
  if temp < 0:
    print("Estado: Frio extremo!")
  elif temp <= 10:
    print("Estado: Frio!")
  elif temp <= 25:
    print("Estado: Ameno!")
  elif temp <= 35:
    print("Estado: Quente!")
  else:
    print("Estado: Muito quente!")

    

