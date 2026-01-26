# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 26/08/25

from sys import stdin

def criptocoder(i, estadito, M, A, B, memoriaPapa):
    ans = 0

    indiceA = estadito[1]
    indiceB = estadito[2]

    if estadito in memoriaPapa:
        ans = memoriaPapa[estadito]
    else:
        if i == len(M) and indiceA == 0 and indiceB == 0:
            ans += 1

        else:   
            if i < len(M) and indiceA < len(A) and indiceB < len(B):
            
                if M[i] == A[indiceA]:
                    if indiceA + 1 == len(A):
                        newEstadito = (i+1, 0, indiceB)
                    else:
                        newEstadito = (i+1, indiceA+1, indiceB)
                    ans += criptocoder(i+1, newEstadito, M, A, B, memoriaPapa)

            
                if M[i] == B[indiceB]:
                    if indiceB + 1 == len(B):
                        newEstadito = (i+1, indiceA, 0)
                    else:    
                        newEstadito = (i+1, indiceA, indiceB+1)
                    ans += criptocoder(i+1, newEstadito, M, A, B, memoriaPapa)

        memoriaPapa[estadito] = ans

    return ans

def main():

    linea = stdin.readline().strip()
    while linea != "":
        M, A, B = linea.split()

        i = 0
        estadoInicial = (0, 0, 0)
        memoriaPapa = {}
        ans = criptocoder(i, estadoInicial, M, A, B, memoriaPapa)

        print(ans % 1010101)

        linea = stdin.readline().strip()
    
main()