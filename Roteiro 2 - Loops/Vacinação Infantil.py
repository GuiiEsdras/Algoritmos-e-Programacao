PrimeiraDose = int(input())
Tempo = int(input())
SegundaDose = PrimeiraDose + (2 - 1) * Tempo
QuartaDose = PrimeiraDose + (4 - 1) * Tempo
for x in range(SegundaDose, QuartaDose + Tempo, Tempo):
    print("{}".format(x), end=" ")