from random import randint

rand = randint(1, 9)
print("Bem vindo, ao jogo de advinhação!!!\nIremos sortear um número de 1 até 9\nSera que você consegue advinhar?\n")
num = int(input("Advinhe o número: "))
if num == rand:
    print("\n\nParabéns!!! Você ganhou!")
elif 1 <= num <= 9:
    print(f"\n\nVocê perdeu!! que pena.\nO número correto era {rand}.")
else:
    print("Você digitou alguma coisa errada. Tente novamente.")

