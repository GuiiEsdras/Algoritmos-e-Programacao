OpcaoDeCarnes = input()

if (OpcaoDeCarnes == "C" or OpcaoDeCarnes == "BF" or OpcaoDeCarnes == "BS"):
    PaoDeAlho = input()
    BebidasAd = input()
    BebidasCr = input()
    QuantCri = int(input())
    QuantAdu = int(input())

    PrecoTotal = 0

    if OpcaoDeCarnes == "C":
        CarneBovina = ((32.00 / 1000) * 200) * (QuantCri + QuantAdu)
        CarneDeFrango = ((18.00 / 1000) * 100) * QuantAdu
        CarneSuina = ((15.00 / 1000) * 100) * QuantAdu
        PrecoTotal = PrecoTotal + CarneBovina + CarneDeFrango + CarneSuina

    elif OpcaoDeCarnes == "BF":
        CarneBovina = (((32.00 / 1000) * 250) * (QuantAdu)) + (((32.00 / 1000) * 200) * (QuantCri))
        CarneDeFrango = ((18.00 / 1000) * 150) * QuantAdu
        PrecoTotal = PrecoTotal + CarneBovina + CarneDeFrango

    elif OpcaoDeCarnes == "BS":
        CarneBovina = (((32.00 / 1000) * 250) * (QuantAdu)) + (((32.00 / 1000) * 200) * (QuantCri))
        CarneSuina = ((15.00 / 1000) * 150) * QuantAdu
        PrecoTotal = PrecoTotal + CarneBovina + CarneSuina

    if BebidasAd == "S":
        PrecoTotal = PrecoTotal + (QuantAdu * 16.00)

    if BebidasCr == "S":
        PrecoTotal = PrecoTotal + (QuantCri * 3.00)

    if PaoDeAlho == "S":
        print("R$: {:.2f}".format(PrecoTotal))

    else:
        PrecoTotal = PrecoTotal - (PrecoTotal * 0.02)
        print("R$: {:.2f}".format(PrecoTotal))

else:
    print("Opção inválida.")