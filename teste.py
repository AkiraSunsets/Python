'''
1)

ano = int(input("Digite um ano: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("É bissexto")
else:
    print("Não é bissexto")


2)

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



idade = int(input("Insira sua idade: "))
if idade < 18:
    print("Não eleitor")

elif 18 <= idade <= 69:
    print("Voto obrigatório")

else:
    print("Voto facultativo")



idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))

if idade1 > idade2 > idade3




hora = float(input("Digite a hora, minutos e segundos: "))
if hora
    print("Hora Válida")

elif hora
    print("Hora Inválida")


'''


