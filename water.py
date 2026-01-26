# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 10/10/25

from sys import stdin

def miRegadorReintenton(i, totalFlujoAsignao, campo, nAspersores, listaPosAspersores, maxFlujoAgua, listaFlujosMaximos, largoCampo, contador):
    global regadasDeCampo
    global flagMejor

    if flagMejor != True:
        if i == nAspersores:
            
            if contador == largoCampo:
                print(contador)
                flagMejor = True
            
            regadasDeCampo.append(contador)       

        
        else:
            flag = True
            x = 0
            while x <= listaFlujosMaximos[i] and flag == True:

                flujoAsignar = x
            
                if (totalFlujoAsignao + flujoAsignar) <= maxFlujoAgua:
                    totalFlujoAsignao += flujoAsignar

                    posXi = listaPosAspersores[i] - flujoAsignar
                    posXf = listaPosAspersores[i] + flujoAsignar
                    
                    newContador = 0

                    newCampo = campo[:]
                    if posXi != posXf:
                        for k in range(posXi, posXf+1):
                            if 1 <= k <= largoCampo + 1:
                                
                                if newCampo[k] == False:
                                    newContador += 1

                                newCampo[k] = True           
                    
                    #print(campo)
                    if totalFlujoAsignao == maxFlujoAgua:
                        miRegadorReintenton(len(listaPosAspersores), totalFlujoAsignao, newCampo, nAspersores, listaPosAspersores, maxFlujoAgua, listaFlujosMaximos, largoCampo, contador+newContador)

                    else:
                        miRegadorReintenton(i + 1, totalFlujoAsignao, newCampo, nAspersores, listaPosAspersores, maxFlujoAgua, listaFlujosMaximos, largoCampo, contador+newContador)

                            
                    totalFlujoAsignao -= flujoAsignar


                else:
                    flag = False

                
                x += 1


def main():

    casos = int(stdin.readline().strip())
    while casos != 0:

        largoCampo = int(stdin.readline().strip())
        nAspersores = int(stdin.readline().strip())
        listaPosAspersores = list(map(int, stdin.readline().split()))
        maxFlujoAgua = int(stdin.readline().strip())
        listaFlujosMaximos = list(map(int, stdin.readline().split()))

        campo = [False for _ in range(largoCampo + 1)]

        global regadasDeCampo
        regadasDeCampo = []

        global flagMejor
        flagMejor = False

        miRegadorReintenton(0, 0, campo, nAspersores, listaPosAspersores, maxFlujoAgua, listaFlujosMaximos, largoCampo, 0)
        
        if flagMejor == False:
            print(max(regadasDeCampo))


        casos -= 1

main()