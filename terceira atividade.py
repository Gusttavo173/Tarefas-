import math

def calcular_bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "A equação não possui raízes reais"
    
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    
    return x1, x2

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("O valor de 'a' deve ser diferente de zero para uma equação quadrática.")
else:
    
    resultado = calcular_bhaskara(a, b, c)
    
    
    if isinstance(resultado, tuple):
        print(f"As raízes da equação são: x1 = {resultado[0]}, x2 = {resultado[1]}")
    else:
        print(resultado)
