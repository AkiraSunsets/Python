print("Exercicio 1")



#------------------------------------------------
print("Exercicio 3")

idade = int(input("Digite a sua idade: \n"))


if idade < 13:
    print("Criança")

elif idade < 18:
    print("Adolescente")

elif idade < 60:
    print("Adulto")

elif idade >= 60:
    print("Idoso")

else:
    print("")
#--------------------------------------------------
print("Exercicio4")


#--------------------------------------------------
print("Exercicio 5")
nota1 = int(input("Digite a primeira nota: \n"))
nota2 = int(input("Digite a segunda nota: \n"))
nota3 = int(input("Digite a terceira nota: \n"))
media = nota1 + nota2 + nota3 / 3

if media >= 7 and media < 10:
    print("Aprovado!")

elif media >= 6 and media < 4:
    print("Recuperação!")

elif media >= 4 and media < 0:
    print("Reprovado!")

else:
    print("Nota fora do intervalo!")
#-------------------------------------------------
print("Desafio 2: ")

ano = int(input("Digite um ano: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("É bissexto")
else:
    print("Não é bissexto")
#-------------------------------------------------



print("Anotações!!!")
numero = 10
if numero > 0:
    print("O número é positivo")


senha = 145

if senha == 145: #comparação
    print("Senha correta")

else:
    print("Senha incorreta")
#------------------------------------------------------
frase = "Olá, mundo!"
print(frase[-2])

frase = "Olá, mundoo!"
print(frase[0:3])

frase = "Olá, mundoo!"
print(frase[0::3])

frase = "python"

print(frase.upper()) # maiusculo

print(frase.lower()) #minusculo

print(frase.title()) #primeira letra maiúscula
#-----------------------------------------------------
nome = input("Digite o nome do personagem: \n")

cor_de_cabelo = input("Digite a cor do cabelo do seu personagem: \n")

cor_de_pele = input("Digite a cor da pele do seu personagem: \n")

classe = input("Selecione a classe do seu personagem: Guerreiro, Mago ou Arqueiro: \n")

idade = int(input("Digite a idade do seu personagem: \n"))

altura = float(input("Digite a altura do seu personagem: \n"))

habilidade = input("Digite a habilidade do seu personagem: \n")

print(f"O nome do seu personagem é {nome}, ele(a) possui cabelos {cor_de_cabelo} claros e pele {cor_de_pele}. Pertence a classe {classe}, tem {idade} anos, tem {altura} de altura e possui {habilidade} como habilidade")

#----------------------------------------------------------------
nome = "Mark"
print(nome)

frase = "Eu sou o seu pai"
print(frase[::-1])

filme = "Avatar"
print(f"A maior bilheteria de 2009 foi {filme}")

numero1 = 10
dado = int(input("Digite o número que deseja: \n"))
print(numero1 * dado)

#--------------------------------------------------------------------
