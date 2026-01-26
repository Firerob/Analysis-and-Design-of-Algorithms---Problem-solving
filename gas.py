# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 25/10/25

from sys import stdin

def estacionesVoracin(listaXi, listaXf, longitud, nEstaciones):
    contador = 0
    flagPosible = True

    xfSeleccionao = 0

    j = 0
    while xfSeleccionao < longitud and flagPosible == True:
        intervalosACompetir = []

        while j < len(listaXi) and listaXi[j] <= xfSeleccionao:
            intervalosACompetir.append((listaXf[j]))

            j += 1

        if len(intervalosACompetir) > 0:
            xfSeleccionao = max(intervalosACompetir)
            contador += 1
        else:
            flagPosible = False


    if flagPosible == False:
        print(-1)
    else:
        print(nEstaciones - contador)


def main():

    linea = stdin.readline().strip()
    longitud, nEstaciones = map(int, linea.split())

    while longitud != 0 and nEstaciones != 0:
        
        listaEstaciones = []
        listaXi = []
        listaXf = []

        i = 0
        while i < nEstaciones:
            posicion, radio = map(int, stdin.readline().split())
            
            posXi = posicion - radio
            posXf = posicion + radio

            if (posXi <= longitud and posXf >= 0):
                listaEstaciones.append((posXi, posXf))
            
            i += 1

        listaEstaciones.sort()

        i = 0
        while i < len(listaEstaciones):
            listaXf.append(listaEstaciones[i][1])
            listaXi.append(listaEstaciones[i][0])

            i += 1
        
        if len(listaEstaciones) > 0 or listaXi[0] <= 0:
            estacionesVoracin(listaXi, listaXf, longitud, nEstaciones)

        else:
            print(-1)


        linea = stdin.readline().strip()
        longitud, nEstaciones = map(int, linea.split())

main()