num = int(input("Digite a quantidade de vezes no qual deseja digitar: "))
menor = int(0)
maior = int(0)
atua = int(0)

for x in range(num):
    x+=1
    atua = int(input(f"digite um numero: "))
    if maior+menor == 0:
        maior = menor = atua
    else:
        if atua >= maior:
            maior = atua
        if atua <= menor:
            menor = atua
    print(x)
print(f"\nNúmero maior: {maior}\nNúmero menor: {menor}")

