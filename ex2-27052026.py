"""
2.Faça um programa em Python que leia dois números inteiros
quaisquer para as variáveis A e B, efetue a troca dos valores
de forma que A passe a armazenar o valor de B e que B
passe armazenar o valor de A e que imprima os valores
trocados.
"""

#Solicitando valores
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

#Imprimindo valores recebidos
print(f"A é {a}")
print(f"B é {b}")

#Invertendo valores das variáveis
a, b = b,a
print("Invertendo os valores...")

#Imprimindo a inversão
print(f"A agora é {a}")
print(f"B agora é {b}")