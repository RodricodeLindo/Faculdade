strin = str(input("Digite: "))
num = char = str('')
for x in range(len(strin)):
    if strin[x].isnumeric():
        num += strin[x]
    elif strin[x].isalpha():
        char += strin[x]
    x+=1
print(f"Caracteres: {char}\n\nNúmeros: {num}")

