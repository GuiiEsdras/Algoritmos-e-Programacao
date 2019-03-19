def dec_2_bin(n):
    if n < 2:
        print(n)
    else:
        dec_2_bin(n // 2)
        print(n % 2)


n = int(input())
dec_2_bin(n)