senha = str('t')
num = char = False

while 8 > len(senha) or len(senha) > 16 or not num or not char:
    num = char = False
    x = 0
    senha = str(input("Digite sua senha: ")).strip()
    while x < len(senha):
        if senha[x].isnumeric():
            num = True
        elif senha[x].isalpha():
            char = True
        if char and num:
            break
        x+=1
    if 8 > len(senha):
        print("Sua senha esta muito pequena, ela precisa ter pelo menos 8 digitos!")
    elif len(senha) > 16:
        print("Sua senha esta muito grande, ela só pode ter no maximo 16 digitos!")
    elif not num:
        print("Sua senha precisa ter pelo menos um número!")
    elif not char:
        print("Sua senha precisa ter pelo menos uma letra!")
print("Parabéns!! sua senha foi aceita!")

