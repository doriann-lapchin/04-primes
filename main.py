"""
Ce programmme traite des nombres premiers

"""
from math import sqrt

#### Fonction secondaire


def isprime(p):

    """
    Détermine si un nombre est premier.

    """
    if p < 2:
        return False
    for divisor in range(2, int(sqrt(p)) + 1):
        if p % divisor == 0:
            return False
    return True
#### Fonction principale

def main():
    """
    Fonction main

    """

    isprime(17)
    isprime(145007)
    isprime(90)
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
