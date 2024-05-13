num = int(input("Digite um numero: "))
num1 = 0
num2 = 1
num3 = 0
x = 0

if num == 1:
    print("1.")
elif num == 2:
    print("1, 2.")
elif num > 2:
    print("0, 1", end='')
    num-=2
    for x in range(num):
        num3 = num1+num2
        num1 = num2
        num2 = num3
        print(f", {num3}", end='')
        x+=1
    print(".")
else:
    print("Por favor digite um número válido.")

