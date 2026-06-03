"""
1. O custo ao consumidor de um carro novo é a soma do custo
de fábrica com a porcentagem do distribuidor e dos impostos
(aplicados ao custo de fábrica). Supondo que a porcentagem
do distribuidor seja de 12% do preço de fábrica e os impostos
de 30% do preço de fábrica, fazer um programa em Python
para ler o custo de fábrica de um carro e imprimir o custo ao
consumidor.
"""

custo_fabrica = float(input("Insira o valor do preço de fabrica: ")) 
distribuidor = 0.12 * custo_fabrica
impostos = 0.30 * custo_fabrica
custo_consumidor = custo_fabrica + distribuidor + impostos

print(f"Custo de fábrica: {custo_fabrica}")
print(f"Distribuidor: {distribuidor}")
print(f"Impostos: {impostos}")
print(f"Custo ao consumidor: {custo_consumidor}")

