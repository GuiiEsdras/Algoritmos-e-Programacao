N1 = int(input())
N2 = int(input())
N3 = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())

a = (N1 + N2 + N3) /3
p = ((N1*p1) + (N2*p2) + (N3*p3)) / (p1+p2+p3)
h = 3/(1/N1+1/N2+1/N3)

print("a: {:.1f}".format(a))
print("p: {:.1f}".format(p))
print("h: {:.1f}".format(h))