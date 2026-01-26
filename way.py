# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 21/09/25

from sys import stdin
import heapq


def prim(noditoInicial, grafito):

    tamGrafito = len(grafito)
    distancias = [float("inf")] * tamGrafito
    padres = [-1] * tamGrafito
    cola = []
    visitado = [False] * tamGrafito
    aristasUsadas = []

    total = 0
    distancias[noditoInicial] = 0
    heapq.heappush(cola, (0, noditoInicial))

    while cola:
        peso, nodito = heapq.heappop(cola)
        if not visitado[nodito]:
           
            visitado[nodito] = True

            if peso == distancias[nodito]:
                total += peso

                if padres[nodito] != -1:
                    aristasUsadas.append((padres[nodito], nodito, peso))
                
                for vNodito, pesoVecino in grafito[nodito]:
                    if not visitado[vNodito] and pesoVecino < distancias[vNodito]:
                        padres[vNodito] = nodito
                        distancias[vNodito] = pesoVecino
                        heapq.heappush(cola, (distancias[vNodito], vNodito))

    i = 1
    flag = False
    while (i < len(visitado)) and (flag == False):
        if visitado[i] == False:
            flag = True
            total = "No way"
        
        i += 1

    return total, flag, aristasUsadas


def primOcultaAristas(noditoInicial, grafito, arista):
    A, B, pesoAocultar = arista
    tamGrafito = len(grafito)
    distancias = [float("inf")] * tamGrafito
    padres = [-1] * tamGrafito
    cola = []
    visitado = [False] * tamGrafito

    total = 0
    distancias[noditoInicial] = 0
    heapq.heappush(cola, (0, noditoInicial))

    while cola:
        peso, nodito = heapq.heappop(cola)
        if not visitado[nodito]:
           
            visitado[nodito] = True

            if peso == distancias[nodito]:
                total += peso
                
                for vNodito, pesoVecino in grafito[nodito]:
                    if not (nodito == A and vNodito == B and pesoVecino == pesoAocultar) or (nodito == B and vNodito == A and pesoVecino == pesoAocultar):
                        if not visitado[vNodito] and pesoVecino < distancias[vNodito]:
                            padres[vNodito] = nodito
                            distancias[vNodito] = pesoVecino
                            heapq.heappush(cola, (distancias[vNodito], vNodito))

    return total


def main():
    
    casos = int(stdin.readline().strip())
    x = 0
    while x < casos:

        nVecinos, nConexiones = map(int, stdin.readline().split())
        grafito = [[] for _ in range(nVecinos)]

        i = 0
        while i < nConexiones:
            A, B, peso = map(int, stdin.readline().split())

            A -= 1
            B -= 1

            grafito[A].append((B, peso))
            grafito[B].append((A, peso))

            i += 1


        ansNormalito, flag, aristasUsadas  = prim(0, grafito)

        if flag != True:
            
            mejorSegundaConexion = float("inf")
            i = 0
            while i < len(aristasUsadas):

                ansSegundo = primOcultaAristas(0, grafito, aristasUsadas[i])
                if ansSegundo < mejorSegundaConexion and ansSegundo >= ansNormalito:
                    mejorSegundaConexion = ansSegundo

                i += 1

            if mejorSegundaConexion == float("inf"):
                print("Case #%d : No second way" % (x+1))
            
            else:
                print("Case #%d : %d" % (x+1, mejorSegundaConexion))


        else:
                
            print("Case #%d : %s" % (x+1, ansNormalito)) 

        x += 1


main()
