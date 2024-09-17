

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def exibir_menu():
    print("Escolha a forma geométrica para calcular a área:")
    print("1 - Retângulo")
    print("2 - Triângulo")
    print("3 - Círculo")

exibir_menu()

escolha = int(input("Digite o número da forma geométrica: "))

if escolha == 1:
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = calcular_area_retangulo(base, altura)
    print(f"A área do retângulo é: {area}")
    
elif escolha == 2:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = calcular_area_triangulo(base, altura)
    print(f"A área do triângulo é: {area}")
    
elif escolha == 3:
    raio = float(input("Digite o raio do círculo: "))
    area = calcular_area_circulo(raio)
    print(f"A área do círculo é: {area}")
    
else:
    print("Escolha inválida. Tente novamente.")
