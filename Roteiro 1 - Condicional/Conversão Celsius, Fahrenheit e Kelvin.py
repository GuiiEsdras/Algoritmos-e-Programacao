M = input()
T = float(input())

CF = T * 1.8 + 32
CK = T + 273.15
FC = (T - 32) / 1.8
FK = (T + 459.67) / 1.8
KC = T - 273.15
KF = T * 1.8 - 459.67

if M == "C" and T >= -273:
    print("{:.1f} F".format(CF))
    print("{:.2f} K".format(CK))
elif M == "F" and T >= -459.67:
    print("{:.2f} C".format(FC))
    print("{:.3f} K".format(FK))
elif M == "K" and T >= 0.0:
    print("{:.2f} C".format(KC))
    print("{:.2f} F".format(KF))
else:
    print("Valor de temperatura abaixo do minimo")