# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 21/09/25

from sys import stdin

def main():

    linea = stdin.readline().strip()

    while linea != "":

        numeroS = int(linea)

        minimoOperaciones = 0
        
        while numeroS > 0:

            if (numeroS % 2) == 0:
                numeroS = numeroS // 2
            
            else:
                
                if (numeroS < 4) or (numeroS % 4) == 1:
                    numeroS -= 1
                else:
                    numeroS += 1

            minimoOperaciones += 1

        

        print(minimoOperaciones)


        linea = stdin.readline().strip()

main()