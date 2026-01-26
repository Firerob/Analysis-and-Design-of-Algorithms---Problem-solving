# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 16/10/25

from sys import stdin

def Resolvedorsito(i, cadenita, combi, tamCombiR):

    letrasUsadas = set()

    if len(combi) == tamCombiR:
        print(''.join(combi))
        
    else:
        
        while i < len(cadenita):
            if cadenita[i] not in letrasUsadas:
                
                combi.append(cadenita[i])
                #print(combi)
                Resolvedorsito(i+1, cadenita, combi, tamCombiR)
                combi.pop()
                #print(combi)

                letrasUsadas.add(cadenita[i])

            i += 1
    
def main():
    linea = stdin.readline().strip()
    
    while linea != "":

        cadenaS, tamCombiR = linea.split()
        cadenita = []
        tamCombiR = int(tamCombiR)

        contador = {}

        i = 0
        while i < len(cadenaS):
            if cadenaS[i] in contador:
                contador[cadenaS[i]] += 1
            else:
                contador[cadenaS[i]] = 1

            if contador[cadenaS[i]] <= tamCombiR:   
                cadenita.append(cadenaS[i])
           
            i += 1

        cadenita.sort()

        combi = []

        if len(cadenita) == tamCombiR:
            print(''.join(cadenita))

        else:
            Resolvedorsito(0, cadenita, combi, tamCombiR)


        linea = stdin.readline().strip()

main()