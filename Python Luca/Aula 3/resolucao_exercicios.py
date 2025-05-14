print("Imprimir os números de 1 a 5:")

numero = range(1,6)
for number in numero:
    print(number)
#==============================================================
print("Calcular a média de uma lista de números")
lista = [1,2,3,4,5]

soma = 0
for item in lista:
    soma = soma + item

media = soma / len(lista)
print(media)
#==============================================================
print("Imprimir cada caractere de uma string em uma linha separada:")
word = "example"
for caracter in word:
    print(caracter)
#===============================================================
print("Verificar se um número é primo")
num = int(input("Digite um número: "))

primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print(num, "é primo")

else:
    print("não é primo")
#===============================================================
print("Criar uma lista com o quadrado de cada número em outra lista:")
numeros = [1,2,3,4,5]
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2) #numero vezes ele mesmo.
print(quadrados)
#================================================================
