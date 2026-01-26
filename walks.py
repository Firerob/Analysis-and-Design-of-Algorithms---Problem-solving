# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 14/10/25

from sys import stdin


def DFS(grafito, nodito, longitudR, camino, nodosCamino):
    global flagNoCamino

    nodosCamino.add(nodito)

    if len(camino) == longitudR + 1:
        print("(", end="")
        print(",".join(map(str, camino)), end="")
        print(")")

        flagNoCamino = True

    else:
        for vNodito in grafito[nodito]:
            if vNodito not in nodosCamino:
                camino.append(vNodito+1)
                DFS(grafito, vNodito, longitudR, camino, nodosCamino)
                
                camino.pop()
                nodosCamino.remove(vNodito)

def main():

    flag = "-9999"
    primeraIter = True

    while flag == "-9999":

        if primeraIter == False:
            print()
        primeraIter = False

        linea = stdin.readline().strip()
        nNoditos, longitudR = map(int, linea.split())

        matriz = []
        i = 0
        while i < nNoditos:
            fila = list(map(int, stdin.readline().strip().split()))
            matriz.append(fila)

            i += 1

        grafito = [[] for _ in range(nNoditos)]

        i = 0
        while i < nNoditos:
            j = 0
            while j < nNoditos:

                if matriz[i][j] == 1:
                    grafito[i].append(j)
                    

                j += 1

            i += 1 

        camino = [1]
        nodosCamino = set()

        global flagNoCamino 
        flagNoCamino = False
        
        #print(grafito)

        DFS(grafito, 0, longitudR, camino, nodosCamino)


        if flagNoCamino == False:
            print("no walk of length %d" % (longitudR))


        flag = stdin.readline().strip()

main()