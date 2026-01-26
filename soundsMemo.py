# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 23/08/25
import sys
from sys import stdin

sys.setrecursionlimit(10**7)


def guitarritaaa(estadito, memoriaPapa, maxlevel, listaVolumenes, i):
    vol = -1

    if estadito in memoriaPapa:
        vol = memoriaPapa[estadito]

    else:
        if i == len(listaVolumenes): 
            vol = estadito[1]
        else:
            auxResta = estadito[1] - listaVolumenes[i]
            if auxResta >= 0:

                newEstadito = (i+1, auxResta)

                mejorVol = guitarritaaa(newEstadito, memoriaPapa, maxlevel, listaVolumenes, i+1)
                if mejorVol > vol:
                    vol = mejorVol


            auxSuma = estadito[1] + listaVolumenes[i]

            if auxSuma <= maxlevel:

                newEstadito = (i+1, auxSuma)

                mejorVol = guitarritaaa(newEstadito, memoriaPapa, maxlevel, listaVolumenes, i+1)
                if mejorVol > vol:
                    vol = mejorVol

        memoriaPapa[estadito] = vol

    return vol


def main():

    casos = int(stdin.readline().strip())
    x = 0
    while x < casos:

        maxlevel = int(stdin.readline().strip())
        inicio = int(stdin.readline().strip())
        listaVolumenes = list(map(int, stdin.readline().strip().split()))

        memoriaPapa = {}
        i = 0
        estadoInicial = (i, inicio)
        voluFinal = guitarritaaa(estadoInicial,memoriaPapa, maxlevel, listaVolumenes, i)

        print(voluFinal)

        x += 1

main()