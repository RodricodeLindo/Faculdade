num = char = str('')
while num == '' or char == '':
    num = char = str('')
    strin = str(input("Digite: ")).replace(' ', '')
    for x in range(len(strin)):
        if strin[x].isnumeric():
            num += strin[x]
        elif strin[x].isalpha():
            char += strin[x]
        x+=1
    if num == '':
        print("Você tem que digitar ao menos um número!")
    if char == '':
        print("Você tem que digitar ao menos uma letra!")
print(f"Caracteres: {char}\n\nNúmeros: {num}")

