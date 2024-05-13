print("Eleição Presidencial")
print("\n1 - Capitão chupeta\n2 - Lula Molusco\n3 - Presidente Padre\n4 - Mr. Walter Blanco\n5 - Voto nulo\n6 - Voto em branco\n0 - Terminar votação")

total = pres1 = pres2 = pres3 = pres4 = bran = nulo = int(0)

while 1:
    x = int(input(": "))
    if x == 1:
        pres1 += 1
        total += 1
    elif x == 2:
        pres2 += 1
        total += 1
    elif x == 3:
        pres3 += 1
        total += 1
    elif x == 4:
        pres4 += 1
        total += 1
    elif x == 5:
        bran += 1
        total += 1
    elif x == 6:
        nulo += 1
        total += 1
    elif x == 0:
        print(f"\n\nVotos em Capitão chupeta: {pres1}\n")
        print(f"Votos em Lula Molusco: {pres2}\n")
        print(f"Votos Presidente Padre: {pres3}\n")
        print(f"Votos Mr. Walter Blanco: {pres4}\n\n")
        print(f"Votos em branco: {bran}\n")
        print(f"Votos em nulo: {nulo}\n\n")
        print(f"Tivemos {(bran/total)*100:.2f}% de votos branco e {(nulo/total)*100:.2f}% de votos nulo.\n")
        break
    else:
        print("Resposta inválida!")

