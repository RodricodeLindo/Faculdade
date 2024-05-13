num = int(input("Digite um número: "))
resul = float(0)
y = int(1)
for x in range(num):
    x+=1
    resul += x/y
    if x == 1:
        print(f"{x}/{y}", end="")
    else:
        print(f" + {x}/{y}", end="")
    y+=2
print(f" = {resul:.3f}")

