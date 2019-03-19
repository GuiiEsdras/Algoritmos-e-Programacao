def mdc(a,b):
    return a if not b else mdc(b, a % b)
n = int(input())
for x in range(n):
    a, b = [int(x) for x in input().split()]
    print("MDC({},{}) = {}".format(a, b, mdc(a,b)))