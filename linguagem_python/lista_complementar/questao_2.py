num = int(input("Digite um numero: "))
nu = str()
cont = int
resul = int(0)

for cont in range(num):
    cont+=1
    nu+='2'
    resul+=int(nu)
    if cont==1:
        print("2", end='')
    else:
        print(f" + {nu}", end="")
print(f" = {resul}")

