n = c = s = 0
while True:
    n = int(input())
    if n == 0:
        break
    s += n
    c += 1
    m = s / c
if m < 110:
    print("Glicose Normal")
elif m >= 200:
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")