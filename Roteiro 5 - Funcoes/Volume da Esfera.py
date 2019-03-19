def VolumeEsfera(r):
    pi = 3.1416
    volume = (4 * pi * r**3) /3
    return volume

r1 = float(input())
r2 = float(input())
r3 = float(input())

print("{:.2f}".format(VolumeEsfera(r1)))
print("{:.2f}".format(VolumeEsfera(r2)))
print("{:.2f}".format(VolumeEsfera(r3)))
