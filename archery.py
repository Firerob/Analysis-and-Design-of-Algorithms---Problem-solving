# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 25/10/25

from sys import stdin

def reinaArquera(nCasito, puntajeS, listaPuntajes, valorAcum, listaResult):
    global flagPosible
    global resultados
    
    if flagPosible != True:
        if valorAcum == puntajeS:
            
            resultados.append(listaResult[:])
            flagPosible = True

        
        else:
            x = len(listaPuntajes) - 1
            while x >= 0:
                
                newValorAcum = valorAcum + listaPuntajes[x]

                if newValorAcum <= puntajeS:
                    listaResult.append(listaPuntajes[x])

                    reinaArquera(nCasito, puntajeS, listaPuntajes, newValorAcum, listaResult)

                    listaResult.pop()
                
                x -= 1


def main():

    nCasos = int(stdin.readline().strip())
    x = 0
    while x < nCasos:
        linea = stdin.readline().strip()
        nElementos, puntajeS = map(int, linea.split())
        listaPuntajes = list(map(int, stdin.readline().split()))

        listaResult = []
        global resultados
        resultados = []

        global flagPosible
        flagPosible = False

        i = len(listaPuntajes) - 1
        while i >= 0:
            
            flagPosible = False

            listaResult.append(listaPuntajes[i])
            reinaArquera(x, puntajeS, listaPuntajes, listaPuntajes[i], listaResult)
            listaResult.pop()

            i -= 1

        x += 1

        if len(resultados) == 0:
            print("Case %d: impossible" % (x))
        
        else:
            listaResult = min(resultados, key=len)
            print("Case %d: [%d] " % (x, len(listaResult)), end="")
            i = 0
            while i < len(listaResult):
                if i == len(listaResult) - 1:
                    print(listaResult[i])
                else:
                    print(listaResult[i], end=" ")

                i += 1
    
main()