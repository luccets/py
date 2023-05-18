num1 = 0

def sequencia (numero) :
    resto = numero %2
    if resto %2 == 0 :
        print("esse numero é par")
    else:
        print("esse numero é impar")
    while num1 != 0 :
        print("Digite um número inteiro")
        num1 = int(input())
        num2 = (sequencia (num1))