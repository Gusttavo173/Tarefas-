

def calcular_media(valor1, valor2, valor3, valor4):
    media = (valor1 + valor2 + valor3 + valor4) / 4
    return media

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
valor4 = float(input("Digite o quarto valor: "))

media = calcular_media(valor1, valor2, valor3, valor4)
print(f"A média dos valores é: {media}")
