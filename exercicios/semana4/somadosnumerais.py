#Receba um número com várias casas e realize a soma dos numerais do mesmo#

numero = int(input("Digite um número bem grande e descubra a soma das suas casas: "))
soma = 0

while numero != 0:
    soma = soma + numero % 10
    numero = numero // 10

print(soma)
