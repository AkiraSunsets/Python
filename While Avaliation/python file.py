#Peça 10 números e conte quantos são múltiplos de 3. Use for.
contador = 0
for num in range(10):
    int = input("Digite um número: \n")
    if num %3 == 0:
        contador += 1
        print("Multiplo de 3")
    else:
        print("Não é multiplo de 3")

print(f"A quantidade de números múltiplos de 3 é: {contador} ")
---------------------------------------------------------------------------------------------------------------------
#2) Crie um programa que simule o uso de senha com tentativas infinitas até digitar a senha correta (use while True).
senha_correta = "1234"

while True: #loop infinito até encontrar a senha correta.
    senha = input("Digite a senha: \n")

    if senha == senha_correta:
        print("Senha correta!")
        break  # encerra o loop quando a senha estiver correta.
    else:
        print("Senha incorreta, tente novamente.")
---------------------------------------------------------------------------------------------------------------------
#3)Monte um sistema que repita um menu até o usuário escolher sair. Use while e break.
opcao = 0

while opcao != 4:
    print("Menu: ")
    print("1 - opção 1")
    print("2 - opção 2")
    print("3 - opção 3")
    print("4 - sair")

    opcao = int(input("Escolha uma opção: \n"))

    if opcao == 1:
        print("Você escolheu a opção 1.")
    elif opcao == 2:
        print("Você escolheu a opção 2")
    elif opcao == 3:
        print("Você escolheu a opção 3")
    elif opcao == 4:
        print("Saindo...")
        break  # Encerra o loop quando a opção 4 é escolhida
    else:
        print("Opção inválida, tente novamente.")

----------------------------------------------------------------------------------------------
#5) O usuário tem 3 tentativas para acertar a senha.
# Se errar todas, o acesso é bloqueado. Use while.
senha = 1234
contador = 0

while contador < 3:
    senha_correta = int(input("Insira sua senha: "))
    if senha == senha_correta:
        print("Welcome!")
        break
    else:
        contador += 1
        if contador == 3:
            print("Acesso restrito")
            break
-----------------------------------------------------------------------------------------
#6#6) Peça 10 números e separe em duas listas: pares e ímpares. Mostre as duas no final.
for num in range(10):
    number = int(input("Digite um número: \n"))
    if number % 2 == 0:
       pares.append(number)
    else:
        impares.append(number)

print(f"lista de pares\n{pares}")
print(f"lista de pares\n{impares}")

#6) Peça 10 números e separe em duas listas: pares e ímpares. Mostre as duas no final.
# Inicializando as listas de pares e ímpares
pares = []
impares = []

# Laço para solicitar 10 números
for num in range(10):
    number = int(input("Digite um número: \n"))

    # Verifica se o número é par ou ímpar e adiciona na lista correspondente
    if number % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)

# Exibe as listas de números pares e ímpares
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")

#7) Peça uma frase e conte quantas vogais há nela.
# Mostre o total de cada uma (a, e, i, o, u).

frase = input("Digite uma frase: \n")
vogais = "aeiouAEIOU" #o que está sendo pedido
contador = 0 #contador de vogais

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase '{frase}' contém {contador} vogais")

#9) Crie um programa que leia uma sequência de números e
# determine quantos números são menores que a média.
num = []
size = int(input("Digite o tamanho da sequência: \n"))
for i in range(size):
    numero = int(input(f"Digite o {i+1}º número: "))
    num.append(numero)

menor = num[0]
for numero in num:
    if numero < menor:
        menor = numero

soma = sum(num)
media = soma / len(num)

print(f"O menor número é: {menor}")
print(f"A média é {media}")
