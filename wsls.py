# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 24/08/25

from sys import stdin
import sys

sys.setrecursionlimit(100000)


def creadorDeEstadito(i, proxMov, jugadasP2):
    
    estadito = None
    puntos = 0
    proxResult = None
    if (proxMov == 'R' and jugadasP2[i] == 'S') or (proxMov == 'S' and jugadasP2[i] == 'P') or (proxMov == 'P' and jugadasP2[i] == 'R'):
            proxResult = 'G'
            puntos += 1
    elif (jugadasP2[i] == 'R' and proxMov == 'S') or (jugadasP2[i] == 'S' and proxMov == 'P') or (jugadasP2[i] == 'P' and proxMov == 'R'):
            proxResult = 'P'
            puntos -= 1

    else:
        proxResult = 'E'

    estadito = (i+1, proxResult, proxMov, jugadasP2[i])
    
    return estadito, puntos 


def janKenPon(estadito, i, memoriaPapa, jugadasP2, probaPrPpPs):

    resultadoProb = 0
    puntos = 0

    if estadito in memoriaPapa:
        resultadoProb = memoriaPapa[estadito]

    else:
        if i < len(jugadasP2): 

            if estadito[1] == 'E':
                
                proxMov = 'R'
                newEstadito, puntos = creadorDeEstadito(i, proxMov, jugadasP2)
                resultadoProb += (probaPrPpPs[0]/100) * (puntos + janKenPon(newEstadito, i+1, memoriaPapa, jugadasP2, probaPrPpPs))

                proxMov = 'P'
                newEstadito, puntos = creadorDeEstadito(i, proxMov, jugadasP2)
                resultadoProb += (probaPrPpPs[1]/100) * (puntos + janKenPon(newEstadito, i+1, memoriaPapa, jugadasP2, probaPrPpPs))

                proxMov = 'S'
                newEstadito, puntos = creadorDeEstadito(i, proxMov, jugadasP2)
                resultadoProb += (probaPrPpPs[2]/100) * (puntos + janKenPon(newEstadito, i+1, memoriaPapa, jugadasP2, probaPrPpPs))

            else:
                proxMov = None

                if estadito[1] == 'G':

                    if estadito[2] == 'R':
                        proxMov = 'P'
                    elif estadito[2] == 'P':
                        proxMov = 'S'
                    else:
                        proxMov = 'R'

                else:

                    if estadito[3] == 'R':
                        proxMov = 'P'
                    elif estadito[3] == 'P':
                        proxMov = 'S'
                    else:
                        proxMov = 'R'
                

                newEstadito, puntos = creadorDeEstadito(i, proxMov, jugadasP2)

                resultadoProb += puntos + janKenPon(newEstadito, i+1, memoriaPapa, jugadasP2, probaPrPpPs)


    memoriaPapa[estadito] = resultadoProb

    return resultadoProb


def normalito(jugadasP1, jugadasP2):
    
    resultado = 0
    
    i = 0
    while i < len(jugadasP1):

        auxP1 = jugadasP1[i]
        auxP2 = jugadasP2[i]

        if (auxP1 == 'R' and auxP2 == 'S') or (auxP1 == 'S' and auxP2 == 'P') or (auxP1 == 'P' and auxP2 == 'R'):
            resultado += 1

        elif (auxP2 == 'R' and auxP1 == 'S') or (auxP2 == 'S' and auxP1 == 'P') or (auxP2 == 'P' and auxP1 == 'R'):
            resultado -= 1

        i += 1

    return resultado


def main():

    x = 0
    casos = int(stdin.readline().strip())
    while x < casos:
        
        jugadasP1 = stdin.readline().strip()

        jugadasP2 = stdin.readline().strip()

        probaPrPpPs = list(map(int, stdin.readline().strip().split()))

        i = 0
        memoriaPapa = {}
        estadoInicial = (i, 'E', None, None)

        xResult = normalito(jugadasP1, jugadasP2)
        yResult = janKenPon(estadoInicial, i, memoriaPapa, jugadasP2, probaPrPpPs)

        zResult = 'N'

        if xResult < yResult:
            zResult = 'Y'


        print("%d %.4f %s" % (xResult, yResult, zResult))


        x += 1

main()