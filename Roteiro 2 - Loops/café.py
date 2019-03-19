XICARAS_POR_CAPSULA = 2
CX_PEQUENA = 10
CX_GRANDE = 16
PROFESSORES = 7

QUANT_CAPS_TOTAL = 0

for x in range(PROFESSORES):
    quant_cxs = int(input())
    tamn_cxs = input()

    if tamn_cxs == "p" or tamn_cxs == "P":
        QUANT_CAPS_TOTAL += quant_cxs * CX_PEQUENA

    elif tamn_cxs == "g" or tamn_cxs == "G":
        QUANT_CAPS_TOTAL += quant_cxs * CX_GRANDE

print(QUANT_CAPS_TOTAL)
print(int(QUANT_CAPS_TOTAL*2/PROFESSORES))