prima = [1,2,3,4]
secun = [1,3]
aux1 = []
aux2 = []
resul = []

if len(prima) > len(secun):
    aux1 = prima.copy()
    aux2 = secun.copy()
else:
    aux1 = secun.copy()
    aux2 = prima.copy()
aux1.sort()
aux2.sort()
for x in aux1:
    for y in aux2:
        if x == y:
            aux1.remove(y)
print(f"\n{aux1}\n")

