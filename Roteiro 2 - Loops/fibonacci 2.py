[i,j] = [0,1]

f = int(input(""))

for n in range(0,f):
  k = i + j
  if (n!=f-1):
    print(k,end=', ')
  else:
    print(k,end='.')
  j=i
  i=k