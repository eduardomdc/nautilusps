lista = range(1000)
pares = []
impares = []
for n in lista:
    if n % 2:
        pares.append(n)
    else:
        impares.append(n)

for i in range(500):
    print("Par: "+str(pares[i]))
    print("Impar: "+str(impares[i]))
