"""
Nombre: Daniel Felipe Moncada Tello
ID: 8976528
Curso: ADA
Fecha: 28/07/2025
"""

from sys import stdin
import math

def fisicaPapa(listaTODOS, mid, posicionesDer):
    listaTODOSposTempo = []
    i = 0
    while i < len(listaTODOS):

        coord = listaTODOS[i][0]
        vel = listaTODOS[i][1]
        posxtempo = coord + vel * mid
        listaTODOSposTempo.append((posxtempo, vel))
        
        i += 1

    listaTODOSposTempo.sort()

    i = 0
    ans = False
    while i < len(posicionesDer):
        posAUX = posicionesDer[i]
        #HUBO CHOQUE PAPAAAAAAAAAAAAAA PARA UN POCOOOO
        if listaTODOSposTempo[posAUX][1] < 0:
            ans = True
        i += 1


    return ans

EPS = 1e-17
def biseccion(listaTODOS, low, high, posicionesDer):
    cont = 0
    while abs(high - low) > EPS and cont < 100:
        mid = low + ((high - low) / 2)
        
        d = fisicaPapa(listaTODOS, mid, posicionesDer)

        if d == True:
            high = mid
        else:
            low = mid
        cont += 1

    print(f"{high:.20f}")


def main():

    nCasitos = stdin.readline().strip()
    while(nCasitos != ""):
        nCasitos = int(nCasitos)

        listaIZQ = []
        listaDER = []
        listaTODOS = []
        posicionesDer = []

        i = 0
        while(i < nCasitos):
            coord, vel = list(map(int, stdin.readline().split()))
            
            if vel < 0:
                listaIZQ.append((coord, vel))
            else:
                listaDER.append((coord, vel))
                posicionesDer.append(i)
            
            listaTODOS.append((coord, vel))

            i += 1

        if len(listaIZQ) == 0 or len(listaDER) == 0:
            print("-1")
        
        elif listaIZQ[-1][0] < listaDER[0][0]:
            print("-1")

        else:
            low = 0
            high = (listaIZQ[-1][0] - listaDER[0][0])/(abs(listaIZQ[-1][1]) + listaDER[0][1])

            biseccion(listaTODOS, low, high, posicionesDer)
            
    
        nCasitos = stdin.readline().strip()
        
main()
