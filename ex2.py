from cmath import sqrt
import math
def raiz (n1) :
    result = math.sqrt(n1)
    return result

print ("digite um numero para ser calculado a raiz")
num1 = int(input())
resultado = raiz (num1)
print(f"A raiz é: {resultado}")
