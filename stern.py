"""
Nombre: Daniel Felipe Moncada Tello
ID: 8976528
Curso: ADA
Fecha: 13/09/2025
"""

from sys import stdin

def busquedaBinaria(numerador, denominador):
    ans = []

    # x
    # -
    # y

    lowX = 0
    lowY = 1
    
    highX = 1
    highY = 0
    
    midX = lowX + highX 
    midY = lowY + highY

    while (numerador * midY) != (denominador * midX):

        if (numerador * midY) < (denominador * midX):
            ans.append("L")
            highX = midX
            highY = midY

        else:
            ans.append("R")
            lowX = midX
            lowY = midY

        midX = lowX + highX 
        midY = lowY + highY
    

    return "".join(ans)


def main():

    linea = stdin.readline().strip()
    flag = True

    while linea != "" and flag == True:

        numerador, denominador = map(int, linea.split())

        if numerador == 1 and denominador == 1:
            ans = "I"
            flag = False
            
        else:
            ans = busquedaBinaria(numerador, denominador)
            
            print(ans)
            
        
        linea = stdin.readline().strip()

main()