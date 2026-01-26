# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 22/09/25

from sys import stdin

def profundidadArbolito(nodito, grafito, profundidad, listaProfundidades):
    
    listaProfundidades[nodito] = (profundidad, nodito)
    
    for vNodito in grafito[nodito]:
        profundidadArbolito(vNodito, grafito, profundidad + 1, listaProfundidades)


def DFS(nodito, grafito, visitados, longitudCaminos, flagCont):
   
    flagCamino = False
    
    if flagCont + 1 == longitudCaminos:
        flagCamino = True

    else:
        for vNodito in grafito[nodito]:
            if not visitados[vNodito]:
                flagCamino = DFS(vNodito, grafito, visitados, longitudCaminos, flagCont + 1)
            
            
    if flagCamino == True:
        visitados[nodito] = True

    return flagCamino


def pintaArbolitos(grafitoTrans, longitudCaminos, listaProfundidades):
    ans = 0
    
    visitados = [False for _ in range(len(grafitoTrans))]
    flagCamino = False

    i = 0
    while i < len(listaProfundidades):
        nodito = listaProfundidades[i][1]
        contador = 0
        
        if not visitados[nodito]:
            
            visitados[nodito] = True
            flagCamino = DFS(nodito, grafitoTrans, visitados, longitudCaminos, contador)
            
            if flagCamino == True:
                ans += 1
        i += 1
    
    return ans


def main():

    linea = stdin.readline().strip()
    
    while linea != "":

        nNoditos, mLineas, longitudCaminos = map(int, linea.split())
        grafito = [[] for _ in range(nNoditos)]
        grafitoTrans =[[] for _ in range(nNoditos)]
        indegrees = [0 for _ in range(nNoditos)]
        
        longitudCaminos += 1

        i = 0
        while i < mLineas:

            listaNodos = list(map(int, stdin.readline().split()))

            j = 1
            while j < len(listaNodos):

                A = listaNodos[0]
                B = listaNodos[j]

                grafito[A].append(B)
                indegrees[B] += 1

                grafitoTrans[B].append(A)

                j +=1

            i += 1

        noditoRaiz = None
        i = 0
        while i < len(indegrees):

            if indegrees[i] == 0:
                noditoRaiz = i

            i += 1

        listaProfundidades = [-1 for _ in range(nNoditos)]
        profundidadArbolito(noditoRaiz, grafito, 0, listaProfundidades)
       
        listaProfundidades.sort(reverse=True)

        ans = pintaArbolitos(grafitoTrans, longitudCaminos, listaProfundidades)

        print(ans)

        linea = stdin.readline().strip()

main()