def MDC(a, b):
    if a % b == 0:
        return b
    else:
        return MDC(b, a % b)


a = int(input())
b = int(input())
print(MDC(a, b))