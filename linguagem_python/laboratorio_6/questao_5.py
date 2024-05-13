notas = []
media = float(0)
for x in range(5):
    notas.append(float(input("Qual nota do aluno: ")))
    media+=notas[x]
media/=5
for x in notas:
    print(x, media)
    if x<float(media):
        notas.remove(x)
print(f"A média dos 5 alunos foi {media}, e as notas igual ou acima da media são: {notas}")

