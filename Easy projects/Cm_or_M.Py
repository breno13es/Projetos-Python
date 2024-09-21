comprimento = float(input("Quanto mediu?: "))
medida = str(input("Tranformar em (C) ou (M): "))

if medida.upper() == "M":
    comprimento = (comprimento / 100)
    Modo = "M"

elif medida.upper() == "C":
    comprimento = str(comprimento * 100)
    Modo = "Cm"
print(f"Seu valor é de " + str(comprimento ) + (Modo))