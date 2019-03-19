def eh_primo(n):
    if n == 1:
        return False

    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    return primo

nums = [int(x) for x in input().split()]

sao_primos = True
for i in nums:
    if not(eh_primo(i)):
        sao_primos = False

prod = 1
if sao_primos:
    for i in range(len(nums)):
        prod *= nums[i]
    print(prod)
else:
    print('SEM PRODUTO')