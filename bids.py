from sys import stdin

def busquedaBinaria(listaPROD, listaCONS, v):

    genteEnojaa = 0

    listaPROD.sort()
    listaCONS.sort()

    h1 = len(listaPROD)
    l1 = 0
    h2 = len(listaCONS)
    l2 = 0

    while (h1 - l1) > 0:
        m1 = l1 + ((h1 - l1) // 2)
        if (v >= listaPROD[m1]):
            l1= m1+ 1

        else:
            h1 = m1

    while (h2 - l2) > 0:
        m2 = l2 + ((h2 - l2) // 2)
        if (v < listaCONS[m2]):
            h2 = m2

        else:
            l2 = m2 + 1

    genteEnojaa = (len(listaPROD) - l1) + h2


    return v, genteEnojaa


def main():

    casos = int(stdin.readline())

    while(casos > 0):
        nProd, nCons = list(map(int, stdin.readline().split()))

        listaPROD = list(map(int, stdin.readline().split()))
        listaCONS = list(map(int, stdin.readline().split()))
        listaTODOS = listaPROD + listaCONS
        listaTODOS.append(0)
        listaTODOS.sort()
        
        menorCantEnojaos = len(listaTODOS)
        precioIdeal = 0

        i = 0   
        while i < len(listaTODOS):
            v = listaTODOS[i]
            precioMinimo, genteEnojaa = busquedaBinaria(listaPROD, listaCONS, v)
            if (genteEnojaa < menorCantEnojaos):
                menorCantEnojaos = genteEnojaa
                precioIdeal = precioMinimo

            i += 1

        print("%d %d" % (precioIdeal, menorCantEnojaos))

        casos -= 1

main()