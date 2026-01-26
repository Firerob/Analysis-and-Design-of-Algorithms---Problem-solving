# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 28/08/25

from sys import stdin

def busquedaBinaria(auxI, lista):

    high = len(lista)
    low = 0

    while (high - low) > 0:
        mid = low + ((high - low) // 2)

        if lista[mid] < auxI:
            low = mid + 1
        
        else:
            high = mid


    return low


def sacaConjuntos(N, hilitos, funcionSecuencia):
    ans = 0
    listaResult = []
    listaResult.append(hilitos[0][1])

    i = 0
    while i < N:
        auxI = hilitos[i][1] * funcionSecuencia
        nuevaPos = busquedaBinaria(auxI, listaResult)
        
        if nuevaPos < len(listaResult):
            listaResult[nuevaPos] = auxI

        else:
            listaResult.append(auxI)
        
        i += 1

    ans = len(listaResult)

    return ans


def main():

    N = int(stdin.readline().strip())

    while N != 0:

        hilosSuperior = list(map(int, stdin.readline().strip().split()))
        hilosInferior = list(map(int, stdin.readline().strip().split()))
        
        hilitos = []

        i = 0
        while i < N:
            hilitos.append((hilosSuperior[i], hilosInferior[i]))

            i += 1

        hilitos.sort()

        ans1 = sacaConjuntos(N, hilitos, 1)
        ans2 = sacaConjuntos(N, hilitos, -1)

        print("%d %d" % (ans1, ans2))


        N = int(stdin.readline().strip())

main()