num = input('Digite um numero positivo: ')
numeros = []
soma = 0
mult = 1
for i in range(0, len(num)):
    soma += int(num[i])
    mult = mult * int(num[i])

print(soma, mult)

RA = 3011392323022