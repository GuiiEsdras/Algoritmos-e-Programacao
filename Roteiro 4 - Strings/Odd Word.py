text = input().split()
for pos, palavra in enumerate(text):
    if pos % 2 != 0:
        text[pos] = palavra[::-1]
for pos, palavra in enumerate(text):
    print(palavra, end=' ')