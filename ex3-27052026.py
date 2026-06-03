"""
3.Faça um programa que peça o tamanho de um arquivo para
download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).
"""

#Solicitando o tamanho do arquivo e velocidade
tamanho_arquivo = float(input("Informe o tamanho de um arquivo em (Mb): "))
velocidade_link = float(input("Informe a velocidade de um link de internet em (Mbps): "))

#Convertendo a velocidade do link em Mbps
velocidade_mbps = velocidade_link / 8

#Convertendo a velocidade do link Mbps em segundos
tempo_segundos = tamanho_arquivo / velocidade_mbps

#Convertendo a velocidade do link Mbps em minutos
tempo_minutos = tempo_segundos / 60

print(f"O tempo de download é {tempo_segundos:.2f} segundos!")
print(f"O tempo de download é {tempo_minutos:.2f} minutos!")