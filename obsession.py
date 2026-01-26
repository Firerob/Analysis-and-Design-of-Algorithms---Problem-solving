# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 20/09/25

from heapq import heappush,heappop
from sys import stdin

def dijkstra(grafito, noditoInicial, noditoFinal):
    
    dist = {}

    estadoInicial = (noditoInicial, 0)
    dist[estadoInicial] = 0
    pqueue = list()
    estadoFinal = -1
    flag = False

    heappush(pqueue, (dist[estadoInicial], estadoInicial))
    
    while len(pqueue) != 0 and flag == False:
        
        valorPeaje, estadito = heappop(pqueue)
        nodito, carreterasCruzadas = estadito

        if (nodito == noditoFinal) and (carreterasCruzadas == 0):
            estadoFinal = (noditoFinal, carreterasCruzadas)
            flag = True

        else:
            
            if dist[estadito] == valorPeaje:
                
                for vNodito, vecinoValorPeaje in grafito[nodito]:  
                    
                    newEstadito = (vNodito, 1 - carreterasCruzadas)
                    if (newEstadito not in dist) or ((valorPeaje + vecinoValorPeaje) < dist[newEstadito]):
                        
                        dist[newEstadito] = valorPeaje + vecinoValorPeaje
                        heappush(pqueue, (dist[newEstadito], newEstadito))

    if estadoFinal == -1:
        ans = -1

    else:
        ans = dist[estadoFinal] 
                         

    return ans


def main():
    
    linea = stdin.readline().strip()
    

    while linea != "":


        nCiudades, nCaminos = map(int, linea.split())
        grafito = [[] for _ in range(nCiudades)]

        i = 0
        while i < nCaminos:
            A, B, valorPeaje = map(int, stdin.readline().split())
            A -= 1
            B -= 1
            grafito[A].append((B, valorPeaje))
            grafito[B].append((A, valorPeaje))

            i += 1

        ans = dijkstra(grafito, 0, nCiudades-1)

        print(ans)

        linea = stdin.readline().strip()


main()