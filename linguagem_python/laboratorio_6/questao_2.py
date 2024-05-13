from math import ceil

presta = [*range(1, 11)]
resul = []
cont = int(0)
num = int(input("Digite um numero: "))

while num<1 or num>10:
    num = int(input("porfavor digite um nemro de 1 a 10: "))
for x in range(ceil(len(presta)/num)):
    resul.append([])
for x in resul:
    for y in range(num):
        x.append(presta[cont])
        cont+=1
        if cont>=len(presta):
            break
print(f"\nlista:\t{resul}\n")

