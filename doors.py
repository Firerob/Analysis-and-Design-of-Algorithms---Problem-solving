from sys import stdin
import math

def main():

    numeroBoys = int(stdin.readline())
    while numeroBoys != 0:

        high = numeroBoys
        low = 1
        if numeroBoys > 1:
            while (high - low) > 0:
                
                mid = low + ((high - low) // 2)
                
                if (mid * mid) <= numeroBoys:
                    low = mid + 1

                else:
                    high = mid

                casillero = high - 1

            print(casillero * casillero)

        else:
            print("1")

        numeroBoys = int(stdin.readline())

main()