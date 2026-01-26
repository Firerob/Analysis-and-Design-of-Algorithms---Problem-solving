# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 23/08/25

from sys import stdin


def guitarritaaa(inicio, maxlevel, listaVolumenes):
    vol = -1

    tablita = [{} for _ in range(len(listaVolumenes) + 1)]
    tablita[0][inicio] = inicio

    i = 0
    while i < len(listaVolumenes):
        x = 0
        for estadito in tablita[i]:
            auxResta = estadito - listaVolumenes[i]

            if auxResta >= 0:
                tablita[i+1][auxResta] = auxResta

            auxSuma = estadito + listaVolumenes[i]
            if auxSuma <= maxlevel:
                tablita[i+1][auxSuma] = auxSuma

            x += 1
        
        i += 1

    ultimosEstados = tablita[len(listaVolumenes)]

    i = 0
    for estado in ultimosEstados:
        if estado > vol:
            vol = estado

        i += 1

    return vol


def main():

    casos = int(stdin.readline().strip())
    x = 0
    while x < casos:

        maxlevel = int(stdin.readline().strip())
        inicio = int(stdin.readline().strip())
        listaVolumenes = list(map(int, stdin.readline().strip().split()))


        voluFinal = guitarritaaa(inicio, maxlevel, listaVolumenes)

        print(voluFinal)

        x += 1

main()