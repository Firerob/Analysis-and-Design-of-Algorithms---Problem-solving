# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 9/08/25

# Codigo solucion guiado por Profesor Camilo Rocha :D

from sys import stdin

def hadamardRecursiva(n, fila, columna):
    
    matrizAns = None

    if n == 1: 
        matrizAns = 1

    else:
        m = n >> 1

        if 0 <= fila < m and 0 <= columna < m: 
            matrizAns = hadamardRecursiva(m, fila, columna)

        elif 0 <= fila < m and m <= columna < n: 
            matrizAns = hadamardRecursiva(m, fila, columna - m)

        elif m <= fila < n and 0 <= columna < m: 
            matrizAns = hadamardRecursiva(m, fila - m, columna)

        else: 
            matrizAns = -hadamardRecursiva(m, fila - m, columna - m)

    return matrizAns


def armadorDeMatriz(n, x, y, w, h):
    
    matrizAns = list()

    for fila in range(y, y + h):
        matrizAns.append(list())

        for columna in range(x, x + w):
            matrizAns[-1].append(hadamardRecursiva(n, fila, columna))

    return matrizAns


def main():
    
    casitos = int(stdin.readline())
    
    while casitos != 0:
        n, x, y, w, h = map(int, stdin.readline().split())
        matrizAns = armadorDeMatriz(n, x, y, w, h)

        for x in matrizAns: 
            print(' '.join(map(str, x)))
        
        print()
        casitos -= 1

main()