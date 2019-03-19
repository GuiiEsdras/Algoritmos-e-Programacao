def soma_dos_digitos(n):
  if n == 0:
    return 0
  else:
    return (n % 10) + soma_dos_digitos(n // 10)

nums = [int(x) for x in input().split()]
n = str(nums[0]) *nums[1]
n = int(n)
tam = soma_dos_digitos(n)

while tam > 10:
    tam = soma_dos_digitos(tam)
print(tam)