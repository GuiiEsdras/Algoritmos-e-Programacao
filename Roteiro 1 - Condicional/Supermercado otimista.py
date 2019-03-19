Dia = str(input())
Pre = float(input())
Opc = str(input())
Nom = input()

if Dia == "seg" or Dia == "ter" or Dia == "Qua" and Opc == "ouro":
    PreF = Pre /2
if Dia == "qui" or Dia == "sex" and Pre >= 10.00 or Pre <= 100.00:
    PreF = Pre /3
if Dia == "sab" and Opc == "prata":
    PreF = Pre *3
else:
    PreF = Pre *2

print("O preco do produto {} no dia {} eh {:.2f}".format(Nom, Dia, PreF))