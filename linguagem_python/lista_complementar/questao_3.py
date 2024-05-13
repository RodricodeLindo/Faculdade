num = int(input("Digite um numero: "))
x = num
resul = num

print(f"{num}", end='')
for x in range(num, 1, -1):
    x-=1
    print(f" * {x}", end="")
    resul*=x
print(f" = {resul}")

