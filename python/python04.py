def prime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False

    return True

primeSum = 0
numbers = range(2,1000)

for n in numbers:
    if prime(n):
        print(n)
        primeSum += n

#isso é muito ineficiente...
print(primeSum)
