"""
Nombre: Daniel Felipe Moncada Tello
ID: 8976528
Curso: ADA
Fecha: 30/07/2025
"""

from sys import stdin

def busquedaBinaria(high, low, listaMillas, dias):

    while (high - low) > 0:
        mid = low + ((high - low) // 2)
        
        distanciaRecorrida = 0
        diasQuePasan = 1
        i = 0
        while i < len(listaMillas) and diasQuePasan <= dias:
            diasFaltantes = dias - diasQuePasan
            millasFaltantes = len(listaMillas) - i

            if distanciaRecorrida + listaMillas[i] > mid or millasFaltantes == diasFaltantes:
                diasQuePasan += 1
                distanciaRecorrida = listaMillas[i]
            else:
                distanciaRecorrida += listaMillas[i]

            i += 1

        if diasQuePasan > dias:
            low = mid + 1
        else:
            high = mid


    distanciaRecorrida = 0
    diasQuePasan = 1
    caminosTomaos = []
    i = 0
    while i < len(listaMillas):
        diasFaltantes = dias - diasQuePasan
        millasFaltantes = len(listaMillas) - i

        if distanciaRecorrida + listaMillas[i] > high or millasFaltantes == diasFaltantes:
            caminosTomaos.append(distanciaRecorrida)
            diasQuePasan += 1
            distanciaRecorrida = listaMillas[i]
        else:
            distanciaRecorrida += listaMillas[i]
        
        i += 1
    caminosTomaos.append(distanciaRecorrida)

    return high, caminosTomaos


def main():

    casos = int(stdin.readline())
    i = 0
    while(i < casos):
        nCampsites, nNights = list(map(int, stdin.readline().split()))
        listaMillas = []

        sumaDeMillas = 0
        millaMayor = 0

        while(nCampsites >= 0):
            m = int(stdin.readline())
            listaMillas.append(m)

            sumaDeMillas += m
            if m > millaMayor:
                millaMayor = m

            nCampsites -= 1

        ans, caminosTomaos = busquedaBinaria(sumaDeMillas, millaMayor, listaMillas, nNights+1)
        
        i += 1
        print("Case %d: %d" % (i, ans))
        j = 0
        while j < len(caminosTomaos):
            print(caminosTomaos[j])
            j += 1
        
main()