y = float(0)

print('/'*5,"Lojas Rodrigão",'\\'*5)
while y > -1:
    y = x = 1
    soma = tro = float(0)
    while y > 0: 
        y = float(input(f"Produto {x}: R$ "))
        if y > 0:
            soma += y
            x+=1
    while tro < soma and y > -1:
        print(f"Total: R$ {soma:.2f}")
        tro = float(input("Dinheiro: R$ "))
        if tro < soma:
            print("valor insuficiente!")
        elif tro >= soma:
            print(f"Troco: R$ {tro-soma:.2f}")
print("Fim do programa")

