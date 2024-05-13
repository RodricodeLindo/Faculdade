from random import randint

num = str("a")
rand = randint(1, 9)
print("Bem vindo, ao jogo de advinhação!!!\nIremos sortear um número de 1 até 9\nSera que você consegue advinhar?\n")
while not num.isnumeric():
    num = str(input("Advinhe o número: ")).strip()
    if not num.isnumeric():
        print("Você precisa advinhar um NÚMERO!!!!!")
    elif 1 > int(num) or int(num) > 9:
        print("Digite um número de 1 até 9!")
        num = str("a")
if int(num) == rand:
    print("\n\nParabéns!!! Você ganhou!")
elif 1 <= int(num) <= 9:
    print(f"\n\nVocê perdeu!! que pena.\nO número correto era {rand}.")
else:
    print("Você digitou alguma coisa errada. Tente novamente.")

