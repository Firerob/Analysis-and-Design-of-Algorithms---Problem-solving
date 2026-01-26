# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 8/10/25

from sys import stdin


def operandoNumeritos(i, valorAcum, numeritos, numsUsados):
    #print(numsUsados)
    #print(valorAcum)
    global flagPosible

    if flagPosible != True:
        
        if i == 5:

            if valorAcum == 23:
                flagPosible = True
            
        else:
            x = 0
            while x < len(numsUsados):
                
                if numsUsados[x] == False:
                    
                    numsUsados[x] = True


                    #resta
                    nuevoValor = valorAcum - numeritos[x]
                    if nuevoValor >= -150: 
                        operandoNumeritos(i + 1, nuevoValor, numeritos, numsUsados)

                    #multiplicacion
                    nuevoValor = valorAcum * numeritos[x] 
                    if nuevoValor <= 150 and nuevoValor >= -150: 
                        operandoNumeritos(i + 1, nuevoValor, numeritos, numsUsados)


                    #suma
                    nuevoValor = valorAcum + numeritos[x]
                    if nuevoValor <= 150: 
                        operandoNumeritos(i + 1, nuevoValor, numeritos, numsUsados)

    
                    numsUsados[x] = False

                x += 1


def main():

    numeritos = list(map(int, stdin.readline().split()))
    listaFlag = [0, 0, 0, 0, 0]

    while numeritos != listaFlag:

        global flagPosible
        flagPosible = False
        
        flagTalvez = False
        
        i = 0
        while i < len(numeritos):
            if (numeritos[i]) % 2 != 0:
                flagTalvez = True
            
            i += 1
        
        if flagTalvez != True:
            print("Impossible")

        else:
            
            i = 0
            while i < len(numeritos) and flagPosible == False:

                numsUsados = [False for _ in range(len(listaFlag))]
                numsUsados[i] = True
                operandoNumeritos(1, numeritos[i], numeritos, numsUsados)

                i += 1

            if flagPosible == True:
                print("Possible")
            else:
                print("Impossible")


        numeritos = list(map(int, stdin.readline().split()))

main()