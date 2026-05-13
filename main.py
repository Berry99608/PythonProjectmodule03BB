import math

print( math.sqrt(34) )


def somme_chiffres(n):
    if n < 10:
        return n
    return n % 10 + somme_chiffres(n // 10)
print(somme_chiffres(1234))
print(somme_chiffres(123))
print('salut')
print('oui OUI')
