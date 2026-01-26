from sys import stdin
from math import sqrt

def miRegadorVoraz(listaAspersores, largoMetros):
    ans = 1
    
    listaAspersores.sort()

    listaPosXiAspersores = []
    listaPosXfAspersores = []

    xiSeleccionao = -1
    xfSeleccionao = -1

    mayorXF = 0
    i = 0
    while i < len(listaAspersores):
     
        listaPosXiAspersores.append(listaAspersores[i][0])
        listaPosXfAspersores.append(listaAspersores[i][1])

        if listaAspersores[i][0] < 0  and listaAspersores[i][1] > xfSeleccionao:
            xfSeleccionao = listaAspersores[i][1]

        if mayorXF < listaAspersores[i][1]:
            mayorXF = listaAspersores[i][1]

        i += 1
   
    if (listaPosXiAspersores[0] <= 0) and (mayorXF >= largoMetros):

        j = 0
        while ((xfSeleccionao < largoMetros) and (ans != -1)):
            
            intervalosACompetir = []

            while j < len(listaPosXiAspersores) and listaPosXiAspersores[j] <= xfSeleccionao:
                intervalosACompetir.append((listaPosXfAspersores[j], listaPosXiAspersores[j]))
                
                j += 1  

            if len(intervalosACompetir) > 0:
                xfSeleccionao, xiSeleccionao = max(intervalosACompetir)
                ans += 1
                
            else:
                ans -= 1

    else: 
        ans = -1
        
    return ans


def main():

    linea = stdin.readline().strip()

    while linea != "":

        nAspersores, largoMetros, anchoMetros = map(int, linea.split())
        
        listaAspersores = []

        i = 0
        while i < nAspersores:
            
            posicion, radio = map(int, stdin.readline().split())
            
            if radio > (anchoMetros/2):
               
                distanciaHorizontal = sqrt((radio*radio) - ((anchoMetros / 2)*(anchoMetros / 2)))
                
                posXi = posicion - distanciaHorizontal
                posXf = posicion + distanciaHorizontal

                if posXi < -1:
                    posXi = -1

                if posXf > largoMetros + 1:
                    posXf = largoMetros + 1

                listaAspersores.append((posXi, posXf))
                
            i += 1

        if len(listaAspersores) > 0:
            ans = miRegadorVoraz(listaAspersores, largoMetros)
            
        else:
            ans = -1
        
        print(ans)

        linea = stdin.readline().strip()

main()