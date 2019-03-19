# SB = Salário Base
# HE = Horas Extras
SB = float(input())
HE = int(input())

#SF = Salário Final
SF1 = (SB / 44) * HE
SF2 = (SF1/100) *10
SF3 = SB + SF1 + SF2

print("{:.2f}".format(SF3))