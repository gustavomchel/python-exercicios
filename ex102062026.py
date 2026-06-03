nome = input("Digite seu nome: ")
nota1 = float(input("Digita a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media= (nota1 + nota2 + nota3) / 3

print(f"Aluno: {nome}")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")

print("Calculando a média final...")
print(f"Média: {media:.2f}")


