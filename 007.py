'''
lista = []
x = 4

while x <= 20:
    lista.extend(range(4, 22, 2))
    x += 1
    print(lista)
    break

'''
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
#correção:
numeros = list()
i = 4
while (i <= 20):
    numeros.append(i)
    i = i+2
print(numeros)