num = int(input("Digite um número: "))
ltr = str(num)[:-2]
ltr += str(num)[-1:-3:-1]
resul = int(ltr)
print(resul)

