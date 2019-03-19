TipoTemp = input()
Temperatura = float(input())

CtoF = Temperatura * 1.8 +32
CtoK = round(Temperatura + 273.15,2)
FtoC = round(((Temperatura - 32) * (5/9)),2)
FtoK = round((Temperatura + 459.67) * (5/9),3)
KtoC = round(Temperatura - 273.15,2)
KtoF = Temperatura * (9/5) - 459.67

if (TipoTemp == "C" and Temperatura >= -273.0):
    print(str(CtoF) + " F")
    print(str(CtoK) + " K")
elif (TipoTemp == "K" and Temperatura >0.0):
    print(str(KtoC) + " C")
    print(str(KtoF) + " F")
elif (TipoTemp == "F" and Temperatura >= -459.67):
    print(str(FtoC) + " C")
    print(str(FtoK) + " K")
else:
    print("Valor de temperatura abaixo do minimo")