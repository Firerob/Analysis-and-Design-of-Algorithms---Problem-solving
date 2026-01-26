"""
Nombre: Daniel Felipe Moncada Tello
ID: 8976528
Curso: ADA
Fecha: 13/09/2025
"""

from sys import stdin


def nibblerCagon(i, estadito, memoriaPapa, listaViajes):
    #este era mi error, como antes tenia la idea de hacerlo como una sumatoria tenia sentido
    #pero la duracion en el peor caso es n * ti, cuando no hay caquitas, naaaaaah
    duracionViaje = 100000
    viajesFaltantes = len(listaViajes) - i

    if estadito in memoriaPapa:
        duracionViaje = memoriaPapa[estadito]

    else:
        
        if i == len(listaViajes):
            duracionViaje = 0

        else:
            duracionPROX = listaViajes[i][0]
            caquitasPROX = listaViajes[i][1]

            caquitasDisponibles = estadito[1]
            
            # usar cacota
            if caquitasDisponibles > 0:
                newCaquitas = (caquitasDisponibles-1) + caquitasPROX

                if newCaquitas > viajesFaltantes:
                    newCaquitas = viajesFaltantes

                newEstadito = (i+1, newCaquitas)
                
                mejorDuracionViaje = ((duracionPROX//2) + nibblerCagon(i+1, newEstadito, memoriaPapa, listaViajes))
                if mejorDuracionViaje < duracionViaje:
                    duracionViaje = mejorDuracionViaje
                

            # no usar cacota
            newCaquitas = caquitasDisponibles + caquitasPROX

            if newCaquitas > viajesFaltantes:
                newCaquitas = viajesFaltantes

            newEstadito = (i+1, newCaquitas)

            mejorDuracionViaje = (duracionPROX + nibblerCagon(i+1, newEstadito, memoriaPapa, listaViajes))
            if mejorDuracionViaje < duracionViaje:
                duracionViaje = mejorDuracionViaje

            
        memoriaPapa[estadito] = duracionViaje


    return duracionViaje


def main():

    nViajes = int(stdin.readline().strip())
    while(nViajes != 0):
        
        listaViajes = []
        memoriaPapa = {}

        x = 0
        while(x < nViajes):
            duracion, caquitas = map(int, stdin.readline().strip().split())
            listaViajes.append((duracion, caquitas))
            
            x += 1

        i = 0

        estadoInicial = (i, 0)

        duracionTotal = nibblerCagon(i, estadoInicial, memoriaPapa, listaViajes)

        print(duracionTotal)
        

        nViajes = int(stdin.readline().strip())


main()