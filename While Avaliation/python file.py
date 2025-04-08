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

