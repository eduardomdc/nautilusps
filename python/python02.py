print("Insire as notas separadas por espaços")
notas1 = input("Lista de notas da primeira prova:")
notas2 = input("Lista de notas da segunda prova:")
notas3 = input("Lista de notas da terceira prova:")

def convertToFloatList(notas):
    notas = notas.split()
    for i in range(len(notas)):
            notas[i] = float(notas[i])
    return notas

notas1 = convertToFloatList(notas1)
notas2 = convertToFloatList(notas2)
notas3 = convertToFloatList(notas3)

for i in range(len(notas1)):
    media = (notas1[i]+notas2[i]+notas3[i])/3
    if media >= 7:
        print("Aluno "+str(i)+" aprovado.")
    else:
        print("Aluno "+str(i)+" reprovado.")
