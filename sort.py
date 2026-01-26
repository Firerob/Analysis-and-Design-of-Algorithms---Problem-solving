from sys import stdin

def sortsitoRandi(i, estadito, lista, memoriaPapa):
    ans = 0

    if estadito in memoriaPapa:
        ans = memoriaPapa[estadito]

    else:
        i = 0
       

        memoriaPapa[estadito] = ans

    return ans


def main():

    n = int(stdin.readline().strip())
    while n != 0:

        lista = list(map(int, stdin.readline().strip().split()))

        estadoInicial = ()
        memoriaPapa = {}

        i = 0
        ans = sortsitoRandi(i, estadoInicial, lista, memoriaPapa)


        n = int(stdin.readline().strip())


main()