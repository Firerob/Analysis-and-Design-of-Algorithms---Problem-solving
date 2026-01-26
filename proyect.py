# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 27/10/25

from sys import stdin
from heapq import heappush,heappop

def zlatanElMejor(sumaAmbas, nMisiones, promObjetivo):
    conjuntosMisiones = [0 for _ in range(nMisiones)]
    tamMisiones = [0 for _ in range(nMisiones)]

    auxAcum = 0
    x = 0
    i = 0
    while i < len(sumaAmbas) and x < nMisiones:

        auxAcum = conjuntosMisiones[x]
        nuevoTam = tamMisiones[x] + 1 
        nuevoAcum = (auxAcum + sumaAmbas[i]) * (nuevoTam - 1)

        if nuevoAcum <= promObjetivo:
            tamMisiones[x] = nuevoTam
            conjuntosMisiones[x] = auxAcum + sumaAmbas[i]
            
        else:
            x += 1
            if x < nMisiones:
                tamMisiones[x] = 1
                conjuntosMisiones[x] = sumaAmbas[i]   
        i += 1     
    
    ans = 0

    if i < len(sumaAmbas) or x >= nMisiones:
        
        flagLimite =  False

    else:
        flagLimite = True

        i = 0  
        while i < len(conjuntosMisiones):
            ans += conjuntosMisiones[i] * (tamMisiones[i] - 1)
            i += 1

    return flagLimite, ans


def biseccion(sumaAmbas, nMisiones, promObjetivo):
    low = promObjetivo // nMisiones
    high = promObjetivo * (len(sumaAmbas))

    resultados = []

    while high > low:
        
        mid = low + ((high - low) // 2)
        flagLimite, ans = zlatanElMejor(sumaAmbas, nMisiones, mid)

        if flagLimite == True:
            high = mid - 1
            resultados.append(ans)

        else:
            low = mid + 1

    print(min(resultados))


def dijkstra(grafito, noditoInicial):
    INF = float('inf')
    dist = [INF for _ in range(len(grafito))]
    dist[noditoInicial] = 0

    pred = [-1 for _ in range(len(grafito))]
    colita = list()
    
    heappush(colita, (dist[noditoInicial], noditoInicial))

    while len(colita)!=0:
        peso, nodito = heappop(colita)
        if dist[nodito] == peso:
            for vNodito, pesoVecino in grafito[nodito]:
                if peso + pesoVecino < dist[vNodito]:
                    dist[vNodito] = peso + pesoVecino
                    pred[vNodito] = nodito
                    heappush(colita, (dist[vNodito], vNodito))
    return dist


def main():

    linea = stdin.readline().strip()
    
    while linea != "":
        nIntersec, nBases, nMisiones, nHiperRutas = map(int, linea.split())

        grafito = [[] for _ in range(nIntersec)]
        grafitoTrans = [[] for _ in range(nIntersec)]

        i = 0
        while i < nHiperRutas:

            A, B, distViaje = map(int, stdin.readline().split())
            A -= 1
            B -= 1
            grafito[A].append((B, distViaje))
            grafitoTrans[B].append((A, distViaje))
            
            i += 1

        if nBases != nMisiones:
            basesAHQ = dijkstra(grafitoTrans, nBases)
            centralABases = dijkstra(grafito, nBases)
            sumaAmbas = [0 for _ in range(nBases)]

            promObjetivo = 0

            i = 0
            while i < nBases:
                auxSuma = basesAHQ[i] + centralABases[i]
                sumaAmbas[i] = auxSuma
                promObjetivo += auxSuma

                i += 1

            sumaAmbas.sort()

            biseccion(sumaAmbas, nMisiones, promObjetivo)
        
        else:
            print(0)
        
    
        linea = stdin.readline().strip()

main()