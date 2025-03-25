#1bissexto
ano = int(input("Digite um ano: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("É bissexto")
else:
    print("Não é bissexto")


#2imc
peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Baixo Peso")

elif imc >= 18.5 and imc <= 24.9:
    print("Normal")

elif imc >= 25 and imc <= 29.9:
    print("Sobre peso")

elif imc >= 30 and imc <= 34.9:
    print("Obesidade")

elif imc >= 35 and imc <= 39.9:
    print("Obesidade Mórbida")

elif imc > 40:
    print("Obesidade Mórbida")

else:
    print("Seu peso está abaixo do esperado")


#produto
produto = int(input("Digite a quantidade de produtos a ser adquirido: "))
valor = float(input("Digite o preço de cada unidade: "))

if produto > 100:
    print("Você ganhou desconto de 10%")

elif produto < 100:
    print("Você ganhou desconto de 5%")

print(valor)

if produto > 100:
    condicao1= valor * 0.9
    print(f"Você pagará o total de {condicao1} ao final de sua compra")

elif produto < 100:
    condicao2 = valor * 0.5
    print(f"Você pagará o total de {condicao2} ao final de sua compra")

#4eleitor

idade = int(input("Insira sua idade: "))
if idade < 18:
    print("Não eleitor")

elif 18 <= idade <= 69:
    print("Voto obrigatório")

else:
    print("Voto facultativo")

#5idade

idade1 = int(input("Digite sua idade:"))
idade2 = int(input("Digite outra idade:"))
idade3 = int(input("Digite outra idade:"))

maior = idade1
if idade2 > idade1 and idade2 > idade3:
    maior = idade2

if idade3 > idade1 and idade3 >= idade2:
    maior = idade3

menor = idade1
if idade2 < idade3 and idade2 < idade1:
    menor = idade2

if idade3 <= idade2 and idade3 < idade1:
    menor = idade3

print(f"A menor idade é: {menor}")
print(f"A maior idade é: {maior}")


6 Verificação de Hora Válida. Peça que o usuário digite a hora, os minutos e os segundos.
Verifique se todos os números estão nos intervalos corretos 
(exemplo: a hora deve ser maior ou igual a zero e menor que 24). Exiba se a hora é válida ou inválida.
hora = int(input("Digite a hora (0-23): "))
minuto = int(input("Digite os minutos (0-59): "))
segundo = int(input("Digite os segundos (0-59): "))

if 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60:
    print("A hora é válida!")
else:
    print("A hora é inválida!")



7) Conversão de Nota em Letra. Receba a nota da prova do usuário e converta em letra conforme a tabela abaixo.
Caso o usuário digite nota menor que 0 ou maior que 10, digite nota inválida.

nota = int(input("Digite sua nota: "))

if nota >= 9 and nota < 10:
    print("A")

elif nota >= 7 and nota < 9:
    print("B")

elif nota >= 5 and nota < 7:
    print("C")

elif nota >= 3 and nota < 5:
    print("D")

elif nota >= 0 and nota < 3:
    print("E")

else:
    print("Nota fora do intervalo")

#8quadrado ou retangulo??

lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))
lado4 = float(input("Digite o valor do lado 4: "))

if lado1 == lado2 == lado3 == lado4:
    print("É um quadrado!")
elif (lado1 == lado3 and lado2 == lado4) or (lado1 == lado2 and lado3 == lado4):
    print("É um retângulo!")
else:
    print("Não é nem quadrado nem retângulo. O que será???")

#9 Calculadora Simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Divisão por zero não é permitida!")

else:
    print("Operação inválida!")


#10 descarte de notas
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

menor_nota = min(nota1, nota2, nota3)

media = (nota1 + nota2 + nota3 - menor_nota) / 2

print(f"A média das duas maiores notas é: {media:.2f}")


import random

print("Jogo de Adivinhação - Você tem 2 chances para acertar o número!")
numero = random.randint(1, 10)

chance1 = int(input("Insira um número (1 a 10): "))
resultado = ""

if chance1 == numero:
    resultado = "Parabéns! Você acertou de primeira!"
else:
    if chance1 > numero:
        print("O número é menor!")
    else:
        print("O número é maior!")

    chance2 = int(input("Sua última tentativa. Insira o número: "))
    if chance2 == numero:
        resultado = "Parabéns! Você acertou!"
    elif chance2 > numero:
        resultado = "Você errou! O número era menor!"
    else:
        resultado = "Você errou! O número era maior!"

print(f"{resultado}\nO número era: {numero}")
