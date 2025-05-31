import random
import string

maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
caracteres_especiais = string.punctuation

while True:
    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado para a senha. Mínimo 4 caracteres: "))
            if comprimento < 4:
                print("A senha precisa ter no mínimo 4 caracteres.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")

    senha = []
    senha.append(random.choice(maiusculas))
    senha.append(random.choice(minusculas))
    senha.append(random.choice(numeros))
    senha.append(random.choice(caracteres_especiais))

    todos_caracteres = maiusculas + minusculas + numeros + caracteres_especiais
    while len(senha) < comprimento:
        senha.append(random.choice(todos_caracteres))

    random.shuffle(senha)

    senha_final = ''.join(senha)

    print("Sua senha é:", senha_final)

    continuar = input("Deseja gerar outra senha? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa")
        break