# Nombre: Daniel Felipe Moncada Tello
# Codigo: 8976528 
# Fecha: 14/10/25

from sys import stdin

dicc = { 'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01,
         'h': 0.70, 'i': 6.25, 'j': 0.44, 'k': 0.00, 'l': 4.97, 'm': 3.15, 'n': 6.71,
         'o': 8.68, 'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93,
         'v': 0.90, 'w': 0.02, 'x': 0.22, 'y': 0.90, 'z': 0.52 }

vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

resultadosPrev = {}

def promLoquito(i, tamPalabra, tipoLetra, valorAcum):
    global ansTotal
    global totalPalabras
    global repes

    if i == tamPalabra:
        ansTotal += valorAcum
        totalPalabras += 1

    else:
        # vocal
        if tipoLetra == 'V':
            x = 0
            while x < len(vocales):

                newLetra = vocales[x]
                repeAux = repes[newLetra] + 1

                if repeAux <= 2:
                    repes[newLetra] += 1

                    nuevoValorAcum = valorAcum + (i+1) * dicc[newLetra]

                    promLoquito(i + 1, tamPalabra, 'C', nuevoValorAcum)
                    
                    repes[newLetra] -= 1

                    
                x += 1

        # consonante
        else:
            x = 0
            while x < len(consonantes):
                
                newLetra = consonantes[x]
                repeAux = repes[newLetra] + 1
                
                if repeAux <= 2:
                    repes[newLetra] += 1

                    nuevoValorAcum = valorAcum + (i+1) * dicc[newLetra] 

                    promLoquito(i + 1, tamPalabra, 'V', nuevoValorAcum)

                    repes[newLetra] -= 1

                
                x += 1

def tamoLoco(palabrita):

    ans = 0
    i = 0
    while i < len(palabrita):
        auxL = palabrita[i]
        ans += (i+1) * dicc[auxL]

        i += 1

    return ans


def main():
    
    casos = int(stdin.readline().strip())
    while casos != 0:

        palabrita = stdin.readline().strip()

        ansSBC = tamoLoco(palabrita)

        if (palabrita[0], len(palabrita)) in resultadosPrev:
            ansPromedio =  resultadosPrev[(palabrita[0], len(palabrita))]
        
        else:
            global repes

            repes = {
                'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
            }


            global ansTotal
            ansTotal = 0

            global totalPalabras
            totalPalabras = 0
            
            valorAcum = 1 * dicc[palabrita[0]]
            repes[palabrita[0]] += 1

            promLoquito(1, len(palabrita), 'V', valorAcum)

            ansPromedio = ansTotal / totalPalabras 

            
            

        if ansSBC >= ansPromedio:
            print("above or equal")
        
        else:
            print("below")


        resultadosPrev[(palabrita[0], len(palabrita))] = ansPromedio
        


        casos -= 1

main()