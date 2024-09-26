U = int(input("Quantas horas você trabalha no dia?: "))
U_M = float(input("Quanto você ganha por hora?: "))

S_B = (U_H * U_M)
S = S_B * 30

IR = (S * 11 / 100)
IN = (S * 8 / 100)
S_P = (S * 5 / 100)

L = (S - S_P) - IN - IR

print(
    f"+ Salário Bruto : R${S:.2f}\n"
    f"- IR (11%) : R${IR:.2f}\n"
    f"- INSS (8%) : R${IN:.2f}\n"
    f"- Sindicato (5%) : R${S_P:.2f}\n"
    f"= Salário Liquido : R${L:.2f}"
)